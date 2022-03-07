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
                  recommokcha=data['recommokcha'],
                  recomcontens=data['recomcontens'],
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


# def recombook():
#     for i in data:
#         # print(data['recomNo'])
#
#     return

# recombook()























# with open('tests/shed_tool_conf.xml') as fd:
#     doc = xmltodict.parse(fd.read())
#     tools_section = doc['toolbox']['section']['@name']
#     print(tools_section)
#
#     with open('tests/shed_tool_conf.xml') as fd:
#         doc = xmltodict.parse(fd.read())
#         for section in doc['toolbox']['section']:
#             tools_section = section.get('@name')
#         print
#         tools_section


# booklist = ElementTree.fromstring(booklist_root)
# recomdata = []
# bookitem = booklist.iter(tag="item")
#
# for element in bookitem:
#     item = {}
#     item['drCode'] = element.find("drCode").text
#     item['drCodeName'] = element.find("drCodeName").text
#     item['recomtitle'] = element.find("recomtitle").text
#     item['recomauther'] = element.find("recomauther").text
#     item['recompublisher'] = element.find("recompublisher").text
#     item['recomfilepath'] = element.find("recomfilepath").text
#     item['recommokcha'] = element.find("recommokcha").text
#     item['recommcontens'] = element.find("recommcontens").text
#     item['publishYear'] = element.find("publishYear").text
#     item['recomYear'] = element.find("recomYear").text
#     item['recomisbn'] = element.find("recomisbn").text
#     recomdata.append(item)
# print(recomdata)





# for item in data:
#     # drCode = item.find('drCode')
#     # drCodeName = item.find('drCodeName')
#     recomtitle = item.find('recomtitle')
#     # recomauther = item.find('recomauther')
#     # recompublisher = item.find('recompublisher')
#     # recomfilepath = item.find('recomfilepath')
#     # recommokcha = item.find('recommokcha')
#     # recomcontens = item.find('recomcontens')
#     # publishYear = item.find('publishYear')
#     # recomYear = item.find('recomYear')
#     # recomMonth = item.find('recomMonth')
#     # recomisbn = item.find('recomisbn')


# for item in data:
#     # print(data)
#     drCode = int(item.find('drCode'))
#     drCodeName = item.find('drCodeName')
#     recomtitle = item.find('recomtitle')
#     recomauther = item.find('recomauther')
#     recompublisher = item.find('recompublisher')
#     recomfilepath = item.find('recomfilepath')
#     recommokcha = item.find('recommokcha')
#     recomcontens = item.find('recomcontens')
#     publishYear = item.find('publishYear')
#     recomYear = int(item.find('recomYear'))
#     recomMonth = int(item.find('recomMonth'))
#     recomisbn = int(item.find('recomisbn'))
#     print(recomtitle.get_text())






# with open("libdata.json", "r", encoding="utf8") as f:
#     contents = f.read()
#     data = json.loads(contents)
#
# dic = ['LBRRY_SEQ_NO',
#        'LBRRY_NAME',
#        'GU_CODE',
#        'CODE_VALUE',
#        'ADRES',
#        'TEL_NO',
#        'HMPG_URL',
#        'OP_TIME',
#        'FDRM_CLOSE_DATE',
#        'LBRRY_SE_NAME',
#        'XCNTS',
#        'YDNTS'
#        ]
#
# for i in range(len(dic)):
#     dic[i] = dic[i].lower()
#
# for i in data['DATA']:
#     Library(lbrry_seq_no=i['lbrry_seq_no'],
#             lbrry_name=i['lbrry_name'],
#             gu_code=i['gu_code'],
#             code_value=i['code_value'],
#             adres=i['adres'],
#             tel_no=i['tel_no'],
#             hmpg_url=i['hmpg_url'],
#             op_time=i['op_time'],
#             fdrm_close_date=i['fdrm_close_date'],
#             lbrry_se_name=i['lbrry_se_name'],
#             xcnts=i['xcnts'],
#             ydnts=i['ydnts']).save()
#     # print('-------------------------------------------')
#
# print(Library.objects.count())
#
#
#
