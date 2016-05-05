import requests

# Get city, country, country_code, county, state, zipcode from latitude and longitude
def reverse_geocode(lat, lon):
    d = {"zipcode": "NA", "state": "NA", "country" : "NA", "county" : "NA", "city" : "NA", "country_code" : "NA"}
    try:
        r = requests.get("http://nominatim.openstreetmap.org/reverse?format=json&lat=" + str(lat) + 
                         "&lon=" + str(lon) + "&zoom=18&addressdetails=1")
        data = r.json()["address"]
        d["zipcode"] = data["postcode"]
        d["state"] = data["state"]
        d["country"] = data["country"]
        d["city"] = data["city"]
        d["country_code"] = data["country_code"]
        d["county"] = data["county"]
        return d
    except:
        return {"county" : "invalid"}

fname = "delaware.txt"
resname = "DE_hc_per_county.txt"
CAcount = {}
count = 0
with open(fname, 'r') as f:
    for line in f:
        count += 1
        print count
        lat, lon, tags = line.rstrip().split("\t")
        res = reverse_geocode(lat, lon)
        county = res["county"]
        if county in CAcount:
            CAcount[county] += 1
        else:
            CAcount[county] = 1

cali_per_county = open(resname, "w")
for county in CAcount:
    cali_per_county.write(county + "\t" + str(CAcount[county]))

cali_per_county.close()
