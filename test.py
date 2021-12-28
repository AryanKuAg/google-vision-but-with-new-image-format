
import json
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import requests
import time
from base64 import b64encode
from IPython.display import Image
from pylab import rcParams

import json
from columnWiseToList import columnWiseToList
from dataFormatter import dataFormatter
from entryWiseFormatter import entryWiseFormatter
from makeExcelSheet import makeExcelSheet

from rawToList import rawToList

#
# with open('data.json') as json_file:
#     data = json.load(json_file)
#     print(data)

##############################################################################
# Not my code

# # without jpg
# FILE_NAME = 'HYD Male Survey Scans (Box 1-2)_Page_000' + \
#     str(fileIncrement)

# def makeImageData(imgpath):
#     img_req = None
#     with open(imgpath, 'rb') as f:
#         ctxt = b64encode(f.read()).decode()
#         img_req = {
#             'image': {
#                 'content': ctxt
#             },
#             'features': [{
#                 'type': 'DOCUMENT_TEXT_DETECTION',
#                 'maxResults': 1
#             }]
#         }
#     # This also works correctly
#     return json.dumps({"requests": img_req}).encode()

# def requestOCR(url, api_key, imgpath):
#     imgdata = makeImageData(imgpath)
#     response = requests.post(ENDPOINT_URL,
#                              data=imgdata,
#                              params={'key': api_key},
#                              headers={'Content-Type': 'application/json'})
#     print(response)
#     return response

# with open('vision_api.json') as f:
#     data = json.load(f)
# # This function works correctly

# ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'
# api_key = data['api_key']
# img_loc = "rawImage/"+FILE_NAME+".jpg"

# result = requestOCR(ENDPOINT_URL, api_key, img_loc)

# if result.status_code != 200 or result.json().get('error'):
#     print("Error")
# else:
#     # need some work here
#     result = result.json()[
#         'responses'][0]['fullTextAnnotation']['text']

# data = result

###############################################################################

data = "4106\n4042\n#\nInitialDate of Contact Ledger Folio Date of Entry Mobile Customer Name Customer Address City State Second Ph/Mobile. Date of Birth\nEmail ID Bank Zone Course (Highest Education) RECORD STATUS\n25-Jun-09 4007 270547 19-Jul-09 9247116184 MISARFARAZAFRIDI 22-3-170Y AKAT PURACHARMINAR HYDERABAD ANDHRA\nPRADESH 24418491 23-Jul-82 custfirstname.custlastname@NA Hyderabad/Secunderabad BE/B.Tech OPEN\n12-Apr-08 4084 270624 6-May-08 9247120935 MtIMRAN AHMED\nwith\nH NO 23-1-322/1 BIBI BAZARHYD HYDERABAD ANDHRA\nPRADESH\n14 Aug-82 custfirstname.custlastname@NA Hyderabad/Secunderabad MCA/PGDCA CLOSED\n15-Oct-00 4151 270691 8-Nov-00 9247119460 MANILKUMAR SADRE 2-3-18/16 TULSI NAGAR COLONY AMBERPET HYDERABAD\nANDHRA PRADESH\n6-Jun-84custfirstname.custlastname@NA Hyderabad/ Secunderabad BE/B.Tech OPEN\n7-Aug-92 3924 270464 31-Aug-92 9247116170 MANOOPKUMAR 18-1-337/167 ARUNDATHI COLONY HYDERABAD ANDHRA\nPRADESH\n22-Mar-88\ncustfirstname.custlastname@NA Hyderabad/Secunderabad Others CLOSED\n9-Aug-10 4174\n270714 2-Sep-10 9247113188 MrB.SEETHAIAH CHOWDARY \"H.NO.S1/B/85, SACHIVALAYA NAGAR,VANASTALIPURAM.\"\nHYDERABAD ANDHRA PRADESH 24111662\n20-Apr-84\ncustfirstname.custlastname@NA Hyderabad/ Secunderabad BE/B.Tech\nCLOSED\n19-Aug-09\n270646 12-Sep-09 9247117792 MrB.V.CHALAPATHI \"FLAT NO.103,H.NO.8-3-948/949, NAGARJUNA NAGAR,AMEERPET.\"\nHYDERABAD ANDHRA PRADESH 9849657574 2-Jul-87 custfirstname.custlastname@NA Hyderabad/ Secunderabad MCA/PGDCA CLOSED\n15-Apr-11\n270582 9-May-11 9247116205 MrD.YADAGIRI\"1-9-1113/27/F/139, NAGAMAIAH GUTTA,UPPAL.\" HYDERABAD\nANDHRA PRADESH\n26-Sep-92 custfirstname.\ncustlastname@NA Hyderabad/ Secunderabad B.Sc CLOSED\n14-Dec-07 3951 270491 7-Jan-089247120933 MIFAHEEMSHAIK H NO 17-1-03AHMED NAGARHYD HYDERABAD ANDHRA PRADESH\n14 Oct-87\n50\nOPEN\ncustfirstname.custlastname@NA Hyderabad/Secunderabad BE/B.Tech\n22-Oct-09\n4035 270575 15-Nov-09\n'\n9247122623 MrFAROOQ ALIASMUZAFAR ALI \"19-3-175 JAHANUMA HYD.\" HYDERABAD\nANDHRA PRADESH\n18-Oct-86 custfirstname.custlastname@NA Hyderabad/ Secunderabad B.Com CLOSED\n23-Jul-07 3961 270501 16-Aug-07 9247116220 MIF AZALERASOOL KHAN \"H.NO.16-3-435/1,CHAN CHAL GUDA JUNIOR COLLEGE,.\"\nHYDERABAD ANDHRA PRADESH\n4-Jan-87 custfirstname.custlastname@NA Hyderabad/ Secunderabad BE/B.Tech OPEN\n17-Jul-99 4105\n270645 10-Aug-99\n9247116340\nMrFEROZKHAN\n\"1-9-7116,ADIKMET.\" HYDERABAD ANDHRA PRADESH\n24-May-77\ncustfirstname custlastname@NA Hyderabad/ Secunderabad MBA/PGDM OPEN\n6-Jun-994092 270632 30-Jun-99 9247116161 MIG SIVAKUMAR 1-9-20/A/3/1 RAM NAGAR HYDERABAD ANDHRA PRADESH\n23-Aug-82 custfirstname.custlastname@NA Hyderabad/Secunderabad MBA/PGDM CLOSED\n4-Feb-10 4151 270691 28-Feb-10 9247116311 MG SRINIVASASRAO 8-369/4AUGAPURALLWYN COLONY HYDERABAD ANDHRA\nPRADESH\n15-Jun-87 custfirstname.custlastname@NA Hyderabad/ Secunderabad BE/B.Tech CLOSED\n22-Mar-13 3967\n270507 15-Apr-13\n9247120980 MHANUMANTHUFERTILIZER INDIRA CHOWKITANDUR HYDERABAD ANDHRA\nPRADESH\n7-Aug 83 custfirstname.custlastname@NA Hyderabad/ Secunderabad MBA/PGDM OPEN\n24-Mar-12\n270522 17-Apr-12 9247119420 MrHYDERAIZ. H NOK 9-4-131/1/B/132/ANADEEM NAGAR HYDERABAD ANDHRA\nPRADESH\n24-Feb-81 custfirstname.custlastname@NA Hyderabad/ Secunderabad MBA/PGDM CLOSED\n3-Nov-07 4257 270797 27-Nov-07 9247122659 MuIBRAHIM 16-2-837/1SAIDABAD HYDERABAD ANDHRA PRADESH\n13-Nov-\n82 custfirstname custlastname@NA Hyderabad/ Secunderabad DiplomaOPEN\n10-Sep-13 4143\n270683 4-Oct-13\n9247116238 MBRAHIMSHAREEF 19-2-364/207HUSSAIN ALAM HYDERABAD ANDHRA PRADESH\n15-Aug-87 custfirstname.custlastname@NA Hyderabad/Secunderabad BE/B.Tech CLOSED\n8-Aug-07 3944 270484 1-Sep-07\n9247116159 MIJ SRINIVASARAO H NO 34-98/CVENKATASWARA NAGARJAGATHGIRI GUTTA\nHYDERABAD ANDHRA PRADESH\n4-Jun-84custfirstname.custlastname@NA Hyderabad/ Secunderabad MCA/PGDCA OPEN\n14-Jul-11\n4189 270729 7-Aug-11 9247116448 MIJ ANAYYA H NO 20-1-310HUSSAINI NAGAR HYDERABAD ANDHRA PRADESH\n4-Jun-79 custfirstname.custlastname@NA Hyderabad/ Secunderabad BE/B.Tech CLOSED\n12-Aug-06 4117 270657 5-Sep-06 9247116201 MIK.NARASIMHA REDDY \"PILLY GUNDLLA VILLAGE,SHANKAR PALLY R.R.DIST.\"\nHYDERABAD ANDHRA PRADESH 8417236422 8-Jan-86 custfirstname.custlastname@NA Hyderabad/ Secunderabad MCA/PGDCA OPEN\n3982\n"


entryList = rawToList(data)
# rawToList works fine

rawDataList = columnWiseToList(entryList)
print(rawDataList)

# dataFormatted = dataFormatter(rawDataList)

# readyforexcelDataList = entryWiseFormatter(dataFormatted)

# makeExcelSheet(readyforexcelDataList)
