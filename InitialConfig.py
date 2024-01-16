import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Add sections and options with values
config["directories"] = {
    # Directory for province shapefiles
    "dir_provshp": "./shp/",
    
    # Directory for SPAM GeoTIFF files
    "dir_prodtif": "C:/Users/Yuchen.Guo/OneDrive/WRI/project/RiskImpact/spam2010v2r0_global_prod.geotiff/",
    
    # Directory for production Excel files
    "dir_prodxls": "./excel/",
    
    # Output directory
    "dir_output": "./out/",
}

config["regions"] = {
    "province": "云南省"
}

config["crops"] = {
    "crop": "wheat"
}

config["years"] = {
    "target_year": "2015"
}

# Save the configuration to a file
with open("config.ini", "w") as configfile:
    config.write(configfile)
