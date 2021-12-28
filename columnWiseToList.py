
import re

from giveCity import giveCity
from giveState import giveState


def columnWiseToList(rawData):
    finalColumnSeperatedList = []

    # Date pattern
    pattern1 = re.compile("\d\d-\w\w\w-\d\d")  # 33-Mar-43
    pattern2 = re.compile("\d-\w\w\w-\d\d")  # 5-Jul-34
    pattern3 = re.compile("\d-\w\w\w\d")  # 6-Mar6
    pattern4 = re.compile("\d-\w\w\w-\d")  # 4-mar-3
    pattern5 = re.compile("\d\w\w\w-\d")  # 6mar-3
    pattern6 = re.compile("-\w\w\w-\d")  # -Dec-06
    pattern7 = re.compile("\d\d-\w\w\w- \d\d")  # 10-May- 12
    pattern8 = re.compile("\d\d\w\w\w-\d\d")  # 24Aug-07
    pattern9 = re.compile("\d-\w\w-\d")  # 4-Ap-0?
    pattern10 = re.compile("\d\d-\w\w\w-\d")  # 13-Apr-0?
    # pattern11 = re.compile("\w\w\w-\d\d")  # May-84

    for index, element in enumerate(rawData):

        finalColumnSeperatedList.append(
            [[], [], [], [], [], [], [], [], [], [], [], [], [], []])

        try:

            if len(element) < 10:
                continue

            splitted = element.split()

            # Initial date of contact

            if len(splitted[0]) < 10:

                finalColumnSeperatedList[index][0].append(splitted[0])
            elif len(splitted[0]) < 14:  # 12-Apr-114103

                finalColumnSeperatedList[index][0].append(
                    splitted[0][0:len(splitted[0]) - 4])
                finalColumnSeperatedList[index][1].append(
                    splitted[0][len(splitted[0]) - 4:])

            # Ledger number
            if len(finalColumnSeperatedList[index][1]) == 0 and len(splitted[1]) < 6:
                finalColumnSeperatedList[index][1].append(
                    splitted[1])

            # Folio Number
            if len(splitted[1]) == 6:
                finalColumnSeperatedList[index][2].append(
                    splitted[1])
            elif len(splitted[2]) == 6:
                finalColumnSeperatedList[index][2].append(
                    splitted[2])

            #################################################################
            ##########EVERYTHING IS WELL AND GOOD ABOVE######################
            #################################################################

            # This is for the name or customer name
            if len(finalColumnSeperatedList[index][2]) > 0:
                folioNumberIndex = element.index(
                    finalColumnSeperatedList[index][2][0])
            else:
                folioNumberIndex = 12

            # This is just initial data if we don't able to find it okay...)_)
            # THIS IS FOR THE INITIAL DATE OF ENTRY

            # THIS VARIABLE GET DATE AND SOME EXTRA DATA
            gotDateAndExtras = element[folioNumberIndex +
                                       6: folioNumberIndex + 18]

            if (pattern1.search(gotDateAndExtras) or pattern2.search(gotDateAndExtras) or pattern3.search(gotDateAndExtras) or pattern4.search(gotDateAndExtras) or pattern5.search(gotDateAndExtras) or pattern6.search(gotDateAndExtras) or pattern7.search(gotDateAndExtras) or pattern8.search(gotDateAndExtras) or pattern9.search(gotDateAndExtras) or pattern10.search(gotDateAndExtras)) and gotDateAndExtras.count('-') == 2:
                finalColumnSeperatedList[index][3].append(
                    gotDateAndExtras.split()[0])

            # PHONE NUMBER 1

            if len(finalColumnSeperatedList[index][3]) > 0:
                dateOfEntryIndex = element.index(
                    finalColumnSeperatedList[index][3][0])
            else:
                dateOfEntryIndex = element.index(
                    finalColumnSeperatedList[index][0][0]) + 30

            tempphoneOne = element[dateOfEntryIndex + 8: dateOfEntryIndex + 25]
            phoneOne = ''
            for nono in tempphoneOne.split():
                if len(nono) > 5:
                    finalColumnSeperatedList[index][4].append(nono)
                    phoneOne = nono

            # just to not get error
            if len(finalColumnSeperatedList[index][4]) == 0:
                finalColumnSeperatedList[index][4].append('')

             # ABOVE GOOD
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
              # DOWN BAD

            # CUSTOMER NAME
            # START WITH NUMBER + NUMBER LENGTH + 22 CHARACTER IS UPPER
            phoneOneIndex = element.index(
                finalColumnSeperatedList[index][4][0]) + len(finalColumnSeperatedList[index][4][0])

            customerNameandData = element[phoneOneIndex: phoneOneIndex + 22]
            numberPattern = re.compile('[0-9]')
            customerName = ''

            for ii, name in enumerate(customerNameandData):
                if ii == len(customerNameandData) - 1:
                    break
                if '"' in name or numberPattern.search(name) or '-' in name:
                    break
                if (name == "H" and customerNameandData[ii + 1] == " ") or (name == "H" and customerNameandData[ii + 1] == "N") or (name == "P" and customerNameandData[ii + 1] == "L") or (name == "H" and customerNameandData[ii + 1] == "O"):
                    break
                customerName += name

            # H NO purifier
            if customerName.find('H NO') > 0:
                customerName = customerName[0:customerName.find('H NO')]

            finalColumnSeperatedList[index][5].append(customerName.strip())
####################################################################################################
            # STATE
            state = giveState(element)
            finalColumnSeperatedList[index][9].append(state['state'])

            # CITY
            stateIndex = state['index']
            tempCityData = element[stateIndex - 15:stateIndex]
            city = tempCityData.split()[len(tempCityData.split()) - 1]
            finalColumnSeperatedList[index][8].append(str(city).strip())

######################################################################################################
            stateLastIndex = stateIndex + len(state['state'])
            tempDate = element[stateLastIndex: stateLastIndex + 15]

            # assuming phonetwo is not given
            if (pattern1.search(tempDate) or pattern2.search(tempDate) or pattern3.search(tempDate) or pattern4.search(tempDate) or pattern5.search(tempDate) or pattern6.search(tempDate) or pattern7.search(tempDate) or pattern8.search(tempDate) or pattern9.search(tempDate) or pattern10.search(tempDate)) and tempDate.count('-') == 2:
                pass
                # tempDate = tempDate.split()[0]
                # if tempDate.find('c') > 0:
                #     tempDate = str(tempDate[:tempDate.find('c')]).strip()
                # else:
                #     tempDate = tempDate.strip()

                # print('tempDate', tempDate)

            else:
                phoneTwo = ''

                for yo in tempDate.split():
                    if len(yo) > 6 and not '-' in yo:
                        phoneTwo = yo
                        finalColumnSeperatedList[index][10].append(
                            str(phoneTwo).strip())

    #################################################################################################
            # Date of birth
            if len(finalColumnSeperatedList[index][10]) > 0:
                allTemp = stateLastIndex + \
                    len(finalColumnSeperatedList[index][10][0])
                tempDate = element[allTemp: allTemp + 15]

            if (pattern1.search(tempDate) or pattern2.search(tempDate) or pattern3.search(tempDate) or pattern4.search(tempDate) or pattern5.search(tempDate) or pattern6.search(tempDate) or pattern7.search(tempDate) or pattern8.search(tempDate) or pattern9.search(tempDate) or pattern10.search(tempDate)) and tempDate.count('-') == 2:
                for yoyo in tempDate.split():
                    if len(yoyo) > 6 and '-' in yoyo:
                        if yoyo.find('c') > 0:
                            yoyo = str(yoyo[:yoyo.find('c')]).strip()
                        else:
                            yoyo = yoyo.strip()

                        finalColumnSeperatedList[index][11].append(
                            str(yoyo).strip())

            #     tempDate = tempDate.split()[0]
            #     if tempDate.find('c') > 0:
            #         tempDate = str(tempDate[:tempDate.find('c')]).strip()
            #     else:
            #         tempDate = tempDate.strip()
            #     finalColumnSeperatedList[index][11].append(
            #         str(tempDate).strip())
            #     print('else', tempDate)

###########################################################################################################
            # open closed
            if 'open' in element.lower():
                finalColumnSeperatedList[index][13].append(
                    'OPEN')
            elif 'closed' in element.lower():
                finalColumnSeperatedList[index][13].append(
                    'CLOSED')

#######################################################################################
            # ADDRESS TIME
            if len(finalColumnSeperatedList[index][5]) > 0 and len(finalColumnSeperatedList[index][8]) > 0:
                cityFirstIndex = stateIndex - len(city)
                nameLastIndex = element.find(str(finalColumnSeperatedList[index][5][0])[
                    len(finalColumnSeperatedList[index][5][0]) - 4:]) + 4
                # print(element[nameLastIndex:cityFirstIndex - 1])
                finalColumnSeperatedList[index][6].append(
                    str(element[nameLastIndex:cityFirstIndex - 1]).replace('"', '').strip())
###########################################################################
            # EMAIL ADDRESS
            email = ''

            if len(finalColumnSeperatedList[index][5]) > 0:
                tempNameHolder = str(finalColumnSeperatedList[index][5][0]).replace("MIJ", '').replace("MIS", '').replace('MrB', '').replace(
                    '.', '').replace('MrD', '').replace("MIG", '').replace("MG", '').replace("MIK", '').replace("Mr", '').replace("Mu", '').replace("Mt", '')

                for mailindex, mail in enumerate(str(tempNameHolder).split()):
                    if mailindex == 0:
                        email += mail
                        if len(tempNameHolder.split()) > 1:
                            email += '.'
                    if mailindex == 1:
                        email += mail

            email += '@gmail.com'

            finalColumnSeperatedList[index][12].append(
                email.strip())

        except:
            print('a little bit error again')

    return finalColumnSeperatedList
