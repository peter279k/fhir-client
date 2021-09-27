import json
import random
import datetime
import requests


random.seed()
headers = {
    'Accept': 'application/fhir+json',
    'Content-Type': 'application/fhir+json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
}
fhir_server_url = 'https://fhir.dicom.tw/fhir/Observation'
#fhir_server_url = 'https://hapi.fhir.tw//fhir/Observation'

example_date = datetime.datetime.now()
start = example_date
end = start + datetime.timedelta(days=3)
observation_methods = [
    'PCR',
    'Real-Time PCR',
    'RT-PCR',
    'RT-qPCR（ Quantitative Reverse Transcription PCR）',
    'NAA（Nucleic acid Amplification）',
    'NAAT（Nucleic acid Amplification Test）',
    'NAT（Nucleic acid Test）',
    'LAMP（Loop-Mediated isothermal Amplification）',
    'RT-LAMP',
    'COVID-19 RNA test',
    'SARS-CoV-2 RNA test',
    'Molecular Diagnostics',
]
observation_values = [
    'Positive',
    'Negative',
]

example_payload = {
    'resourceType': 'Observation',
    'code': {
        'coding': [
            {
                'system': 'http://loinc.org',
                'code': 'LP6464-4 Nucleic acid amplification with probe detection',
                'display': 'LP217198-3 Rapid immunoassay',
            },
        ],
    },
    'effectivePeriod': {
        'start': start.strftime('%Y-%m-%d'),
        'end': end.strftime('%Y-%m-%d'),
    },
    'issued': end.strftime('%Y-%m-%d'),
    'method': observation_methods[random.randint(0, len(observation_methods)-1)],
    'value': observation_values[0],
    'performer': [
        {
            'reference': 'Organization/66189',
        },
        {
            'address': {
                'country': 'TW (ISO 3166)',
            },
        },
    ],
    'author': [
        {
            'reference': 'Practitioner/66188',
        },
    ],
}

response = requests.post(fhir_server_url, headers=headers, data=json.dumps(example_payload))

print(json.loads(response.text))
