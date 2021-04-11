import pywt
import numpy as np
from osgeo import gdal
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.metrics import jaccard_score
from skimage.metrics import structural_similarity as ssim
from scipy.stats import pearsonr
import cv2 as cv
from sklearn.cluster import KMeans, DBSCAN
import sys
from utils.clustering import *


class WaWi():
    def __init__(self,b3_path, b5_path, thumb_path):
        self.b5_img = gdal.Open(b5_path, 0)
        self.b3_img = gdal.Open(b3_path, 0)
        self.sr5_array = self.b5_img.GetRasterBand(1).ReadAsArray()
        self.sr3_array = self.b3_img.GetRasterBand(1).ReadAsArray()
        self.rgb_img = mpimg.imread(thumb_path)


    def index(self,b5_norm, b3_norm, w = 'db1'):
        '''
        Recebe as bandas b3 e b5 corrigidas e retorna o
        WaWI da imagem.
        '''
        
        # Aplicando a transformada Wavelet
        n = 1
        w = w
        b5_coeffs = pywt.wavedec2(b5_norm,wavelet=w,level=n)
        Ab5 = b5_coeffs[0]
        b3_coeffs = pywt.wavedec2(b3_norm,wavelet=w,level=n)
        Ab3 = b3_coeffs[0]
        
        # Cálculo do índice
        index = (np.log(Ab5) - np.log(Ab3))/(np.log(Ab5) + np.log(Ab3))
        
        return index, Ab5, Ab3
    
    def index_pipeline(self, w= 'db1', n_clusters=5):
        b5_norm = normaliza(self.sr5_array, (1,2))
        b3_norm = normaliza(self.sr3_array, (1,2))
        wawi_index, _, _ = self.wawi(b5_norm, b3_norm, w)
        wawi_index_norm = normaliza(wawi_index, (0,1))
        wawi_final, water_cluster = make_kmeans_clusters(wawi_index_norm, n_clusters = n_clusters)
        wawi_final_bin = binariza_label(wawi_final, water_cluster)
        return wawi_final, wawi_final_bin