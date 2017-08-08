import urllib.request, json
import csv
import datetime, calendar, time
#import pymysql

#conn = pymysql.connect(
#        db='commuting',
#        user='root',
#        passwd='gooses',
#        host='localhost')
#c = conn.cursor()

url = "https://maps.googleapis.com/maps/api/directions/json?origin=place_id:%s&destination=place_id:%s&key=%s&arrival_time=%s"
url2 = "https://maps.googleapis.com/maps/api/directions/json?origin=place_id:%s&destination=place_id:%s&mode=transit&key=%s&arrival_time=%s"

towns = [("Old Greenwich", "ChIJbWgW47aYwokRS_-QioWnp9k"),
("Greenwich","ChIJly5MDxGYwokR4jAEYCeuMQg"),
("Darien", "ChIJC6TcEIegwokReGrCDJwO5Sw"),
("NC","ChIJESxVNa-nwokRz27KMKkYEfg"),
("Rye", "ChIJyVCxxcqQwokR6GnPGTOEaxM")]
TwoSigma = "ChIJpf-x64pZwokRYr9BwWaVP9k"

API_Key = "AIzaSyCFgqXKCJF4OS7kqmjiZcECFTX0VM_pK4Y"


dur  = []
output = []
train = []
urls = []
arrival = 1502197200

for (city, locate) in towns:
    req = url % (locate, TwoSigma, API_Key, arrival)
    req2 = url2 % (locate, TwoSigma, API_Key, arrival)
    train = json.loads(urllib.request.urlopen(req2) .read())
    drive = json.loads(urllib.request.urlopen(req) .read())
    dur.append([city, "Drive: " + drive['routes'][0]['legs'][0]['duration']['text'], "Train: " + train['routes'][0]['legs'][0]['duration']['text'], "Leave by: " + train['routes'][0]['legs'][0]['departure_time']['text'], "Time: " + str(datetime.datetime.now())])
#    c.execute("INSERT INTO times VALUES (dur)")

print(dur)


#with open("commute.csv", "a") as f:
#    writer = csv.writer(f)
#    writer.writerows(times)
