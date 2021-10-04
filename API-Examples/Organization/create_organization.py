import json
import requests


headers = {
    'Accept': 'application/fhir+json',
    'Content-Type': 'application/fhir+json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
}
fhir_server_url = 'https://fhir.dicom.tw/fhir/Organization'
#fhir_server_url = 'https://hapi.fhir.tw/fhir/Organization'


example_payload = {
    'resourceType': 'Organization',
    'identifier': [
        {
            'system': 'https://ma.mohw.gov.tw',
            'value': '3501113063',
        },
    ],
    'name': '紫陽復健科診所',
    'address': {
        'country': 'TW',
    },
}

response = requests.post(fhir_server_url, headers=headers, data=json.dumps(example_payload))

print(json.loads(response.text))
