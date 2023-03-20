import time
import requests
import datetime
import os

url = "https://www.emissionsregistry.admin.ch/crweb/public/auction/dates.action"


def get_emissions_data():
    response = requests.get(url)
    return response.content


def save_data(url_data):
    data_file = os.path.join("auction_data", f"emissions_data_{str(datetime.datetime.now()).replace(':', '_')}.txt")
    with open(data_file, "wb") as f:
        f.write(url_data)


# Run the scraper every minute
while True:
    url_data = get_emissions_data()
    save_data(url_data)
    print(str(datetime.datetime.now()).replace(':', '_'))
    time.sleep(60)
