import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Add sections and options with values
config["directories"] = {
    "dir_input": "E:/研究生_个人/WRI/SPAM_data",
    "dir_distribution": "E:/研究生_个人/WRI/SPAM_data/OutPut/History/",
    "dir_output": "E:/研究生_个人/WRI/SPAM_data/OutPut/Tiff/",
    "dir_global": "./spam2010v2r0_global_prod.geotiff"
}

config["regions"] = {
    "province": "辽宁省"
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
