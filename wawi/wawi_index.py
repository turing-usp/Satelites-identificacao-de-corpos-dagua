import pywt
import numpy as np
from typing import Tuple
from osgeo import gdal
import matplotlib.image as mpimg
from wawi.utils.clustering import *


class WaWi():
    """
    Classe representando o índice para uma imagem.
    """
    
    def __init__(self,b3_path: str, b5_path: str, thumb_path: str) -> None:
        """
        Construtor de uma instância da classe.

        Args:
            b3_path (str): caminho base para a banda b3
            b5_path (str): caminho base para a banda b5
            thumb_path (str): caminho base para a thumb
        """
        self.b5_img = gdal.Open(b5_path, 0)
        self.b3_img = gdal.Open(b3_path, 0)
        self.sr5_array = self.b5_img.GetRasterBand(1).ReadAsArray()
        self.sr3_array = self.b3_img.GetRasterBand(1).ReadAsArray()
        self.rgb_img = mpimg.imread(thumb_path)


    def index(self, b5_norm: np.ndarray, b3_norm: np.ndarray,
        w: str = 'db1') -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Recebe as bandas b3 e b5 corrigidas e retorna o WaWI da imagem.

        Args:
            b5_norm (np.ndarray): array da banda b5
            b3_norm (np.ndarray): array da banda b3
            w (str, optional): tipo da transformada Wavelet aplicada às bandas

        Returns:
            Retorna o WaWI, assim como as próprias bandas b3 e b5 aproximadas
            pela transformada Wavelet.
        """
        
        # Aplicando a transformada Wavelet
        n = 1
        w = w
        b5_coeffs = pywt.wavedec2(b5_norm, wavelet=w, level=n)
        Ab5 = b5_coeffs[0]
        b3_coeffs = pywt.wavedec2(b3_norm, wavelet=w, level=n)
        Ab3 = b3_coeffs[0]
        
        # Cálculo do índice
        index = (np.log(Ab5) - np.log(Ab3))/(np.log(Ab5) + np.log(Ab3))
        
        return index, Ab5, Ab3
    
    def index_pipeline(self, w: str = 'db1',
        n_clusters: int = 5) -> Tuple[np.ndarray, np.ndarray]:
        """
        Realiza o pipeline para extração do índice.

        Args:
            w (str, optional): tipo da transformada Wavelet aplicada às bandas
            n_clusters (int, optional): número de clusters

        Returns:
            WaWI final e WaWI bizarizado.
        """
        b5_norm = normaliza(self.sr5_array, (1,2))
        b3_norm = normaliza(self.sr3_array, (1,2))
        wawi_index, _, _ = self.wawi(b5_norm, b3_norm, w)
        wawi_index_norm = normaliza(wawi_index, (0,1))
        wawi_final, water_cluster = constroe_kmeans_clusters(
            wawi_index_norm,
            n_clusters = n_clusters
        )
        wawi_final_bin = binariza_label(wawi_final, water_cluster)
        return wawi_final, wawi_final_bin
