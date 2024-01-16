# SPAM-China-1km

## Overview
This script generates the distribution of crop production at the provincial level in China from 2010 to 2022. It currently covers 17 types of crops, with plans to expand in the future. The script provides detailed information on crop production distribution based on various irrigation technologies.

## Key Features
- **Historical Data Analysis:** Covers crop distribution data from 2010 to 2022.
- **Multiple Crop Types:** Supports 17 different crop types, with plans to add more.
- **Irrigation Technology Impact:** Analyzes crop production based on different irrigation technologies.

## Methodology

balabala

## Usage Instructions

### Initial Setup
1. **Configuration with `InitialConfig.py`:**
   - This module helps you generate the `config.ini` file.
   - Set up the directory, region, crop type, and target year to get the final `config.ini`.

### Directory Structure
- `excel`: Folder to store Excel files.
- `out`: Output folder for results.
- `shp`: Contains `SPAMChina1km` shapefiles for cliping study area.

### Crop Types and Technologies
The script categorizes crop production based on different technologies:
- `*_A`: All technologies together (complete crop).
- `*_I`: Irrigated portion of the crop.
- `*_H`: Rainfed high inputs portion of the crop.
- `*_L`: Rainfed low inputs portion of the crop.
- `*_S`: Rainfed subsistence portion of the crop.
- `*_R`: Rainfed portion of the crop (equals `A - I`, or `H + L + S`).

