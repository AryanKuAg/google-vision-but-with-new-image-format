

def giveState(rawData):
    rawData = rawData.lower()

    if 'andhra' in rawData:
        return {'state': 'Andhra Pradesh'.upper(), 'index': rawData.find('andhra')}
    elif 'arunachal' in rawData:
        return {'state': 'Arunachal Pradesh'.upper(), 'index': rawData.find('arunachal')}
    elif 'assam' in rawData:
        return {'state': 'Assam'.upper(), 'index': rawData.find('assam')}
    elif 'bihar' in rawData:
        return {'state': 'Bihar'.upper(), 'index': rawData.find('bihar')}
    elif 'chhattisgarh' in rawData:
        return {'state': 'Chhattisgarh'.upper(), 'index': rawData.find('chhattisgarh')}
    elif 'goa' in rawData:
        return {'state': 'GOA', 'index': rawData.find('goa')}
    elif 'gujarat' in rawData:
        return {'state': 'Gujarat'.upper(), 'index': rawData.find('gujarat')}
    elif 'haryana' in rawData:
        return {'state': 'Haryana'.upper(), 'index': rawData.find('haryana')}
    elif 'himachal' in rawData:
        return {'state': 'Himachal Pradesh'.upper(), 'index': rawData.find('himachal')}
    elif 'jammu' in rawData:
        return {'state': 'Jammu and Kashmir'.upper(), 'index': rawData.find('jammu')}
    elif 'jharkhand' in rawData:
        return {'state': 'Jharkhand'.upper(), 'index': rawData.find('jharkhand')}
    elif 'karnataka' in rawData:
        return {'state': 'Karnataka'.upper(), 'index': rawData.find('karnataka')}
    elif 'kerala' in rawData:
        return {'state': 'Kerala'.upper(), 'index': rawData.find('kerala')}
    elif 'madhya' in rawData:
        return {'state': 'Madhya Pradesh'.upper(), 'index': rawData.find('madhya')}
    elif 'maharashtra' in rawData:
        return {'state': 'maharashtra'.upper(), 'index': rawData.find('maharashtra')}
    elif 'manipur' in rawData:
        return {'state': 'Manipur'.upper(), 'index': rawData.find('manipur')}
    elif 'meghalaya' in rawData:
        return {'state': 'Meghalaya'.upper(), 'index': rawData.find('meghalaya')}
    elif 'mizoram' in rawData:
        return {'state': 'Mizoram'.upper(), 'index': rawData.find('mizoram')}
    elif 'nagaland' in rawData:
        return {'state': 'Nagaland'.upper(), 'index': rawData.find('nagaland')}
    elif 'odisha' in rawData:
        return {'state': 'Odisha'.upper(), 'index': rawData.find('odisha')}
    elif 'orissa' in rawData:
        return {'state': 'Orissa'.upper(), 'index': rawData.find('orissa')}
    elif 'punjab' in rawData:
        return {'state': 'Punjab'.upper(), 'index': rawData.find('punjab')}
    elif 'rajasthan' in rawData:
        return {'state': 'Rajasthan'.upper(), 'index': rawData.find('rajasthan')}
    elif 'sikkim' in rawData:
        return {'state': 'Sikkim'.upper(), 'index': rawData.find('sikkim')}
    elif 'tamil' in rawData:
        return {'state': 'Tamil Nadu'.upper(), 'index': rawData.find('tamil')}
    elif 'telangana' in rawData:
        return {'state': 'Telangana'.upper(), 'index': rawData.find('telangana')}
    elif 'tripura' in rawData:
        return {'state': 'Tripura'.upper(), 'index': rawData.find('tripura')}
    elif 'uttar' in rawData:
        return {'state': 'Uttar Pradesh'.upper(), 'index': rawData.find('uttar')}
    elif 'uttarakhand' in rawData:
        return {'state': 'Uttarakhand'.upper(), 'index': rawData.find('uttarakhand')}
    elif 'west bengal' in rawData:
        return {'state': 'West Bengal'.upper(), 'index': rawData.find('west bengal')}

    else:
        return {'state': '', 'index': 100}
