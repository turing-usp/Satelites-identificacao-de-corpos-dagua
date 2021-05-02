from pathlib import Path
import pandas as pd
import numpy as np
import urllib.request
from tqdm import tqdm
import gdown
from typing import List
import argparse
import time


_LOCATIONS_URL = 'https://drive.google.com/file/d/1is3apsPQ8IZtK0Fu6y250Ks5I69TLzW8/view?usp=sharing'
_LANDSAT_URL = 'https://s3-us-west-2.amazonaws.com/landsat-pds/c1/L8/{path}/{row}/{productId}/{productId}_{band}'


def _get_locations_dataframe(url: str = _LOCATIONS_URL,
                             output_path = 'data') -> pd.DataFrame:
    file_id = url.split('/')[-2]
    dwn_url='https://drive.google.com/uc?export=download&id=' + file_id
    output_path = Path(output_path)
    output_path.mkdir(parents=True, exist_ok=True)
    if not Path(f'{output_path.name}/scene_list.csv').exists():
        gdown.download(dwn_url, f'{output_path.name}/scene_list.csv')
    df = pd.read_csv(f'{output_path.name}/scene_list.csv')
    return df


class RegionGetterImages():
    """
    Classe que manipula e faz download das imagens.
    """

    def __init__(self, lat: float, lon: float, region_name: str) -> None:
        """
        Construtor de uma instância da classe.

        Args:
            lat (float): latitude de interesse
            lon (float): longitude de interesse
            region_name (str): nome da região de interesse
        """
        self.lat = lat
        self.lon = lon
        self.region_name = region_name

    def is_in_square(self, max_lon: float, max_lat: float,
                     min_lon: float, min_lat: float) -> bool:
        """
        Verifica se lat e lon estão dentro de um determinado retângulo.

        Args:
            max_lon (float): longitude máxima
            max_lat (float): latitude máxima
            min_lon (float): longitude mínima
            min_lat (float): latitude mínima

        Returns:
            Retorna True se lat e lon estão contidos. False caso o contrário.
        """
        in_square = False
        if min_lat <= self.lat <= max_lat:
            if min_lon <= self.lon <= max_lon:
                in_square = True
        return in_square

    def find_coord_datasets(self, scene_list: pd.DataFrame) -> pd.DataFrame:
        """
        A partir da lista de cenas retorna as informações da região para a
        latitude e longitude passadas na criação da classe.

        Args:
            scene_list (pd.DataFrame): lista de cenas com as informações

        Returns:
            pd.DataFrame da região para lat e lon.
        """
        filter_df = scene_list.apply(
            lambda row: self.is_in_square(
                row['max_lon'],
                row['max_lat'],
                row['min_lon'],
                row['min_lat']
            ), axis=1)
        return scene_list.loc[np.array(filter_df)]
    
    def get_bands_images(self, path: str, row: int, product_id: str, region: str,
                        bands: List[str], outputbasepath: str) -> None:
        """
        Com base nas informações da região faz o download das imagens.

        Args:
            path (str): caminho para a requisição
            row (int): row para a requisição
            product_id (str): Id do produto para a requisição
            region (str): nome da região
            bands (List[str]): lista de bandas de interesse
            outputbasepath (str): caminho base onde as imagens serão salvas
        """
        out_path = Path(f'{outputbasepath}/{region}/{product_id}')
        out_path.mkdir(parents=True, exist_ok=True)
        
        for band in bands:
            
            params = {
                'path': '{:0>3d}'.format(path),
                'row': '{:0>3d}'.format(row),
                'productId': product_id,
                'band': band
            }

            url = _LANDSAT_URL.format(**params)
            if not Path(f'{str(out_path)}/{band}').exists():
                urllib.request.urlretrieve(url, f'{str(out_path)}/{band}')
    
    def get_images(self,
        scene_list: pd.DataFrame,
        bands: List[str] = ['thumb_small.jpg','B3.TIF','B5.TIF'],
        outputbasepath = 'images') -> None:
        """
        Função principal que chamas as demais para fazer download das imagens

        Args:
            scene_list (pd.DataFrame): lista de cenas para achar informações
            da região
            bands (List[str], optional): bandas de interesse
            outputbasepath (str, optional): caminho base para salvar as imagens
        """
        start = time.time()
        print(f"[INFO] Encontrando região para os pontos passados...")
        region_data = self.find_coord_datasets(scene_list)
        print("[INFO] Região encontrada! Tempo: {:.4f}s".format(
            time.time() - start
        ))
        lines = 0
        for i, row in tqdm(region_data.iterrows()):
            print(f"[INFO] Fazendo download do produto {row['productId']}")
            self.get_bands_images(
                row['path'],
                row['row'],
                row['productId'],
                self.region_name,
                bands,
                outputbasepath
            )
            lines += 1


if __name__ == "__main__":
    """
    Função principal do programa.
    """
    parser = argparse.ArgumentParser(
        description="Faz download das imagensdo s2 baseado na lat e lon"
    )

    parser.add_argument(
        "--lat",
        dest="lat",
        default=0,
        type=float,
        help="Latitude de referência"
    )

    parser.add_argument(
        "--lon",
        dest="lon",
        default=0,
        type=float,
        help="Longitude de referência"
    )

    parser.add_argument(
        "--region",
        dest="region",
        default="BR",
        type=str,
        help="Nome da região"
    )

    parser.add_argument(
        "--out",
        dest="out",
        default="images",
        type=str,
        help="Pasta de destino"
    )

    parse_args = parser.parse_args()

    region_getter = RegionGetterImages(
        parse_args.lat,
        parse_args.lon,
        parse_args.region
    )

    start = time.time()
    print("[INFO] Iniciando busca do arquivo scene_list...")
    df = _get_locations_dataframe()
    print("[INFO] Fim da busca do arquivo scene_list. Tempo: {:.4f}s".format(
        time.time() - start
    ))

    start = time.time()
    print("[INFO] Iniciando download das imagens...")
    region_getter.get_images(scene_list=df, outputbasepath=parse_args.out)
    print("[INFO] Fim do download das imagens. Tempo: {:.4f}s".format(
        time.time() - start
    ))
