import requests 
import json

@app.route('/alltodoitems' , methods=['GET'])
def alltodoitems():
    url = "https://api.trello.com/1/boards/{61bb961c223edf0a94b3973f}/cards"

response = requests.request(
   "GET",
    url,
    cards=open
)

    print(response.text)

@app.route('/createnewcard' , methods=['POST'])
def createnewcard ():
    url = "https://api.trello.com/1/cards"

    headers = {
        "Accept": "application/json"
}

    query = {
        'idList': '61b9c21fde84b95cb7973adc'
}

    response = requests.request(
        "POST",
        url,
        headers=headers,
        params=query
)

        print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
