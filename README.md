<img src="https://i.ibb.co/DtHQ3FG/802x265-Logo-GT.png" width="400"> 

## Grupo Turing
# Visão Computacional: Projeto de Satélites
#### Por: [Luísa Heise](https://github.com/luisaheise); [Rodrigo Estevam](https://github.com/materloki); [Camila Fonseca](https://github.com/fonsecamilla); [Noel Eliezer](https://github.com/anor4k); [Luis Henrique](https://github.com/luish18); [Wesley de Almeida](https://github.com/WesPereira); [Rodrigo Fill](https://github.com/rodrigofill)

## Imagens de satélite

### Resolução
Imagens de satélite podem ser diferenciadas por quatro tipos distintos de resolução:

* **Resolução Espectral**: Região do espectro eletromagnético observado em cada banda eletromagnética de casa imagem.
* **Resolução Espacial**: Área superficial coberta por cada pixel da imagem.
* **Resolução Temporal**: Período de tempo de aquisição de cada imagem de satélite.
* **Resolução Radiométrica**: A menor diferença de energia observada da reflectância eletromagnética.

Atualmente diferentes algoritmos são amplamente aplicados quando utilizados em modelos baseados em imagens de satélite, entre eles temos a transformada wavelet discreta (DWT) e SOM (Self-Organizing Maps). Em geral há uma preferência pelo uso de métodos não supervisionados para aderessar os desafios intrinsecos à esse tipo de dado uma vez que labels totalmente corretos são quase sempre inexistentes. 

### Canais
As imagens de satelite, como dito anteriormente, possuem vários canais e capturam ondas eletromagnéticas fora do espectro visível.  Quais são as bandas/canais e seus intervalos pode depender do satélite em questão, uma estrutura plausível poderia ser:

| Bands              | Wavelength(μm) |
|--------------------|----------------|
| Coastal – Band 1   | 0.43–0.45      |
| Blue – Band 2      | 0.45–0.51      |
| Green – Band 3     | 0.53–0.59      |
| Red – Band 4       | 0.64–0.67      |
| aNIR – Band 5      | 0.85–0.88      |
| aSWIR 1 – Band 6   | 1.57–1.65      |
| SWIR 2 – Band 7    | 2.11–2.29      |
| aPAN – Band 8      | 0.50–0.68      |
| Cirrus – Band 9    | 1.36–1.38      |
| aTIRS 1 – Band 10  | 10.6–11.19     |
| TIRS 2 – Band 11   | 11.5–12.51     |

[Entretanto, outras configurações são possíveis. Os satélites LANDSAT 5 e 7, utilizados pelo INPE, por exemplo, possuem apenas 7 bandas. ](http://www.dgi.inpe.br/Suporte/files/Cameras-LANDSAT57_PT.php)


## Superfícies de reflectância
Reflectância é a proporção entre o fluxo de radiação eletromagnética incidente numa superfície e o fluxo que é refletido. Frequentemente a reflectância é apresentada sob a forma de percentagem

## Índices de refectância

Neste cenário que a busca por índices se torna de grande importância para o estudo destas imagens, estes índices são capazes de reduzir a grande quantidade de informação da imagem de satélite para que a mesma seja mais utilizável. Dentre eles temos o NVDI, o MNVDI e o AWEI.

### Normalized Density Vegetation Index – NDVI
O índice NDVI é a diferença normalizada da vegetação que permite a análise e separação de tipos e densidade de cobertura vegetal pela presença de água foliar. É extraído dos comprimentos de onda em que a vegetação tem alta refletância, infravermelho próximo (NIR), e baixa refletância, vermelho (RED) (HE et al, 2010), conforme representado pela fórmula:

NDVI = (NIR - RED)/(NIR + RED)

### Normalized Density Building Index – NDBI

Proposto por Zha et al, (2003) o Normalized Density Building Index (NDBI) é a diferença normalizada para áreas construídas, com a finalidade de incrementar o número digital destas respectivas áreas nos intervalos das bandas do infravermelho próximo (near-infrared - NIR) e infravermelho médio (mid-infrared - MIR). A fórmula a seguir demonstra a construção do NDBI:

NDBI = (SWIR - NIR)/(SWIR + NIR)

### Normalized Difference Water Index - NDWI

Esse nome pode aludir a dois índices distintos.

Um deles utiliza os canais NIR e SWIR, duas regiões do infravermelho. Ele consegue dizer o conteúdo de água que há na vegetação (folhas). E sua fórmula é:

NDWI = (NIR - SWIR)/(NIR + SWIR)

Há também uma variação que mede a quantidade de água em corpos d’água, que utiliza o canal Verde e NIR, também chamado de MNDWI:

NDWI = (GREEN - NIR)/(GREEN + NIR)

### Automated Water Extraction Index - AWEI

Esse índice também captura água em corpos d’água e deve funcionar melhor que o NDWI, entretanto, precisa de 5 bandas para ser computado e não 2 como o NDWI. Ele vem em duas versões, uma delas (a nsh) é mais eficaz em eliminar pixels que não são água.

AWEInsh =4 (GREEN - SWIR5) - 0.25 NIR + 2.75 SWIR7

AWEIsh =BLUE + 2.5 GREEN - 1.5 (NIR + SWIR5) - 0.25 SWIR7

-------
Esse repositório teve inspiração no seguinte paper

    
    @incollection{JeniceAroma2019,
      doi = {10.1007/978-3-030-24178-0_12},
      url = {https://doi.org/10.1007/978-3-030-24178-0_12},
      year = {2019},
      month = nov,
      publisher = {Springer International Publishing},
      pages = {255--274},
      author = {R. Jenice Aroma and Kumudha Raimond},
      title = {A Wavelet Transform Applied Spectral Index for Effective Water Body Extraction from Moderate-Resolution Satellite Images},
      booktitle = {Remote Sensing and Digital Image Processing}
    }


