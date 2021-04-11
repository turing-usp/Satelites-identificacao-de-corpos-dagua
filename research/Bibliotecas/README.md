## Raster Image
De um modo geral, informações do tipo *raster* contém uma localização e um grid de célular preenchidos com valores. Ainda que esses valores sejam null. <br>
**Multi band** rasters são matrizes de *raster* uma em cima da outra. <br>
Imagens como .jpeg, .jpg, .png ou .tiff que contém valores de pixels são imagens do tipo raster. <br>
Elas são divididas em "células" comv alores. <br>
*Bit-depth* se refere ao número de cores de possível representação na imagem. Em geral, as nossas fotos de 8bit, mas para algumas, utilizamos 16-bit. <br>

## Radiância, Reflectância e correções de imagem
Em geral, as imagens são recebidas como *raster* contendo os valores de pixel para cada uma das bandas. Depois, temos o seguinte processamento: <br>
**Número do pixel** --> **Radiancia** --> **Reflectância** <br>
Para análises quantitativas, tais como extração de índices, pode ser necessário aplicar esse processo.
Em resumo,  o que será feito é inferir qual parte do valor contido no pixel refere-se a de fato um raio refletido no objeto desejado, qual parte desviou na atmosfera e acertou nosso sensor. <br>
Cada satélite específico tem uma curva (uma regressão linear, com coeficiente ângular chamado de ganho e coeficiente linear chamado de bias ou offset) que mapeia o valor "cru" do pixel para a reflectância espectral. 

----
## Referências:
[Raster Data - GIS](https://www.youtube.com/watch?v=R64aJfG8RXM) <br>
[Digital Number, Radiance, and Reflectance](https://www.youtube.com/watch?v=sOk5fFPSDBA) <br>
[Radiative transfer and atmospheric correction](https://www.youtube.com/watch?v=qb4yFwzsnU8)
[GDAL: Process and Transform Raster Data (Maptime Salzburg 2018)](https://www.youtube.com/watch?v=6kCXhQ73kgk)
[7a TOA Radiance and TOA Reflectance Bias Gain Landsat Explained](https://www.youtube.com/watch?v=fXx08JQXr7A)

