
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
for fileIncrement in range(10, 11):
    # without jpg
    FILE_NAME = 'Andhra General Scan (Box 1)_Page_00' + \
        str(fileIncrement)

    def makeImageData(imgpath):
        img_req = None
        with open(imgpath, 'rb') as f:
            ctxt = b64encode(f.read()).decode()
            img_req = {
                'image': {
                    'content': ctxt
                },
                'features': [{
                    'type': 'DOCUMENT_TEXT_DETECTION',
                    'maxResults': 1
                }]
            }
        # This also works correctly
        return json.dumps({"requests": img_req}).encode()

    def requestOCR(url, api_key, imgpath):
        imgdata = makeImageData(imgpath)
        response = requests.post(ENDPOINT_URL,
                                 data=imgdata,
                                 params={'key': api_key},
                                 headers={'Content-Type': 'application/json'})
        print(response)
        return response

    with open('vision_api.json') as f:
        data = json.load(f)
    # This function works correctly

    ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'
    api_key = data['api_key']
    img_loc = "rawImage/"+FILE_NAME+".jpg"

    result = requestOCR(ENDPOINT_URL, api_key, img_loc)

    if result.status_code != 200 or result.json().get('error'):
        print("Error")
    else:
        # need some work here
        result = result.json()[
            'responses'][0]['fullTextAnnotation']['text']

    data = result
    print(data)

    ###############################################################################

    entryList = rawToList(data)
    # rawToList works fine

    rawDataList = columnWiseToList(entryList)
    # columnWiseToList works fine

    dataFormatted = dataFormatter(rawDataList)
    # rawDataList works fine

    readyforexcelDataList = entryWiseFormatter(dataFormatted)
    # entryWiseFormatter works fine

    makeExcelSheet(readyforexcelDataList, FILE_NAME)
