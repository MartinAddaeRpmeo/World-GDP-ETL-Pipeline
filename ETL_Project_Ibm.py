#!/usr/bin/env python
# coding: utf-8




import pandas as pd 
import logging
import sqlite3
from sqlalchemy import create_engine
from bs4 import BeautifulSoup
import requests
from datetime import datetime, time


db_name = 'World_Economies.db'
table_name = 'Countries_by_GDP'
taget_file="GDP_Data.csv"
log_file="log_file.txt"


def extract():
    try:
        dataframe=pd.DataFrame(columns=["Country", "GDP_USD_millions"])
        url='https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
        html_page=requests.get(url).text
        data=BeautifulSoup(html_page,"html.parser")

        table=data.find_all("tbody")
        rows=table[2].find_all("tr")

        for row in rows:
            col= row.find_all("td")
            if len(col) > 2:
                data_dict={"Country":col[0].text.strip(), "GDP_USD_millions":col[2].text.strip()}
                df=pd.DataFrame(data_dict, index=[0])
                dataframe=pd.concat([dataframe,df],ignore_index=True
                                   )
        print("Data has extracted succesfully")
        return dataframe
    except Exception as e:
        print("Erro:", e)
        return None


def transform(data):
    try:
        data["GDP_USD_millions"]=data["GDP_USD_millions"].str.replace(",","")
        data["GDP_USD_millions"]=pd.to_numeric(data["GDP_USD_millions"], errors="coerce")
        data["GDP_USD_millions"]= round(data["GDP_USD_millions"]/1000,2)
        data=data.rename(columns={"GDP_USD_millions":"GDP_USD_billion"})
        print("data Tranformation Succefull")
        return data
    except Exception as e:
        print("Error:", e)
        return None

def load(data):
    try:
        data.to_csv(taget_file)
        conn=sqlite3.connect("db_name")
        data.to_sql(table_name, conn, if_exists="replace", index=False)
        print("data has succefully Loaded in database")
    except Exception as e:
        print("Error:", e)


def query():
    try:
        conn=sqlite3.connect("db_name")
        query=("""select * from Countries_by_GDP 
        where GDP_USD_billion > 100 
        order by 2 desc;""")
        df1=pd.read_sql(query,conn)
        print(df1)
    except Exception as e:
        print("Error:",e)


def logging(message):
    try:
        
        time_format="%Y-%m-%d-%H:%M:%S"
        time=datetime.now()
        timestamp=time.strftime(time_format)
        with open (log_file,"a") as f:
            
            f.write(timestamp +','+ message + "\n")
    except Exception as e:
        print("Error:", e)
        
    
if __name__ == "__main__":

    logging("Etl Process Starting")
    logging("Extraction of Data")
    data=extract()

    logging("Data Transformation")
    data=transform(data)

    logging("Loading of data")
    if data is not None and data.empty:

        load(data)

    logging("Data querying for countries with GDP over 100Billion")
    













