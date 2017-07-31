import urllib.request, json
url = "https://maps.googleapis.com/maps/api/directions/json?origin=place_id:%s&destination=place_id:%s&key=%s"
url2 = url + "&mode=transit"

towns = [("Old Greenwich", "ChIJbWgW47aYwokRS_-QioWnp9k"),
("Greenwich","ChIJly5MDxGYwokR4jAEYCeuMQg"),
("Darien", "ChIJC6TcEIegwokReGrCDJwO5Sw"),
("NC","ChIJESxVNa-nwokRz27KMKkYEfg"),
("Rye", "ChIJyVCxxcqQwokR6GnPGTOEaxM"),
("Round Hill", "ChIJgd5ICP6XwokRjOFdp-nyXn0")]
TwoSigma = "ChIJpf-x64pZwokRYr9BwWaVP9k"

API_Key = "AIzaSyCFgqXKCJF4OS7kqmjiZcECFTX0VM_pK4Y"

times = []
output = []
urls = []
for (city, locate) in towns:
    req = url % (locate, TwoSigma, API_Key)
    drive = json.loads(urllib.request.urlopen(req) .read())
    times.append([city, "Drive: " + drive['routes'][0]['legs'][0]['duration']['text']])
print(times)
