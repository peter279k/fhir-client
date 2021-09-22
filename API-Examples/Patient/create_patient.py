import json
import datetime
import requests


headers = {
    'Accept': 'application/fhir+json',
    'Content-Type': 'application/fhir+json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
}
fhir_server_url = 'https://fhir.dicom.tw/fhir/Patient'
#fhir_server_url = 'https://hapi.fhir.tw//fhir/Patient'

today = datetime.datetime.now().isoformat() + '+08:00'

example_payload = {
    'resourceType': 'Patient',
    'identifier': [
        {
            'system': 'http://system.lab.website',
            'value': 'U123456789',
        }
    ],
    'name': [
        {
            'text': 'Peter Li',
            'family': 'Li',
            'given': ['Peter Li'],
        }
    ],
    'contact': [{
        'name': 'Peter Li',
        'telecom': '0910123456',
        'address': 'Taiwan, Taipei',
        'organization': 'III',
    }],
    'gender': 'male',
    'birthDate': '1993-06-30',
    'managingOrganization': {},
}

response = requests.post(fhir_server_url, headers=headers, data=json.dumps(example_payload))

print(json.loads(response.text))
