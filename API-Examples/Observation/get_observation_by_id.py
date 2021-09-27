import json
import requests


headers = {
    'Accept': 'application/fhir+json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
}
fhir_server_url = 'https://fhir.dicom.tw/fhir/Observation/66199'
#fhir_server_url = 'https://hapi.fhir.tw/fhir/Observation/66199'

response = requests.get(fhir_server_url, headers=headers)

print(json.loads(response.text))
