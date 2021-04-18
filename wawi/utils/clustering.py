from typing import Tuple
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def normaliza(img: np.ndarray, limits: Tuple[int, int] = (0,1)) -> np.ndarray:
    """
    Função que recebe uma imagem (i.e. uma das bandas) e normaliza com
    valores entre limits.

    Args:
        img (np.ndarray): imagem alvo
        limits (Tuple[int, int], optional): limites de normalização;

    Returns:
        Imagem normalizada entre limits.
    """
    menor = np.min(img)
    maior = np.max(img)
    return np.interp(img, (menor, maior), limits)


def binariza(img: np.ndarray, threshold: float = 0.6) -> np.ndarray:
    """
    Função que recebe uma imagem (i.e. uma das bandas) e retorna a imagem
    filtrada por uma máscara com o threshold passado.

    Args:
        img (np.ndarray): imagem alvo
        threshold (float, optional): threshold para binarizar

    Returns:
        Imagem binarizada com o threshold passado.
    """
    mascara = np.array(img > threshold, dtype=int)
    return mascara * img


def binariza_label(img: np.ndarray, label: np.ndarray) -> np.ndarray:
    """
    Função que recebe uma imagem (i.e. uma das bandas) e retorna a imagem
    filtrada pela máscara passada.

    Args:
        img (np.ndarray): imagem alvo
        label (np.ndarray): máscara de filtragem

    Returns:
        Imagem filtrada pela máscara.
    """
    mascara = np.array(img == label, dtype=int)
    return mascara * img


def constroe_kmeans_clusters(wawi_index_norm: np.ndarray,
    n_clusters: int = 5) -> Tuple[np.ndarray, int]:
    """
    Aplica o algotimo de K-Means a imagem passada com o número de clusters
    passado e retorna o cluster da água.

    Args:
        wawi_index_norm (np.ndarray): imagem com o índice wawi aplicado
        n_clusters (int, optional): número de clusters

    Returns:
        Cluster para água, assim como seu índice.
    """
    z = wawi_index_norm.reshape((-1,1))
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(z)
    centers = kmeans.cluster_centers_
    water_cluster = np.argmin(centers)
    labels = kmeans.predict(Z)
    clustered_wawi = labels.reshape(wawi_index_norm.shape)
    return clustered_wawi, water_cluster


def histograma(img: np.ndarray) -> None:
    """
    Plota o histograma de uma imagem.

    Args:
        img (np.ndarray): imagem alvo
    """
    img.reshape((-1,1))
    plt.hist(img)
    plt.show()
