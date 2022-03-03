import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SCLproject.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import json
from libsearch.models import Library

with open("libdata.json", "r", encoding="utf8") as f:
    contents = f.read()
    data = json.loads(contents)

dic = ['LBRRY_SEQ_NO',
       'LBRRY_NAME',
       'GU_CODE',
       'CODE_VALUE',
       'ADRES',
       'TEL_NO',
       'HMPG_URL',
       'OP_TIME',
       'FDRM_CLOSE_DATE',
       'LBRRY_SE_NAME',
       'XCNTS',
       'YDNTS'
       ]

for i in range(len(dic)):
    dic[i] = dic[i].lower()

for i in data['DATA']:
    Library(lbrry_seq_no=i['lbrry_seq_no'],
            lbrry_name=i['lbrry_name'],
            gu_code=i['gu_code'],
            code_value=i['code_value'],
            adres=i['adres'],
            tel_no=i['tel_no'],
            hmpg_url=i['hmpg_url'],
            op_time=i['op_time'],
            fdrm_close_date=i['fdrm_close_date'],
            lbrry_se_name=i['lbrry_se_name'],
            xcnts=i['xcnts'],
            ydnts=i['ydnts']).save()
    # print('-------------------------------------------')

print(Library.objects.count())



