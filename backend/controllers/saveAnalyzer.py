import json
import json2txttree as j

filePath = 'C:/Users/Diego/PycharmProjects/intscore/backend/saves/mp_Lan_Xang1478_01_03.json'
# Load json data
with open(filePath, 'r', encoding='utf8') as f:
  jsonData = json.load(f)

# Pretty print json hierarchy as a tree

tree =j.json2txttree(jsonData)
print(type(tree))
with open('jsonTree.txt', 'w', encoding='utf-8') as f:
  f.writelines(tree)
