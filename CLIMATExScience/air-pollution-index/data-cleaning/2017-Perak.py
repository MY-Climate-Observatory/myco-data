# -*- coding: utf-8 -*-
"""
26 May 2020
Author: Xiandi Ooi
We will first download the file from the source. 
Then, the data is organized to ease future analysis. Specific changes are as follows:
    1. Datetime variable added;
    2. Numerical API values are extracted;
    3. Dominant pollutant type are extracted
"""

import requests
import pandas as pd

def download_file(url, file_name):
    """
    url: url of the file to be downloaded
    file_name: file name to save the file.
    
    This function takes the given url and download it as the given file name.
    
    Note: the document will be saved to the current working directory, change if required.
    """
    try:
        response = requests.get(url)
    except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  
    except Exception as err:
            print(f"Other error occurred: {err}")  
    else:
        with open(file_name, "wb") as working_file:
            working_file.write(response.content)
        
def clean_data(file_name):
    """
    file_name: file to be cleaned
    
    This function converts the data types in the original dataframe into more suitable type.
    The good news is that the orginal dataframe is already in good shape so there's less to do.   
    """
    
    df_input = pd.read_excel(file_name, skiprows=3)
    
    #Checking the basic information about the dataframe (optional)
    #print(df_input.info()) 
    #print(df_input.describe())

    #Selecting columns
    df_output = df_input.rename(columns = {"DATE/TIME":"Datetime"})
    df_output.drop(df_output.tail(1).index,inplace=True)
    
    #Pivoting the dataframe for its Area and State
    df_final = pd.melt(df_output, id_vars=["Datetime"], 
                        value_vars = ["Sek. Keb. Ayer Puteh, Taiping",
                                      "Sek. Men. Keb. Jalan Tasek, Ipoh",
                                      "Sek. Keb. Jalan Pegoh, Pegoh",
                                      " Pentadbiran Daerah Manjung, Seri Manjung",
                                      "Universiti Perguruan Sultan Idris, Tanjung Malim"],
                        var_name="Station", value_name="API")
    area_directory = {"Sek. Keb. Ayer Puteh, Taiping": ("Kg. Air Putih, Taiping", "Perak"),
                      "Sek. Men. Keb. Jalan Tasek, Ipoh": ("Jalan Tasek, Ipoh", "Perak"),
                      "Sek. Keb. Jalan Pegoh, Pegoh": ("S K Jalan Pegoh, Ipoh", "Perak"),
                      " Pentadbiran Daerah Manjung, Seri Manjung": ("Seri Manjung", "Perak"),
                      "Universiti Perguruan Sultan Idris, Tanjung Malim": ("Tanjung Malim", "Perak")}
    #There are some new stations added, the area are displayed in a similar manner as previous datasets
    df_final["Site"] = df_final["Station"].map(area_directory)
    df_final[["Area", "State"]] = pd.DataFrame(df_final["Site"].tolist(), index= df_final.index)
    
    #Separating each API values into values and its dominant pollutant
    df_final["API"].astype(str)
    df_final["Dominant"] = df_final["API"].str.extract("(\D+)", expand = False)
    df_final["API_Values"] = df_final["API"].str.extract("(\d+)", expand = False)
    df_final["API_Values"] = pd.to_numeric(df_final["API_Values"], errors="coerce").fillna(0).astype(int)
    
    df_final = df_final.drop(columns = ["Station", "Site", "API"])  
    #Checking the basic information about the final dataframe (optional)
    #print(df_final.info())
    
    #Export output to new csv file (edit path and name as needed)
    df_output.to_csv(r"file_path\file_name.csv")
    return df_final
    
def main():
    url = "http://www.data.gov.my/data/ms_MY/dataset/caae1f31-f80d-4952-bd7a-1b8ca4b58ec5/resource/02ccf23f-ea68-4c99-b743-bbd7a293d2e2/download/perak.xlsx"
    file_name = "API_Perak_2017.xlsx"
    download_file(url, file_name)
    clean_data(file_name)

if __name__ == "__main__":
    main()
