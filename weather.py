import requests

def getTemperature(location="Irvine"):
    r = requests.get(f"https://api.tomorrow.io/v4/weather/realtime?location={location}&apikey=nGzr5m5xojxxYiJ4sAMpoGP3tQh641Sj")
    response = r.json()

    # print(response['data']['values']['temperature'])
    # return response['data']['values']['temperature']
    return 40

