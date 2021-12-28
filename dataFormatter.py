

import re

from giveMonthIndex import giveMonthIndex


def dataFormatter(rawDataList):
    dateMonthPattern = re.compile('[A-Z][a-z][a-z]')
    for index, element in enumerate(rawDataList):
        # INITIAL DATE OF CONTACT
        try:
            if len(element[0]) > 0:
                element[0][0] = element[0][0].replace('-', '/')

                monthMatch = dateMonthPattern.search(element[0][0]).group()

                element[0][0] = element[0][0].replace(
                    monthMatch, giveMonthIndex(monthMatch))
        except:
            print('initial date error')

        # INITIAL DATE OF RECORD
        if len(element[3]) > 0:
            try:
                element[3][0] = element[3][0].replace('-', '/')
                #########
                if not element[3][0] == '':
                    monthMatch = dateMonthPattern.search(element[3][0]).group()

                    element[3][0] = element[3][0].replace(
                        monthMatch, giveMonthIndex(monthMatch))
            except:
                pass

        # DATE OF BIRTH
        if len(element[11]) > 0:
            element[11][0] = element[11][0].replace('-', '/')
            try:
                if not element[11][0] == '':
                    monthMatch = dateMonthPattern.search(
                        element[11][0]).group()

                    element[11][0] = element[11][0].replace(
                        monthMatch, giveMonthIndex(monthMatch))
            except:
                pass

        # PHONE NUMBER FORMATTER
        if len(element[4]) > 0:
            if len(element[4][0]) == 10:
                element[4][0] = '+91 ' + element[4][0][0:5] + \
                    " " + element[4][0][5:]
        if len(element[10]) > 0:
            if len(element[10][0]) == 10:
                element[10][0] = '+91 ' + element[10][0][0:5] + \
                    " " + element[10][0][5:]

        # EMAIL FORMATTER
        if len(element[12]) > 0:
            element[12][0] = element[12][0].replace(" ", '').lower()

        # NAME FORMATTER
        if len(element[5]) > 0:
            element[5][0] = element[5][0].upper()

    return rawDataList
