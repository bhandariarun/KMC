from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import sqlite3
import csv


conn = sqlite3.connect('world_meter.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS covid_data (
                    Name TEXT,
                    Total_Cases VARCHAR,
                    New_Cases VARCHAR,
                    Total_Deaths VARCHAR,
                    New_Deaths VARCHAR,
                    Total_Recovered VARCHAR,
                    New_Recovered VARCHAR,
                    Active_Cases VARCHAR,
                    Serious_Cases VARCHAR,
                    Total_Tests VARCHAR,
                    Population VARCHAR
                    )''')
conn.commit()

url = 'https://www.worldometers.info/coronavirus/'
x = requests.get(url)
print(x)

soup = BeautifulSoup(x.content, 'html.parser')
y = soup.find('table', id='main_table_countries_today')
z = soup.find('tbody').find_all('tr')
column_names = [
    'id',
    "Names",
    "Total_Cases",
    "New_Cases",
    "Total_Deaths",
    "New_Deaths",
    "Total_Recovered",
    "New_Recovered",
    "Active_Cases",
    "Serious_Cases",
    "Top_Cases",
    "Death",
    "Total_Tests",
    "Test",
    "Population"
]
complete_data = []
for i in range(8, len(z)):
    data = []
    list_data = z[i].find_all('td')
    for i in list_data:
        data.append(i.text.strip())
    complete_data.append(data)

# complete_data = []
# for i in range(len(z)):
#     data = []
#     list_data = z[i].find_all('td')
#     for item in list_data:
#         # Remove any leading/trailing whitespace and newlines
#         data.append(item.text.strip())
#     complete_data.append(data)

# print(y.text)
# headers=[i for i in column_names]
# data=[j for j in complete_data]
# output_data = [headers]
# print(output_data)
# print(data)
output_data = [column_names]
output_data.extend(complete_data )

# for i in range(0, len(data), len(headers)):
#         row = data[i:i + len(headers)]
#         output_data.append(row)
output_data_filtered = [[row[i] for i in range(len(row)) if i != 0 and i != 10 and i != 11 and i !=13][:11] for row in output_data]
for row in output_data_filtered:
    print(row)
    c.execute('''INSERT INTO covid_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', row[:11])
    conn.commit()

df=pd.DataFrame(output_data_filtered)
csv_file_path = 'data.csv'
#
# # Write to CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(output_data_filtered)
print(f'Data has been saved to {csv_file_path}')
df.to_csv("data.csv", index=False)

# c.execute("INSERT INTO output_data_filtered (Names, Total_Cases, New_Cases, Total_Deaths, New_Deaths, Total_Recovered, New_Recovered, Active_Cases, Serious_Cases, Total_tests, Population) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")
# conn.commit()
conn.close()

# , (Names, Total_Cases, New_Cases, Total_Deaths, New_Deaths, Total_Recovered, New_Recovered, Active_Cases, Serious_Cases, Total_tests, Population)

# z = soup.find('tbody').find_all('tr')
# print(z)