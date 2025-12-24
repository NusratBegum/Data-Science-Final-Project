"""
Air Quality Data Fetcher

This module fetches real-time air quality data from the AQICN (Air Quality Index China) API
and stores it in a CSV file for analysis. It collects AQI and PM2.5 data for multiple cities.

Author: Group 3 - Data Science Final Project
Date: 2025
Course: Data Science Essentials

API Documentation:
    - API Reference: https://aqicn.org/api/
    - Data Platform: https://aqicn.org/data-platform/register/
    - Historical Data: https://aqicn.org/historical/#city:bangkok

Requirements:
    - requests: HTTP library for API calls
    - csv: CSV file handling
    - os: Environment variable access
    - datetime: Timestamp generation

Environment Variables:
    AQICN_API_KEY: Your API key from AQICN data platform

Usage:
    Set the API key as an environment variable:
        export AQICN_API_KEY="your_api_key_here"
    
    Run the script:
        python fetch_airdata.py
    
    The script will fetch data for all cities in the 'cities' list and append
    it to 'air_data.csv' with a timestamp.

Example:
    $ export AQICN_API_KEY="demo_key"
    $ python fetch_airdata.py
    Data saved for Bangkok: AQI=67, PM2.5=67
    Data saved for Beijing: AQI=42, PM2.5=42
    Data saved for Los Angeles: AQI=33, PM2.5=30
"""

import requests
import csv
import os
from datetime import datetime

# Retrieve API key from environment variable
# Register at https://aqicn.org/data-platform/register/ to get your API key
API_KEY = os.getenv("AQICN_API_KEY")

# List of cities to monitor
# Cities can be added or removed based on research needs
cities = ["Bangkok", "Beijing", "Los Angeles"]

# CSV file name for storing collected data
CSV_FILE = "air_data.csv"

def fetch_pm25_data(city):
    """
    Fetch air quality data for a given city from the AQICN API.
    
    This function makes an HTTP GET request to the AQICN API to retrieve
    real-time air quality information including AQI, PM2.5, and other
    pollutant measurements for the specified city.
    
    Args:
        city (str): Name of the city to fetch data for (e.g., "Bangkok", "Beijing")
    
    Returns:
        dict or None: A dictionary containing the air quality data if successful,
                     including:
                     - 'aqi': Air Quality Index value
                     - 'iaqi': Individual air quality indices for various pollutants
                     - 'time': Timestamp of the measurement
                     - 'city': City information (name, geo coordinates)
                     - 'forecast': Forecasted air quality data
                     Returns None if the request fails or data is unavailable.
    
    Raises:
        Exception: Prints error message if API request fails
    
    Example:
        >>> data = fetch_pm25_data("Bangkok")
        >>> if data:
        ...     print(f"AQI: {data['aqi']}")
        ...     print(f"PM2.5: {data['iaqi']['pm25']['v']}")
    """
    api_url = f"https://api.waqi.info/feed/{city}/?token={API_KEY}"
    try:
        response = requests.get(api_url)
        data = response.json()
        
        if data["status"] == "ok":
            return data["data"]
        else:
            print(f"Error fetching data for {city}: {data['data']}")
            return None

    except Exception as e:
        print(f"Failed to retrieve data for {city}: {e}")
        return None

def save_to_csv(data, filename):
    """
    Save the fetched air quality data to a CSV file.
    
    This function appends a new row of data to the CSV file. If the file
    doesn't exist, it creates a new file with appropriate headers.
    
    Args:
        data (list): A list containing the data row to be saved with elements:
                    [timestamp, city, aqi, pm25, json_data]
        filename (str): Path to the CSV file where data should be saved
    
    File Structure:
        The CSV file contains the following columns:
        - Timestamp: Date and time when data was collected (YYYY-MM-DD HH:MM:SS)
        - City: Name of the city
        - AQI: Air Quality Index value
        - PM2.5: PM2.5 concentration (µg/m³)
        - JSON: Complete JSON response from the API for detailed analysis
    
    Example:
        >>> timestamp = "2025-03-17 08:00:00"
        >>> data = [timestamp, "Bangkok", 67, 67, {...}]
        >>> save_to_csv(data, "air_data.csv")
    """
    file_exists = os.path.isfile(filename)

    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Write header if file is newly created
        if not file_exists:
            writer.writerow(["Timestamp", "City", "AQI", "PM2.5", "JSON"])

        writer.writerow(data)

if __name__ == "__main__":
    """
    Main execution block.
    
    Iterates through all cities in the 'cities' list, fetches their air quality
    data, and saves it to the CSV file with a timestamp. Prints confirmation
    messages for each city processed.
    
    This script is designed to be run periodically (e.g., via cron job) to
    collect time-series air quality data for research and analysis.
    """
    for city in cities:
        pm25_data = fetch_pm25_data(city)
        aqi = pm25_data.get("aqi", "N/A")
        pm25 = pm25_data.get("iaqi", {}).get("pm25", {}).get("v", "N/A")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if pm25_data:
            save_to_csv([timestamp, city, aqi, pm25, pm25_data], CSV_FILE)
            print(f"Data saved for {city}: AQI={aqi}, PM2.5={pm25}")
