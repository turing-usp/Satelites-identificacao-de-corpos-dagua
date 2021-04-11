import numpy as np
from sklearn.cluster import KMeans, DBSCAN

def normaliza(img, limits = (0,1)):
    '''
    Função que recebe uma imagem (i.e. uma das bandas) e 
    normaliza com valores entre limits.
    '''
    menor = np.min(img)
    maior = np.max(img)
    return np.interp(img, (menor, maior), limits)

def binariza(img, threshold = 0.6):
    '''
    Função que recebe uma imagem (i.e. uma das bandas) e 
    eretorna a imagem filtrada por uma máscara com o
    threshold passado.
    '''
    mascara = np.array(img > threshold, dtype=int)
    return mascara * img

def binariza_label(img, label):
    '''
    Função que recebe uma imagem (i.e. uma das bandas) e 
    eretorna a imagem filtrada por uma máscara com o
    threshold passado.
    '''
    mascara = np.array(img == label, dtype=int)
    return mascara * img

def make_kmeans_clusters(wawi_index_norm, n_clusters = 5):
    Z = wawi_index_norm.reshape((-1,1))
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(Z)
    centers = kmeans.cluster_centers_
    water_cluster = np.argmin(centers)
    labels = kmeans.predict(Z)
    clustered_wawi = labels.reshape(wawi_index_norm.shape)
    return clustered_wawi, water_cluster

def histogram(img):
    img.reshape((-1,1))
    plt.hist(img)
    plt.show()