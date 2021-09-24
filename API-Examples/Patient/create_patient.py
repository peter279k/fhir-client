import json
import requests


headers = {
    'Accept': 'application/fhir+json',
    'Content-Type': 'application/fhir+json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
}
patient_id = ''
fhir_server_url = 'https://fhir.dicom.tw/fhir/Patient'
#fhir_server_url = 'https://hapi.fhir.tw//fhir/Patient'


example_payload = {
    'resourceType': 'Patient',
    'identifier': [
        {
            'use': 'usual',
            'type': {
                'text': '身分證字號',
            },
            'value': 'U123456789',
            'assigner': {
                'display': '內政部',
            },
        }
    ],
    'active': True,
    'name': [
        {
            'text': 'Peter Li',
        }
    ],
    'gender': 'male',
    'birthDate': '1993-06-30',
    'address': [
        {
            'use': 'home',
            'text': '105台北市松山區民生東路四段133號',
        },
    ],
    'telecom': [
        {
            'use': 'home',
            'system': 'phone',
            'value': '0910123456',
        }
    ],
    'managingOrganization': {},
}

response = requests.post(fhir_server_url, headers=headers, data=json.dumps(example_payload))

print(json.loads(response.text))
