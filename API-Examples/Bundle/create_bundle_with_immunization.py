import json
import uuid
import requests
import datetime


fhir_server_url = 'https://hapi.fhir.tw/fhir/Bundle'
#fhir_server_url = 'https://fhir.dicom.tw/fhir/Bundle'

period_start = '2010-09-24'
period_end = '2020-09-24'

type_coding_value = ['82593-5', 'LP6464-4', 'LP217198-3']
type_coding_display = ['Immunization summary report', 'Nucleic acid amplification with probe detection', 'Rapid immunoassay']
title = ['COVID-19 Vaccine', 'Test Certificate']

example_payload = {
    'resourceType': 'Bundle',
    'identifier': [
        {
            'system': 'https://www.vghtc.gov.tw',
            'value': str(uuid.uuid4()),
        },
    ],
    'type': 'document',
    'timestamp': datetime.datetime.isoformat() + '08:00',
    'entry': [
        {
            'resourceType': 'Composition',
            'status': 'final',
            'type': {
                'coding': [
                    {
                        'system': 'http://loinc.org',
                        'value': type_coding_value[0],
                        'display': type_coding_display[0],
                    },
                ],
            },
            'subject': {
                'reference': 'Patient/66176',
                'display': '',
            },
            'date': datetime.datetime.isoformat() + '08:00',
            'title': title[0],
            'author': {
                'reference': '',
                'display': '',
            },
            'section': {
                'entry': [
                    {},
                    {},
                    {}
                ]
            }
        },
        {
            
        },
        {
            
        },
        {

        },
    ],
}


