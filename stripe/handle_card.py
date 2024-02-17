import json

 # get json object from rails app backend
 
def get_json():
    with open('card.json') as f:
        data = json.load(f)
    return data

