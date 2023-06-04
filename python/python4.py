import requests
import csv
from datetime import datetime

def download_and_convert_to_csv(url):
    # Download data from the provided link
    response = requests.get(url)
    data = response.json()

    # Convert data to proper structure
    formatted_data = []
    for entry in data:
        year = entry.get("year", "")
        if year:
            year = datetime.strptime(year, "%Y-%m-%dT%H:%M:%S.%f")
        
        formatted_data.append([
            entry.get("name", ""),
            entry.get("id", ""),
            entry.get("nametype", ""),
            entry.get("recclass", ""),
            entry.get("mass", ""),
            year,
            entry.get("reclat", ""),
            entry.get("reclong", "")
        ])

    # Create and write data to a CSV file
    csv_filename = "meteorite_data_m.csv"
    with open(csv_filename, "w", newline="", encoding="utf-8-sig") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Name of Earth Meteorite", "ID of Earth Meteorite", "Name Type", "Rec Class", "Mass (g)", "Year", "Latitude", "Longitude"])
        writer.writerows(formatted_data)

    return csv_filename

# Provide the URL for the data
url = "https://data.nasa.gov/resource/y77d-th95.json"

# Call the function to download, convert, and export the data
csv_file = download_and_convert_to_csv(url)
print(f"Data downloaded and exported to {csv_file}.")
