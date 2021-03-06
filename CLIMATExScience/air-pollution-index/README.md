# Air Pollution Index 

**Indeks Pencemaran Udara**

The Air Pollution Index (API) indicates the air quality status of a particular area. Normally, the indicator is calculated based on the average concentration of 6 air pollutant parameters: sulphur dioxide, nitrogen dioxide, carbon monoxide, ozone, PM2.5, and PM10. Each is measured at different period as they have different human-acceptable exposure periods. The air pollutant with the highest average concentration over a period of time will determine the API value. The API calculation in Malaysia is based on Pollution Standard Index (PSI) that is recognized internationally. 

For more details on the calculation of Malaysia's API, check this out: [AIR POLLUTANT INDEX (API) CALCULATION](http://apims.doe.gov.my/public_v2/pdf/API_Calculation.pdf)

The organized csv file of all the available API data can be downloaded [here](https://www.dropbox.com/s/rg0h0b8ez5p2fk8/api-20200713.csv?dl=0). This csv contains Malaysia's API data from 2005 - 2019 in all 14 states & territories (based on availability of data). Please note that the delimiter for this dataset is ";". For those who would like to get their hands dirty on some data analysis, feel free to use this dataset!

## Data Format

| Variable Name | Variable Type | Description | Unit | Example |
| :-----------: | :-----------: | :---------: | :--: | :-----: |
| Primary Key | `integer` | ID of each entry | None | `"12311"`|
| State | `string` | State/federal territories of Malaysia | None | `"Wilayah Persekutuan"`|
| Area | `string` | Unique location of the data collection site | None | `"Labuan"` |
| Dominant | `string` | Special character denoting the 24 hr running average most dominant pollutant character | None | `"**"` | 
| API_Values | `float` | Recorded value of the most dominant pollutant character | API | `"35.3"` |
| Datetime | `DateTime` | Date and time of the recorded value | Year, Month, Day, Hour, Minute | `"01-10-05 17:00"` |

## Other Useful Details of the Dataset

| Character | Type of Dominant Pollutant | 
| :--------------------------: | :---------------: |
| ** | Particulate matter with diameter of less than 2.5 micron (PM2.5) / μg/m3 |
| * | Particulate matter with diameter of less than 10 micron (PM10) / μg/m3 |
| a | Sulphur Dioxide (SO2) / ppm | 
| b | Nitrogen Dioxide (NO2) / ppm | 
| c | Ozone (O3) / ppm | 
| d | Carbon Monoxide (CO) / ppm |
| & | More than one pollutant | 
| others | No clarification by the official data releasing insitutions so please be wary |

API reflects its effect on human health ranging from good to hazardous. It can be categorized according to the action criteria as stipulated in the National Haze Action Plan. 
| API | Status |
| :--: | :----: |
| 0 - 50 | Good |
| 51 - 100 | Moderate |
| 101 - 200 | Unhealthy |
| 201 - 300 | Very Unhealthy |
| > 300 | Hazardous | 

Currently, the API publishing is under the portfolio of the DOE. They made a real-time [Malaysia API tracker](http://apims.doe.gov.my/public_v2/home.html) that 
allows you to track hourly API data across Malaysia for the past 7 days. However, 7 days of data is definitely not enough if, for example, you are interested in 
understanding the overall trend of Malaysia's air quality over the past 10 years. 

## Meta Data

### Purpose 

API are used as the ambient air quality measurement in Malaysia. The actual concentration of air pollutants are not published so this is the current available data for us to assess the air quality of Malaysia.

### Time period of creation

This dataset is cleaned and organized from March 2020 - June 2020.

### Contributor

@XD-Ooi

### Data Source
Releasing entities: Malaysia's Ministry of Water, Land and Natural Resources (KATS), and Department of Environment (DOE) 

Accessed on: [data.gov.my](http://www.data.gov.my/). 

The original links of the datasets are as listed below (we tried to keep the title as close to the original as possible):
* [Malaysia API 2005 - 2013](http://www.data.gov.my/data/ms_MY/dataset/bacaan-indeks-pencemaran-udara-ipu-di-malaysia-pada-tahun-2005-hingga-2013)
* [Malaysia API 2013 - 2014](http://www.data.gov.my/data/ms_MY/dataset/bacaan-indeks-pencemaran-udara-ipu-di-malaysia-pada-tahun-2013-hingga-2014)
* [Malaysia API 2014 - 2015](http://www.data.gov.my/data/ms_MY/dataset/bacaan-indeks-pencemaran-udara-ipu-di-malaysia-pada-tahun-2014-hingga-2015)
* [Malaysia API 2015](http://www.data.gov.my/data/ms_MY/dataset/jas-bacaan-indeks-pencemaran-udara-ipu-di-malaysia-pada-tahun-2015)
* [Malaysia API 2016](http://www.data.gov.my/data/ms_MY/dataset/bacaan-indeks-pencemaran-udara-ipu-2016)
* [Malaysia API 2017](http://www.data.gov.my/data/ms_MY/dataset/bacaan-indeks-pencemar-udara-ipu-bagi-semua-stesen-pengawasan-kualiti-udara-automatik-dalam-malaysia)
* [2017 Hourly API for Kuala Lumpur](http://www.data.gov.my/data/ms_MY/dataset/bacaan-indeks-pencemar-udara-ipu-kuala-lumpur-bagi-tahun-2017)
* [2017 Hourly API for Putrajaya](http://www.data.gov.my/data/ms_MY/dataset/bacaan-indeks-pencemar-udara-ipu-putrajaya-bagi-tahun-2017)
* [2017, 2018, 2019 Hourly API for Johor](http://www.data.gov.my/data/ms_MY/dataset/bacaan-indeks-pencemar-udara-negeri-johor)
* [2017, 2018, 2019 Hourly API for Kedah](http://www.data.gov.my/data/ms_MY/dataset/bacaan-indeks-pencemar-udara-ipu-negeri-kedah-bagi-tahun-2017)
* [2017, 2018, 2019 Hourly API for Kelantan](http://www.data.gov.my/data/ms_MY/dataset/bacaan-indeks-pencemar-udara-ipu-negeri-kelantan-bagi-tahun-2017)
* [2017, 2018, 2019 Hourly API for Melaka](http://www.data.gov.my/data/ms_MY/dataset/bacaan-indeks-pencemar-udara-ipu-negeri-melaka-bagi-tahun-2017)
* [2017, 2018, 2019 Hourly API for Negeri Sembilan](http://www.data.gov.my/data/ms_MY/dataset/bacaan-indeks-pencemar-udara-ipu-negeri-sembilan-bagi-tahun-2017)
* [2017, 2018, 2019 Hourly API for Pahang](http://www.data.gov.my/data/ms_MY/dataset/bacaan-indeks-pencemar-udara-ipu-negeri-pahang-bagi-tahun-2017)
* [2017, 2018, 2019 Hourly API for Perak](http://www.data.gov.my/data/ms_MY/dataset/bacaan-indeks-pencemar-udara-ipu-negeri-perak-bagi-tahun-2017)
* [2017, 2018, 2019 Hourly API for Perlis](http://www.data.gov.my/data/ms_MY/dataset/bacaan-indeks-pencemar-udara-ipu-negeri-perlis-bagi-tahun-2017)
* [2017, 2018, 2019 Hourly API for Pulau Pinang](http://www.data.gov.my/data/ms_MY/dataset/bacaan-indeks-pencemar-udara-ipu-negeri-pulau-pinang-bagi-tahun-2017)
* [2017, 2018, 2019 Hourly API for Sabah](http://www.data.gov.my/data/ms_MY/dataset/bacaan-indeks-pencemar-udara-ipu-negeri-sabah-bagi-tahun-2017)
* [2017, 2018, 2019 Hourly API for Sarawak](http://www.data.gov.my/data/ms_MY/dataset/bacaan-indeks-pencemar-udara-ipu-negeri-sarawak-bagi-tahun-2017)
* [2017, 2018, 2019 Hourly API for Terengganu](http://www.data.gov.my/data/ms_MY/dataset/bacaan-indeks-pencemar-udara-ipu-negeri-terengganu-bagi-tahun-2017)

## Terms of Use

Data and information are subject to the Malaysian Government Open Data Terms of Use 1.0. Find out more at <http://www.data.gov.my/page/termsofuse>.

## File size

108 MB

## Data Organizing Process

1. Data downloaded from original linked and cleaned separately. Scripts for the data cleaning process of each dataframe can be found in the `data-cleaning` folder.
2. Merge and combine all dataframes. Scripts also in the `data-cleaning` folder.
3. Data output in the form of a `.csv` file, with ";" as the delimiter.
4. Scripts for visualizations of the dashboards as included in the `data-visualization` folder.
