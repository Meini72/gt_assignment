import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Get data from API
response = requests.get("https://api.covid19api.com/total/dayone/country/singapore")
data = response.json()

# Extract date and number of cases from the data
dates = []
cases = []
for item in data:
    dates.append(item['Date'])
    cases.append(item['Confirmed'])

# Convert date string to datetime object
dates = [mdates.datestr2num(date) for date in dates]

# Create a graph
fig, ax = plt.subplots()
ax.plot_date(dates, cases, fmt="-")
ax.set_title("Number of COVID-19 Cases in Singapore")
ax.set_xlabel("Date")
ax.set_ylabel("Number of Cases")
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%Y"))
plt.xticks(rotation=45)
plt.show()
