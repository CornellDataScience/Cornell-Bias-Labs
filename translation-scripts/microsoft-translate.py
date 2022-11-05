import requests, uuid, json
from dotenv import dotenv_values
import csv

input_csv_name = "../data/occupations.csv"
output_csv_name = "microsoft-translate-output-sp.csv"

config = dotenv_values(".env")  

key = config["MS_API_KEY"]
endpoint = "https://api.cognitive.microsofttranslator.com"

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
location = config["MS_LOCATION"]

path = '/translate'
constructed_url = endpoint + path

params = {
'api-version': '3.0',
'from': 'en',
'to': 'es'
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

with open(input_csv_name, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        output_csv = open(output_csv_name, 'w')
        writer = csv.writer(output_csv)
        for row in csvreader:
            occupation = row[1]
            body = [{
            'text': occupation
            }]

            request = requests.post(constructed_url, params=params, headers=headers, json=body)
            response = request.json()
            print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
            writer.writerow([occupation, response[0]['translations'][0]['text']])

        output_csv.close()

    

# print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))