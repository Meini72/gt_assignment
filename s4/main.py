import requests
import csv

url = "https://api.covid19api.com/country/singapore/status/confirmed"

response = requests.get(url)

data = response.json()

with open('covid_data_singapore.csv', 'w', newline='') as csvfile:
    fieldnames = ['Date', 'Cases']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow({'Date': row['Date'], 'Cases': row['Cases']})