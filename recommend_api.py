import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SCLproject.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import requests
import xmltodict
import json
from recommend.models import Recommend
# from bs4 import BeautifulSoup


# params = {
#     'key' : '8247c0b40458e2a93e8d1b9a713ef57dd38dba9a6e060b726a6119edc0391983',
#     'startRowNumApi' : '1',
#     'endRowNemApi' : '99999',
#     'start_date' : '20200101',
#     'end_date' : '20221231',
# }


url = "https://nl.go.kr/NL/search/openApi/saseoApi.do?key=8247c0b40458e2a93e8d1b9a713ef57dd38dba9a6e060b726a6119edc0391983&startRowNumApi=1&endRowNumApi=999999&start_date=20100101&end_date=20221231"
result = requests.get(url)
# soup = BeautifulSoup(result, 'html.parser')
# data = soup.find_all()

recomxpar = xmltodict.parse(result.text)
recomload = json.loads(json.dumps(recomxpar))
data = recomload['channel']['list']
for i in data:
    data = i.get('item')
    try:
        Recommend(recomNo=data['recomNo'],
                  drCode=data['drCode'],
                  drCodeName=data['drCodeName'],
                  recomtitle=data['recomtitle'],
                  recomauthor=data['recomauthor'],
                  recompublisher=data['recompublisher'],
                  recomfilepath=data['recomfilepath'],
                  recommokcha=data['recommokcha.string'],
                  recomcontens=data['recomcontens.string'],
                  publishYear=data['publishYear'],
                  recomYear=data['recomYear'],
                  recomMonth=data['recomMonth'],
                  recomisbn=data['recomisbn']).save()
    except KeyError:
        Recommend(drCode=None,
                  drCodeName=None,
                  recomtitle=None,
                  recomauthor=None,
                  recompublisher=None,
                  recomfilepath=None,
                  recommokcha=None,
                  recomcontens=None,
                  publishYear=None,
                  recomYear=None,
                  recomMonth=None,
                  recomisbn=None).save()