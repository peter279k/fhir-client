import json
import datetime
import requests


headers = {
    'Accept': 'application/fhir+json',
    'Content-Type': 'application/fhir+json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
}
fhir_server_url = 'https://fhir.dicom.tw/fhir/Composition'
#fhir_server_url = 'https://hapi.fhir.tw//fhir/Composition'

type_coding_value = ['82593-5', 'LP6464-4', 'LP217198-3']
type_coding_display = ['Immunization summary report', 'Nucleic acid amplification with probe detection', 'Rapid immunoassay']
title = ['COVID-19 Vaccine', 'Test Certificate']

example_payload = {
    'resourceType': 'Composition',
    'status': 'final',
    'type': {
        'coding': [
            {
                'system': 'http://loinc.org',
                'code': type_coding_value[0],
                'display': type_coding_display[0],
            },
        ],
    },
    'subject': [
        {
            'reference': 'Patient/66215',
        }
    ],
    'date': datetime.datetime.now().isoformat().split('.')[0] + '+08:00',
    'title': title[0],
    'author': [
        {
            'reference': 'Organization/66217',
        },
    ],
    'section': {
        'entry': [
            {
                'reference': 'Organization/66217',
            },
            {
                'reference': 'Patient/66215',
            },
            {
                'reference': 'Immunization/66220',
            },
        ],
    },
}

response = requests.post(fhir_server_url, headers=headers, data=json.dumps(example_payload))

print(json.loads(response.text))
