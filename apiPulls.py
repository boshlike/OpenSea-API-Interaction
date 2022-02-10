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
    headers = {
    "Accept": "application/json",
    "X-API-KEY": "API key here"
    }
    params = { # This needs work to build in the right parameters
        'collection': 'beaming-bulldogs',
        'order_by': 'pk',
        'order_direction': 'asc',
        'offset': offset,
        'limit': 50
    }
    r = requests.get('https://api.opensea.io/api/v1/assets', headers=headers, params=params) # ends a GET request using the parameters and headers listed
    response_json = r.json() # Decodes the response json
    data['assets'].extend(response_json['assets']) # .extend adds the data in the response json to the data dictionary that we have initialised above

    if len(response_json['assets']) < 50: # Ends the while loop when the 
        break
    
    offset += 50 # Increases the offset by 50 each time so it can loop through the whole list
    time.sleep(1) # Suspends the execution of the loop for 1 second

# dump entire data structure, you can redirect this output to a file
print(json.dumps(data)) # This needs work as we need to append the  information to a dataframe and export to csv