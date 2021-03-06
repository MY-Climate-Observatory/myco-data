# Sequence of Order

To reproduce the data cleaning process of this metric, please run the scripts in the following order:

1. These scripts clean the data from their sources separately, and they can be run in any order:
    * 20051001-20150610.py
    * 20150611-20151231.py
    * 20160101-20161231.py 
    * 2017-Johor.py
    * 2017-KL.py
    * 2017-Kedah.py
    * 2017-Kelantan.py
    * 2017-Melaka.py
    * 2017-NS.py
    * 2017-Pahang.py
    * 2017-Perak.py
    * 2017-Perlis.py
    * 2017-Putrajaya.py
    * 2017-Sabah.py
    * 2017-Sarawak.py
    * 2017-Terengganu.py
    * 2018-Johor.py
    * 2018-Melaka.py
    * 2018-NS.py
    * 2018-Pahang.py
    * 2018-Penang.py
    * 2018-Perak.py
    * 2018-Perlis.py
    * 2018-Sabah.py
    * 2018-Sarawak.py
    * 2019-Johor.py
    * 2019-Kedah.py
    * 2019-Kelantan.py
2. data-merge.py
3. version-update-1.py
4. version-update-2.py
5. These scripts clean the data separately, and they can run in any order:
    * 2019-Melaka.py
    * 2019-NS.py
    * 2019-Pahang.py
    * 2019-Penang.py
    * 2019-Perak.py
    * 2019-Perlis.py
    * 2019-Sabah.py
    * 2019-Sarawak.py
    * 2019-Terengganu.py
6. version-update-3.py

Please note that this metric will be updated periodically as the original source release more datasets.

## Original repository

These scripts were originally created [here](https://github.com/XD-Ooi/MY-Climate-Observatory). The scripts are duplicates of the original, and the duplication has the consent of the original author. Updates beyond version-update-2.py are pushed to this repository directly.

