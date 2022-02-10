import requests, json, time

# A function to collect Collection stats from the OpenSea API
def getCollectionStats (collection_slug): # Defines the function and takes a parameter of collection_slug as a string
    headers = {"Accept": "application/json"} # Header requirements
    url = "https://api.opensea.io/api/v1/collection/" + collection_slug + "/stats" # Defines the API URL
    response = requests.request("GET", url, headers=headers) #Uses requests to get a response.
    return response.text # Returns the response text to the API call 


offset = 0

data = {'assets': []}

# fetch assets in collection 50 at a time
while True:
    params = {
        'collection': 'beaming-bulldogs',
        'order_by': 'pk',
        'order_direction': 'asc',
        'offset': offset,
        'limit': 50
    }
 
    r = requests.get('https://api.opensea.io/api/v1/assets', params=params)
    response_json = r.json()
    data['assets'].extend(response_json['assets'])

    if len(response_json['assets']) < 50:
        break
    
    offset += 50

    # uncomment if you want to add a delay in case you get throttled
    time.sleep(1)

# dump entire data structure, you can redirect this output to a file
print(json.dumps(data))