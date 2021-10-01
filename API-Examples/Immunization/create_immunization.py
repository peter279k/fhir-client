import json
import datetime
import requests


headers = {
    'Accept': 'application/fhir+json',
    'Content-Type': 'application/fhir+json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
}
fhir_server_url = 'https://fhir.dicom.tw/fhir/Immunization'
#fhir_server_url = 'https://hapi.fhir.tw//fhir/Immunization'

vaccine_identifiers = [
    'J07BX03 covid-19 vaccines (ATC)'
    '1119349007 COVID-19 mRNA vaccine (SNOMED CT)',
    '1119305005 COVID-19 antigen vaccine (SNOMED CT)',
]
vaccine_codes = [
    'AZ',
    'Cov',
]
displlay_vaccine_codes = [
    'AZD1222',
    'BNT162b2',
    'mRNA-1273',
    'MVC-COV1901',
]
manufacturers = [
    'AstraZeneca',
    'Pfizer BioNTech',
    'Moderna Biotech',
    'Medigen',
]

example_date = datetime.datetime.now().strftime('%Y-%m-%d')
example_payload = {
    'resourceType': 'Immunization',
    'vaccineCode': {
        'coding': [
            {
                'system': 'https://www.cdc.gov.tw',
                'code': vaccine_codes[0],
            },
        ],
        'display': displlay_vaccine_codes[0],
    },
    'manufacturer': manufacturers[0],
    'patient': {
        'reference': 'Patient/66187',
    },
    'protocolApplied': [
        {
            'doseNumberPositiveInt': 1,
        },
        {
            'seriesDosesPositiveInt': 2,
        },
        {
            'targetDisease': {
                'system': 'http://hl7.org/fhir/sid/icd-10',
                'value': 'U07.1',
            },
        },
    ],
    'lotNumber': 'SA123456789',
    'occurrence': '2021-08-30',
    'performer': [
        {
            'actor': {
                'reference': 'Organization/66189',
                'address': {
                    'country': 'ISO 3166 (TW)',
                },
            },
        },
        {
            'actor': {
                'display': 'Practitioner/66188',
            },
        },
    ],

}

response = requests.post(fhir_server_url, headers=headers, data=json.dumps(example_payload))

print(json.loads(response.text))
