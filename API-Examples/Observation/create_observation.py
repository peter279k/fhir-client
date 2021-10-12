import json
import uuid
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
    'id': str(uuid.uuid4()),
    'status': 'final',
    'code': {
        'coding': [
            {
                'system': 'http://loinc.org',
                'code': 'LP6464-4',
                'display': 'Nucleic acid amplification with probe detection',
            },
        ],
    },
    'effectivePeriod': {
        'start': start.isoformat().split('.')[0] + 'Z',
        'end': end.isoformat().split('.')[0] + 'Z',
    },
    'valueString': observation_values[0],
    'performer': [
        {
            'reference': 'Organization/66189',
        },
    ],
}

response = requests.post(fhir_server_url, headers=headers, data=json.dumps(example_payload))

print(json.loads(response.text))
