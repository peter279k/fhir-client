import json
import uuid
import requests
import datetime


def get_organization_by_id(org_id):
    fhir_server_url = 'https://fhir.dicom.tw/fhir/Organization/' + org_id
    headers = {
        'Accept': 'application/fhir+json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
    }
    response = requests.get(fhir_server_url, headers=headers)

    return json.loads(response.text)

def get_patient_by_id(patient_id):
    fhir_server_url = 'https://fhir.dicom.tw/fhir/Patient/' + patient_id
    headers = {
        'Accept': 'application/fhir+json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
    }
    response = requests.get(fhir_server_url, headers=headers)

    return json.loads(response.text)

def get_immunization_by_id(immunization_id):
    fhir_server_url = 'https://fhir.dicom.tw/fhir/Immunization/' + immunization_id
    headers = {
        'Accept': 'application/fhir+json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
    }
    response = requests.get(fhir_server_url, headers=headers)

    return json.loads(response.text)

def get_composition_by_id(composition_id):
    fhir_server_url = 'https://fhir.dicom.tw/fhir/Composition/' + composition_id
    headers = {
        'Accept': 'application/fhir+json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
    }
    response = requests.get(fhir_server_url, headers=headers)

    return json.loads(response.text)


fhir_server_url = 'https://fhir.dicom.tw/fhir/Bundle'
#fhir_server_url = 'https://hapi.fhir.tw/fhir/Bundle'

headers = {
    'Accept': 'application/fhir+json',
    'Content-Type': 'application/fhir+json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
}

period_start = '2010-09-24'
period_end = '2020-09-24'

example_payload = {
    'resourceType': 'Bundle',
    'identifier': [
        {
            'system': 'https://www.vghtc.gov.tw',
            'value': str(uuid.uuid4()),
            'period': {
                'start': period_start,
                'end': period_end,
            },
        },
    ],
    'type': 'document',
    'timestamp': datetime.datetime.now().isoformat().split('.')[0] + '+08:00',
    'entry': [
        get_composition_by_id('66197'),
        get_organization_by_id('66189'),
        get_patient_by_id('66187'),
        get_immunization_by_id('66192'),
    ],
}

response = requests.post(fhir_server_url, headers=headers, data=json.dumps(example_payload))

print(json.loads(response.text))
