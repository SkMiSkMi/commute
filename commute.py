import urllib.request
url = "https://maps.googleapis.com/maps/api/directions/json?origin=place_id:%s&destination=place_id:%s&key=%s"

OldGC = "ChIJbWgW47aYwokRS_-QioWnp9k"
GC = "ChIJly5MDxGYwokR4jAEYCeuMQg"
Darien = "ChIJC6TcEIegwokReGrCDJwO5Sw"
NC = "ChIJESxVNa-nwokRz27KMKkYEfg"
Rye = "ChIJyVCxxcqQwokR6GnPGTOEaxM"
RHC = "ChIJgd5ICP6XwokRjOFdp-nyXn0"
TwoSigma = "ChIJpf-x64pZwokRYr9BwWaVP9k"

API_Key = "AIzaSyCFgqXKCJF4OS7kqmjiZcECFTX0VM_pK4Y"

request = url % (GC, TwoSigma, API_Key)
print(reques)
