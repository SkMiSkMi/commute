import urllib.request, json
url = "https://maps.googleapis.com/maps/api/directions/json?origin=place_id:%s&destination=place_id:%s&key=%s"

OldGC = "ChIJbWgW47aYwokRS_-QioWnp9k"
GC = "ChIJly5MDxGYwokR4jAEYCeuMQg"
Darien = "ChIJC6TcEIegwokReGrCDJwO5Sw"
NC = "ChIJESxVNa-nwokRz27KMKkYEfg"
Rye = "ChIJyVCxxcqQwokR6GnPGTOEaxM"
RHC = "ChIJgd5ICP6XwokRjOFdp-nyXn0"
TwoSigma = "ChIJpf-x64pZwokRYr9BwWaVP9k"

API_Key = "AIzaSyCFgqXKCJF4OS7kqmjiZcECFTX0VM_pK4Y"

req = url % (GC, TwoSigma, API_Key)
print(req)
with urllib.request.urlopen(req) as url:
    data = json.loads(url.read().decode())
    print(data)
for time in data
time['legs']['duration']
