var landsat = ee.Image('LANDSAT/LC08/C01/T1_TOA/LC08_123032_20140515')
  .select(['B4', 'B3', 'B2'])

var geometry = ee.Geometry.Rectangle([116.2621, 39.8412, 116.4849, 40.01236])

Export.image.toDrive({
  image: landsat,
  description: 'imageToDriveExample',
  scale: 30,
  region: geometry
})

print(landsat)