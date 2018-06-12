import requests

from keys import USERNAME, PASSWORD
from const import WATSONURL,WATSONHEADER

def translate(text=None,model_id=None):
    payload = {
        'text':text,
        'model_id':model_id
    }
    response = requests.get(WATSONURL,auth=(USERNAME,PASSWORD),headers=WATSONHEADER,params=payload)
    if response.ok:
        data = response.json()
        return data

    else:
        print(response.status_code)
        data='Error: text was not translated'
        return data



if __name__ == '__main__':
    text = input('Translate what ?')
    translate_output=translate(text = text,model_id='en-es')
    print(translate_output['translations'][0]['translation'])