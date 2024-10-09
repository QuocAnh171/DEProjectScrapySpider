import requests
from bs4 import BeautifulSoup
import re
from datetime import date, timedelta
import json

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def crawl_data(date_time: str):
    headers = {}
    x = requests.get(f'https://www.minhngoc.com.vn/ket-qua-xo-so/mien-bac/{date_time}.html', headers=headers)

    soup = BeautifulSoup(x.content, 'html.parser')
    content = soup.find("div", attrs={"class": "box_kqxs"})
    rows = list()
    for row in content.findAll("tr"):
        rows.append(row)

    rowkqxsdt = rows[0]

    list_search = {"db", '1', '2', '3', '4', '5', '6', '7'}
    list_result = list()
    priceItem = {}
    listPriceValue = []

    for i in list_search:
        namePrice = 'giai'
        result = rowkqxsdt.find("td", attrs={"class": namePrice + i})

        # Regex để tìm tất cả các số trong thẻ <div>
        pattern = r'<div>(\d+)</div>'

        # Tìm tất cả các số trong thẻ <div>
        numbers = re.findall(pattern, str(result))

        # In ra kết quả dưới dạng list
        for num in numbers:
            if str(num)[-2:] not in listPriceValue:
                listPriceValue.append(str(num)[-2:])

    listPriceValue.sort()
    priceItem[date_time] = result = ','.join(map(str, listPriceValue))
    list_result.append(priceItem)

    return list_result

def main_request():
    start_date = date(2024, 9, 1)
    end_date = date(2024, 9, 10)
    for single_date in daterange(start_date, end_date):
        a = single_date.strftime("%d-%m-%Y")
        print(a)
        print(crawl_data(a))

def load_data_to_db_using_insert_value(connection, table_name, data_field, list_data):
    # step 1: check table_name exists
    # step 2: data cleaning, checking
    # step 3: insert data to table
    # step 4: close connection
    pass


def load_data_to_db_using_json_file(connection, table_name, data_field, list_data):
    # step 1: check table_name exists
    # step 2: data cleaning, checking
    # step 3: insert data to table
    # step 4: close connection
    
    with connection.cursor() as cur:

        #TODO using file_path to insert data
        with open('file_path.json') as my_file:
            data = json.load(my_file)

            #TODO execute create table
            cur.execute(""" create table if not exists json_table(
                p_id integer, first_name text, last_name text, p_attribute jsonb,
                quote_content text) """)
            
            #TODO execute insert data to table from json file
            query_sql = """ insert into json_table
                select * from json_populate_recordset(NULL::json_table, %s) """
            cur.execute(query_sql, (json.dumps(data),))