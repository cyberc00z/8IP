# need api key from 'https://ip-geolocation.whoisxmlapi.com/'

from simple_geoip import   GeoIP, geoip

if __name__ == "__main__":
    IP = "127.0.0.1"
    geoip = GeoIP("at_5Hu01r2V5jKlck1HVJJyuZFY0OB3S")
    data = geoip.lookup(IP)
    print(data)