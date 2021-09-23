import json
import requests


headers = {
    'Accept': 'application/fhir+json',
    'Content-Type': 'application/fhir+json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
}

patient_id = '66177'
fhir_server_url = 'https://fhir.dicom.tw/fhir/Patient/' + patient_id
#fhir_server_url = 'https://hapi.fhir.tw//fhir/Patient/' + patient_id

example_payload = {
    'resourceType': 'Patient',
    'id': patient_id,
    'identifier': [
        {
            'system': 'http://system.lab.website',
            'value': 'S123456789',
        }
    ],
    'name': [
        {
            'text': 'Peter Li',
            'family': 'Li',
            'given': ['Peter Li', 'Chun-Sheng, Li'],
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

response = requests.put(fhir_server_url, headers=headers, data=json.dumps(example_payload))

print(json.loads(response.text))
