import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import folium
import pandas as pd
from folium.plugins import HeatMap


def parse_tcx_files(path):
    coordinates_data = []

    for tcx_file in path.glob("*.tcx"):
        tree = ET.parse(tcx_file)
        root = tree.getroot()

        # Define the namespaces based on the provided XML structure
        ns = {"ns1": "http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2"}

        for trackpoint in root.findall(".//ns1:Trackpoint", namespaces=ns):
            time_elem = trackpoint.find("ns1:Time", namespaces=ns)
            if time_elem is not None:
                position = trackpoint.find("ns1:Position", namespaces=ns)
                if position is not None:
                    lat_elem = position.find("ns1:LatitudeDegrees", namespaces=ns)
                    lon_elem = position.find("ns1:LongitudeDegrees", namespaces=ns)
                    if lat_elem is not None and lon_elem is not None:
                        lat = float(lat_elem.text)
                        lon = float(lon_elem.text)
                        coordinates_data.append((lat, lon))

    return coordinates_data


def create_heatmap(coordinates_data, output_file="heatmap.html"):
    coordinates_df = pd.DataFrame(coordinates_data, columns=["Latitude", "Longitude"])

    heatmap = folium.Map()

    heat_data = [
        [row["Latitude"], row["Longitude"]] for index, row in coordinates_df.iterrows()
    ]

    if heat_data:
        HeatMap(heat_data).add_to(heatmap)

    heatmap.save(output_file)
    print(f"Heatmap saved to {output_file}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_activities_dir>")
        sys.exit(1)

    activities_path = Path(sys.argv[1])

    if not activities_path.is_dir():
        print(f"The provided path {activities_path} is not a valid directory.")
        sys.exit(1)

    coordinates_data = parse_tcx_files(activities_path)
    if not coordinates_data:
        print("No coordinates data to plot.")
        sys.exit(1)

    print(f"Extracted {len(coordinates_data)} coordinates")
    create_heatmap(coordinates_data)
