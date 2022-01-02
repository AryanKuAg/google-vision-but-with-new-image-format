
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
# for fileIncrement in range(1382, 2001):
# # without jpg
# FILE_NAME = 'Andhra General Scan (Box 2)_Page_' + \
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
# print(data)

###############################################################################
data = "#\n28-Jun-13 4184 270724 Mr. Rajasekhar Chittoor 19-Jul-13 CLOSED NEW REEF GROUP OF COMPANIES \"H.No:4-44, #405, Mohan Stracha\nComplex, Habsi guda,\"\nHYDERABAD 500044 914040132001 914040132002 rajasekha.chittoor@newreef group.com\n24 Apr-09\n270571 Mrs. GAYATRI SINGH 15-May-09 CLOSED NEW REEF IMPEX (P) LTD. \"FLAT NO. 203, MOHAN SHADDHA\nCOMPLEX. OPP. TO NMDC STREET NO.8, HABSIGUDA,\"\nHYDERABAD 500007\ngayathri.singh@newreefgroup.com\n4031\n9-May-05 3887\n270427 \"Mr. RAMA KRISHNA reddy, Mr. RAMA KRISHNA reddy, Pirdi srinivasa Rao, MR.O.P. JALAN\" 30-May-05 OPEN\nDECCAN INDUSTRIAL PRODUCTS PVT. LTD. \"PLOT NO. 2, HAFEEZPET, MINI INDUSTRIAL ESTATE, MIYAPUR\"\nHYDERABAD\n500050 914023045247/23040449 914027542512 \"sravansrinivaa@yahoo.com, info@deplindia.com\"\n26-Jul-11 4114 270654 mr. gaurav singh 16-Aug-11 CLOSED \"JSM (SHENZHEN) ENTERPRISES CO., LTD.\" \"1, Pavani Villas, Dwarkapuri\ncolony, Panjagutta,\"\nHYDERABAD 500082 914023356865 914023356861 gaur avsingh06@gmail.com\n6-Jan-083984 270524 Dr. RANGA RAO 27-Jan-08\nCLOSED\nKN BIO TECH PVT.LTD. \"3, SAGAR SOCIETY, ROAD NO.2, BANJARA\nHILLS,\"\nHYDERABAD 500034 914023546562/23545911 /23747933 (R) 914023545916 kn_biotech@yahoo.co.in\n9-Jul-01 3747 270287 \"Mr. SIV APRASAD M., Mr. balakrishna reddy, MR.G SREENIVAS, Mr. Vijay B Pulavarti, Mr. Syed M Ghouse, Mr. Kishore Kumar, hbinife\npower systems Ltd., Mullapudi Srinivasa Rao, Mr. Mojjada Srinivasa Rao\" 30-Jul-01 CLOSED HBL NIFE POWER SYSTEMS LIMITED \"No.8-2-601,\nRoad No. 10, Banjara Hills,\"\nHYDERABAD 500078 918418244640 918418244627 \"msp@hbl.in, balkireddy@sify.com,\ncortilinks@tatanova.com, vijay_pulavarti@yahoo.com, ghouse@satyam.net.in, sreenivasg@hhlnife.com, hblrife_materials@rediffmail.com, mulapudi@hblnife.com,\nmojjada_mst@yahoo.co.in\"\n27-Dec-09 4056 270596 Mt. MADHUSUDAN 17-Jan-10 OPEN NATL TECHNOLOGIES LTD \"PLOT NO. 30-A, ROAD NO. 1, JUBILLE HILLS,\nFILM NAGAR,\"\nHYDERABAD 500033 914023553459/23553460 914023553462 laksh_nara@yahoo.com\n6-Jun-114109 270649 \"Mr. M. A. SATTAR, Mr. Sadha \"27-Jun-11 OPEN PARAMOUNT CHEMICAL INDUSTRIES\"3-112, FATHENAGAR,\"\nHYDERABAD 500018 914023772440/23745771 (R) 914023772440 flimshady27_007@yahoo.com\n4-Oct-11 4121 270661 Mr. K. Naveen Chandra 25-Oct-11 CLOSED ABR ORGANICS LIMITED \"A-3, Sri Machava Apartments, 2-2-23/41/4\n& 5, Bank Colony, Bagh Am berpet,\nHYDERABAD 500013 914027426059/65575981/27170642 914027426059\nhyd2_abror g@sancharnet, in\n8-Dec-11\n4127 270667 Mr. SURYA KUMAR SIKHA 29-Dec-11 OPEN FORTREC INDIA PRIVATE LIMITED \"201, Pleasant Park, Shanthi Nagar,\nMasab Tank,\"\nHYDERABAD 500028 914066104004 914066755005 sikha@fortrec.com\n24 Jul-10 4077 270617 \"MR. C. KRISHNA, Mr. P. G. Raju\" 14-Aug-10 CLOSED CHEMTECH ACIDS & CHEMICALS PVT. LTD. \"FLAT\nNO. 119, SANALI HEAV PNS APPT., NAGARJUNA NAGAR,\"\nHYDERABAD 500072 914023748372/23742781 914023748374\n\"chemtechhyd@yahoo.com, brau@msn.com\"\n5-Mar-08 3990\n270530 Mr. D. Nageswara Rao 26-Mar-08 CLOSED SUN CHEMICALS \"Plot No. 176 & 190, S.V. Co-op. Industrial Estate,\nIDA, Jeedimetla,\"\nHYDERABAD 500055 914023193717 914023193717\n25-Jul-10 4077 270617 Mr. M. SY AMA SUNDAR 15-Aug-10 OPEN SRIMATHA CHEMICALS & INTERMEDIATES \"HIG-160, BESIDE\nVENKATESWARA SWAMY TEMPLE, PHASE-I, K.P.H.B, COLONY, KUKATPALLY, ROAD NO. 4,\"\nHYDERABAD 500072 914023058645\n914023058645 srim atha_chemind@hotmail.com\n1-Oct-10 4084 270624 MR. TVVSN MURTHY 22-Oct-10 OPEN SRINIVASA PHARMA CHEMICALS PVT. LTD. \"PLOT NO. 66/B-2, PHASE-I,\nIDA, JEEDIMELTA,\n\"C-4,\nHYDERABAD 500055 914023095487/23095233/23746059/60/61 914023095233\n5-Dec-09 4054\n270594 \"Mr. Ravi Prathap Reddy, DR. RAMA KRISHNA\" 26-Dec-09\nCLOSED\nSRI KRISHNA DRUGS LTD\nINDUSTRIAL AREA, UPPAL,\"\nHYDERABAD 500039 914027201101/02/27204471 914027204470/71/27205432\n\"Ik@srikrishnapharma.com, skg@srikristapharma.com\"\n13-Jun-06 3927 270467 Mt. SANDEEP RATHI 4-Jul-06 CLOSED SRI RAM MARKETING \"14/8, 576, Chudi Bazar, Begun Bazar,\"\nHYDERABAD 500012 914024613336 914024613336/30965234\n23-Jun-13 4183 270723 Mr. Sharma 14 Jul-13 CLOSED VADLAXMI INTERMEDIATED AND CHEMICALS PVT LTD.\nIDA, Mallapur,\"\nHYDERABAD 500076 914027152376/23220399 914023220466 s_needi@yahoo.com\n\"Plot No. 169,\n"

entryList = rawToList(data)
# rawToList works fine

rawDataList = columnWiseToList(entryList)
# columnWiseToList works fine

dataFormatted = dataFormatter(rawDataList)
# rawDataList works fine

readyforexcelDataList = entryWiseFormatter(dataFormatted)
# entryWiseFormatter works fine

makeExcelSheet(readyforexcelDataList, FILE_NAME)
