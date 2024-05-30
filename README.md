# Google Fit Data Heatmap

This repository contains a Python script to generate a heatmap from Google Fit data exported in `.tcx` format.

The script parses the `.tcx` files for geolocation data (latitude and longitude) and creates an interactive heatmap using `folium`.

## Requirements

- Python 3.6 or later
- `pandas`
- `folium`

You can install the required packages using pip:

```
pip install pandas folium
```

## Usage

Export Google Fit Data:

- Request your Google Fit data from Google Takeout.

- Extract the downloaded archive to a directory.

Run the Script:

- Navigate to the directory where you extracted your Google Fit data.

- Run the script with the path to the Activities directory as an argument.

```
python script.py <path_to_activities_dir>

# for example:
python script.py Takeout/Fit/Activities
```

The script will parse the `.tcx` files in the specified directory and generate a heatmap saved as `heatmap.html` in the current directory.

## Example output

After running the script, open `heatmap.html` in a web browser to view the interactive heatmap.
