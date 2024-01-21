import ee
import geemap

ee.Initialize()

# Applies scaling factors fot landsat maps.
def apply_scale_factors(image):
  optical_bands = image.select('SR_B.').multiply(0.0000275).add(-0.2)
  thermal_bands = image.select('ST_B.*').multiply(0.00341802).add(149.0)
  return image.addBands(optical_bands, None, True).addBands(
      thermal_bands, None, True
  )

def create_landsat_image(file_dir, file_name):
    landsat_visualization = {
        'bands': ['SR_B4', 'SR_B3', 'SR_B2'],
        'min': 0.0,
        'max': 0.3,
    }

    #Landsat 8 images
    dataset_ls8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2').filterDate(
        '2021-05-01', '2021-06-01'
    )

    dataset_ls8 = dataset_ls8.map(apply_scale_factors)

    map_ls8 = geemap.Map()
    map_ls8.set_center(-114.2579, 38.9275, 8)
    map_ls8.add_layer(dataset_ls8, landsat_visualization, 'True Color (432)')

    map_ls8.save(f"{file_dir}/{file_name}")

def create_temp_map(file_dir, file_name):
    # ERA5 Monthly Aggregates - Latest Climate Reanalysis Produced by ECMWF / Copernicus Climate Change Service
    dataset_era5 = ee.ImageCollection('ECMWF/ERA5/MONTHLY')

    era5_visualization = {
    'bands': ['mean_2m_air_temperature'],
    'min': 250.0,
    'max': 320.0,
    'palette': [
        '000080', '0000d9', '4000ff', '8000ff', '0080ff', '00ffff',
        '00ff80', '80ff00', 'daff00', 'ffff00', 'fff500', 'ffda00',
        'ffb000', 'ffa400', 'ff4f00', 'ff2500', 'ff0a00', 'ff00ff',
    ]
    }

    map_era5 = geemap.Map()
    map_era5.set_center(22.2, 21.2, 0)
    map_era5.add_layer(dataset_era5, era5_visualization, 'Monthly average air temperature [K] at 2m height')

    map_era5.save(f"{file_dir}/{file_name}")

def create_soil_moisture_map(file_dir, file_name):
    # NASA-USDA Enhanced SMAP Global Soil Moisture Data
    dataset_smap = ee.ImageCollection('NASA_USDA/HSL/SMAP10KM_soil_moisture').filterDate(
        '2017-04-01', '2017-04-30'
    )

    soil_moisture = dataset_smap.select('ssm')
    soil_moisture_vis = {
    'min': 0.0,
    'max': 28.0,
    'palette': ['0300ff', '418504', 'efff07', 'efff07', 'ff0303'],
    }

    map_soil_moisture = geemap.Map()
    map_soil_moisture.set_center(-6.746, 46.529, 2)
    map_soil_moisture.add_layer(soil_moisture, soil_moisture_vis, 'Soil Moisture')

    map_soil_moisture.save(f"{file_dir}/{file_name}")

def create_nvdi_map(file_dir, file_name):
    # MOD13A3.061 Vegetation Indices Monthly L3 Global 1 km SIN Grid
    dataset_nvdi = ee.ImageCollection('MODIS/061/MOD13A3').filterDate(
        '2020-01-01', '2023-05-01'
    )

    ndvi = dataset_nvdi.select('NDVI')

    ndviVis = {
    'min': 0,
    'max': 9000,
    'palette': [
        'ffffff', 'ce7e45', 'df923d', 'f1b555', 'fcd163', '99b718', '74a901',
        '66a000', '529400', '3e8601', '207401', '056201', '004c00', '023b01',
        '012e01', '011d01', '011301'
    ],
    }

    map_nvdi = geemap.Map()
    map_nvdi.set_center(6.746, 46.529, 2)
    map_nvdi.add_layer(ndvi, ndviVis, 'NDVI')

    map_nvdi.save(f"{file_dir}/{file_name}")

file_dir = "C:/pale-blue-dot-challenge/src/figures"

create_landsat_image(file_dir, "landsat_map.html")
create_temp_map(file_dir, "temp_map.html")
create_soil_moisture_map(file_dir, "sm_map.html")
create_nvdi_map(file_dir, "nvdi_map.html")