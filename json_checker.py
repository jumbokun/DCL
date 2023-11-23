import json

with open('/DATA1/bzhu/DCL/annotations/mimic_train_kg_AO.json', 'r') as f:
    data = json.load(f)
    # print(data)
for i, item in enumerate(data):
    if i >= 1: 
        break
    import pprint
    pprint.pprint(item)