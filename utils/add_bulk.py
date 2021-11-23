from elasticsearch import Elasticsearch
from elasticsearch import helpers
import json


es = Elasticsearch()

INDEX = 'sl-cricket'
TYPE = 'player'

converted = []
with open('D:\/1 E drive\Sem 7\DM & IR\IR\IR project\/final_sinhala.json', encoding='utf-8') as f:
    data = json.load(f)

player_objs = []

for player in data:
    obj = {}
    
    print(player['name'])
    
    obj['name'] = player['name']
    obj['birthday'] = player['born']
    obj['batting'] = player['batting']
    obj['bowling'] = player['bowling']
    obj['description'] = player['description']
    obj['career'] = player['career']
    obj['matches'] = int(player['stats']['test']['matches'])
    obj["runs"] = int(player['stats']['test']['runs'])
    obj["wickets"] = int(player['stats']['test']['wickets'])
    obj["top_score"] = int(player['stats']['test']['top_score'])
    obj["best_bowling"] = player['stats']['test']['best_bowling']
    player_objs.append(obj)

actions = []
i = 1

for obj in player_objs:
    actions.append({
        "_index": INDEX,
        "_type": TYPE,
        "_id": i,
        "_source": obj
    })
    i += 1

helpers.bulk(es, actions)