from flask import Flask, request, jsonify
import ee

app = Flask(__name__)

# Initialize the Earth Engine API
ee.Initialize()
ee.Authenticate()

@app.route('/air_quality', methods=['POST'])
def air_quality():
    # Get user input from the request
    data = request.json
    location = data.get('location')  # Expecting a dictionary with 'lat' and 'lon'
    start_date = data.get('start_date')
    end_date = data.get('end_date')

    # Call the function to get air quality data
    result = get_air_quality_data(location, start_date, end_date)
    return jsonify(result)

def get_air_quality_data(location, start_date, end_date):
    # Define the geometry based on user input
    point = ee.Geometry.Point(location['lon'], location['lat'])

    # Load the air quality dataset (e.g., MODIS, Sentinel, etc.)
    dataset = ee.ImageCollection('COPERNICUS/S5P/OFFL/L3_NO2') \
        .filterDate(start_date, end_date) \
        .filterBounds(point)

    # Calculate mean air quality over the specified period
    mean_image = dataset.mean()

    # Get the air quality data as a dictionary
    air_quality_data = mean_image.reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=point,
        scale=1000
    ).getInfo()

    return air_quality_data

if __name__ == '__main__':
    app.run(debug=True)