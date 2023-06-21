import requests
from datetime import datetime

# Function to fetch air quality data from OpenAQ API
def get_air_quality_data(location, parameter, date):
    url = f"https://api.openaq.org/v1/measurements?location={location}&parameter={parameter}&date_from={date}&limit=10000"
    response = requests.get(url)
    data = response.json()
    return data['results']

# Function to analyze air quality data
def analyze_air_quality(data):
    # Perform analysis on the retrieved data
    # Add your analysis logic here based on your specific requirements

    # Example analysis: Calculate the average value of a specific parameter
    values = [measurement['value'] for measurement in data]
    average_value = sum(values) / len(values)
    return average_value

# Example usage
location = "country:US"  # Specify the location (country code) or use "city:CityName" for specific cities
parameter = "pm25"      # Specify the air quality parameter of interest (e.g., "pm25" for particulate matter 2.5)
date = "2023-06-01"    # Specify the date of interest (in YYYY-MM-DD format)

# Fetch air quality data from OpenAQ API
air_quality_data = get_air_quality_data(location, parameter, date)

# Analyze the air quality data
average_value = analyze_air_quality(air_quality_data)

# Output the result
print(f"The average {parameter} value on {date} in {location} was: {average_value}")

