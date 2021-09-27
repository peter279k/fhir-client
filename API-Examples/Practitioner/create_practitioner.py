import json
import requests


headers = {
    'Accept': 'application/fhir+json',
    'Content-Type': 'application/fhir+json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chro    me/94.0.4606.54 Safari/537.36',
}

fhir_server_url = 'https://fhir.dicom.tw/fhir/Practitioner'
#fhir_server_url = 'https://hapi.fhir.tw//fhir/Practitioner'

example_payload = {
    'resourceType': 'Practitioner',
    'active': True,
    'identifier': [
        {
            'value': 'V123456789',
        },
    ],
    'name': [
        {
            'family': '李',
            'given': [ '大明' ],
            'prefix': [ 'Dr' ],
        },
    ],
}

response = requests.post(fhir_server_url, headers=headers, data=json.dumps(example_payload))

print(json.loads(response.text))
