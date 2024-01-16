# SPAM-China-1km

This script help you generate the distribution of the crops' distribution in province level of China from 2010 to 2022. Currently, it will cover 17 types of crops and the crops types will expand in the future. It will give the different types of crop production distriburion based on the Irrigation technology.  

Following are the instruction of script:

'InitialConfig.py' will you help generate the "config.ini", every time you set up the dirctory, region, crop type, target year, you will get the final  
congfig.ini:
folder "excel":
folder "out":
folder "shp":
"SPAMChina1km"

"""
    *_A	all technologies together, ie complete crop
    *_I	irrigated portion of crop
    *_H	rainfed high inputs portion of crop
    *_L	rainfed low inputs portion of crop
    *_S	rainfed subsistence portion of crop
    *_R	rainfed portion of crop (= A - I, or H + L + S)
"""
