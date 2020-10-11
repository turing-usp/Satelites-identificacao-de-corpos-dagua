sentinel1 = ee.ImageCollection("COPERNICUS/S2_SR")

var start = ee.Date('2018-06-01')
var finish = ee.Date('2018-10-01')

var filteredCollection = sentinel1
  .sort('CLOUD_COVER', true)

print("Qt de imgs filtradas: ", filteredCollection.size())

var imgToExport = ee.Image(filteredCollection.first()).select('B.+')

print(imgToExport)

var geometry = ee.Geometry.Rectangle([116.2621, 39.8412, 116.4849, 40.01236])

Export.image.toDrive({
  image: imgToExport,
  description: 'SP_sentinel2',
  scale: 30,
  region: geometry
})