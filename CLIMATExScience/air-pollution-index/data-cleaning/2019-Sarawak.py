# -*- coding: utf-8 -*-
"""
9 July 2020
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
    
    df_input = pd.read_excel(file_name, skiprows=2)
    
    #Checking the basic information about the dataframe (optional)
    #print(df_input.info()) 
    #print(df_input.describe())
    
    #Selecting columns
    df_output = df_input.rename(columns = {"DATE/TIME":"Datetime"})
    df_output = df_output.iloc[:,1:]
    df_output.drop(df_output.tail(1).index,inplace=True)
    
    #Pivoting the dataframe for its Area and State
    df_final = pd.melt(df_output, id_vars=["Datetime"], 
                        value_vars = ["Limbang, SARAWAK",
                                      "ILP Miri, SARAWAK",
                                      "Miri, SARAWAK",
                                      "Samalaju, SARAWAK",
                                      "Bintulu, SARAWAK",
                                      "Mukah, SARAWAK",
                                      "Kapit, SARAWAK",
                                      "Sibu, SARAWAK",
                                      "Sarikei, SARAWAK",
                                      "Sri Aman, SARAWAK",
                                      "Samarahan, SARAWAK",
                                      "Kuching, SARAWAK"],
                        var_name="Station", value_name="API")
    temp = df_final["Station"].str.split(", ", n = 1, expand = True) 
    df_final["Area"] = temp[0] 
    df_final["State"] = temp[1].str.capitalize() 
    
    #Separating each API values into values and its dominant pollutant
    df_final["API"] = df_final["API"].astype(str)
    df_final["Dominant"] = df_final["API"].str.extract("(\D+)", expand = False)
    df_final["API_Values"] = df_final["API"].str.extract("(\d+)", expand = False)
    df_final["API_Values"] = pd.to_numeric(df_final["API_Values"], errors="coerce").fillna(0).astype(int)
    
    df_final = df_final.drop(columns = ["Station", "API"])  
    #Checking the basic information about the final dataframe (optional)
    #print(df_final.info())
    
    #Export output to new csv file (edit path and name as needed)
    df_output.to_csv(r"file_path\file_name.csv")
    return df_final
    
def main():
    url = "http://www.data.gov.my/data/ms_MY/dataset/72e4b1de-4eb4-4ee7-9d8a-8c8e78192a41/resource/4f75c42f-4ea0-4837-986f-8c1857157b19/download/sarawak.xlsx"
    file_name = "API_Sarawak_2019.xlsx"
    download_file(url, file_name)
    clean_data(file_name)

if __name__ == "__main__":
    main()
