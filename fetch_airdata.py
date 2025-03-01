import requests
import csv
import os
from datetime import datetime

# Read more from
# https://aqicn.org/api/
# https://aqicn.org/data-platform/register/
# https://aqicn.org/historical/#city:bangkok

# Replace with your API key
# Retrieve API key from environment variable
API_KEY = os.getenv("AQICN_API_KEY")

# List of cities
cities = ["Bangkok", "Beijing", "Los Angeles"]

# CSV File Name
CSV_FILE = "air_data.csv"

def fetch_pm25_data(city):
    """
    Fetch PM2.5 data for a given city from the AQICN API.
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
    Save the fetched data to a CSV file.
    """
    file_exists = os.path.isfile(filename)

    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Write header if file is newly created
        if not file_exists:
            writer.writerow(["Timestamp", "City", "AQI", "PM2.5", "JSON"])

        writer.writerow(data)

if __name__ == "__main__":
    for city in cities:
        pm25_data = fetch_pm25_data(city)
        aqi = pm25_data.get("aqi", "N/A")
        pm25 = pm25_data.get("iaqi", {}).get("pm25", {}).get("v", "N/A")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if pm25_data:
            save_to_csv([timestamp, city, aqi, pm25, pm25_data], CSV_FILE)
            print(f"Data saved for {city}: {pm25_data}")
