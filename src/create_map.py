import ee
import geemap

ee.Initialize()

dataset = ee.ImageCollection('MODIS/061/MOD11A1').filter(ee.Filter.date('2018-01-01', '2018-05-01'))

date = ee.Filter.date('2018-01-01', '2018-05-01')
data_modis = ee.ImageCollection('MODIS/061/MOD11A1').filter(date)

landSurfaceTemperature = data_modis.select('LST_Day_1km')
landSurfaceTemperatureVis = {
  "min": 13000.0,
  "max": 16500.0,
  "palette": [
    '040274', '040281', '0502a3', '0502b8', '0502ce', '0502e6',
    '0602ff', '235cb1', '307ef3', '269db1', '30c8e2', '32d3ef',
    '3be285', '3ff38f', '86e26f', '3ae237', 'b5e22e', 'd6e21f',
    'fff705', 'ffd611', 'ffb613', 'ff8b13', 'ff6e08', 'ff500d',
    'ff0000', 'de0101', 'c21301', 'a71001', '911003'
  ]
}

# image_path = "C:/pale-blue-dot-challenge/src/figures/SurfTemp_map.png"
# image = geemap.ImageOverlay(
#     url=image_path, bounds=((-74.5,-33.5), (-34.5,5.5))
# )

map = geemap.Map(center=[-20, -50], zoom=3.5)
map.add_basemap('HYBRID')
# map.add_layer(data_sent.mean(), visualization, 'RGB')
map.add_layer(landSurfaceTemperature, landSurfaceTemperatureVis,'Land Surface Temperature')
# map.add_layer(image)

map.save("C:/Users/marti/Documents/pbdchallenge-wendy/assets/figures/modis_temp_map.html")