import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Add sections and options with values
config["directories"] = {
    # Directory for province shapefiles
    "dir_provshp": "E:/研究生_个人/WRI/SPAM_data",
    
    # Directory for SPAM GeoTIFF files
    "dir_prodtif": "E:/研究生_个人/WRI/SPAM_data/spam2010v2r0_global_prod.geotiff",
    
    # Directory for production Excel files
    "dir_prodxls": "E:/研究生_个人/WRI/SPAM_data",
    
    # Output directory
    "dir_output": "E:/研究生_个人/WRI/SPAM_data/OutPut/",
}

config["regions"] = {
    "province": "云南省"
}

config["crops"] = {
    "crop": "wheat"
}

config["years"] = {
    "target_year": "2020"
}

# Save the configuration to a file
with open("config.ini", "w") as configfile:
    config.write(configfile)
