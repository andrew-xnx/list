import json

j_1 = 'data_1.json'
j_2 = 'data_2.json'

with open(j_1, 'r') as f1:
    dataone = json.load(f1)

with open(j_2, 'r') as f2:
    datatwo = json.load(f2)


#fkMacrozona


for data_1 in dataone:
    for data_2 in datatwo:
        if 'fkMacrozona' in data_1 and 'fkMacrozona' in data_2:
           if data_2['fkMacrozona'] == data_1['fkMacrozona']:
            data_1['location'] = data_2
            print(data_1)


