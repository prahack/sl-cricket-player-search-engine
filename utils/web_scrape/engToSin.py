import json
from googletrans import Translator
translator = Translator()


converted = []
with open('D:\/1 E drive\Sem 7\DM & IR\IR\IR project\/final_all_with_career copy.json') as f:
    data = json.load(f)

player_id_list = list(data.keys())
print(player_id_list)
for name in player_id_list:
    obj = data[name]
    print(name)
    obj['name'] = translator.translate(obj['name'], dest='si').text
    obj['batting'] = translator.translate(obj['batting'], dest='si').text
    obj['bowling'] = translator.translate(obj['bowling'], dest='si').text
    obj['description'] = translator.translate(obj['description'], dest='si').text
    obj['career'] = translator.translate(obj['career'], dest='si').text
    
    converted.append(obj)

out_file = open("final_sinhala.json", "w", encoding='utf-8')
json_data = json.dump(converted, out_file, indent = 4, ensure_ascii=False)