import requests

from keys import USERNAME, PASSWORD
from const import WATSONURL


response = requests.get(WATSONURL)

print (response)