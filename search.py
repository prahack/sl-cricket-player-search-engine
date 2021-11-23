import re
import queries
from helper import calSimilarity_words
from lists import list_runs, list_wickets, gte, lte, all,names
from elasticsearch import Elasticsearch, helpers
# from preprocessing import preprocess

client = Elasticsearch(HOST="http://localhost",PORT=9200)
INDEX = 'sl-cricket'

#boosting function
def boost(boost_array):
    name ="name^{}".format(boost_array[1])
    batting = "batting^{}".format(boost_array[2])
    bowling = "bowling^{}".format(boost_array[3])
    matches = "matches^{}".format(boost_array[4])
    top_score = "top_score^{}".format(boost_array[7])
    best_bowling = "best_bowling^{}".format(boost_array[8])
    
    return [name, batting, bowling, matches, top_score, best_bowling]


#function for search using the name
def searchByName(tokens):
  found_name = False
  for t in range(len(tokens)):
    token = tokens[t]

    for name in names:
      name_list = name.split()
      for i in range(len(name_list)):
        if calSimilarity_words(token, name_list[i], 0.8) and abs(len(token)-len(name_list[i])) <= 1:
            tokens.append(name_list[i])
            found_name = True
  return found_name


def search(phrase):
    #name,batting,bowling,matches,runs,wickets,top_score,best_bowling
    flags = [1, 1, 1, 1, 0, 0, 1, 1, 1]

    # #search list
    # # 0 - position
    # # 1 - party
    # # 2 - district
    # # 3 - related_subjects
    # # 4 - contact info
    # # 5 - participation
    # search_list = [0, 0, 0, 0, 0, 0]

    num=0
    tokens = phrase.split()
    search_by_name = searchByName(tokens)
    tokens = list(set(tokens))
    containsDigit = bool(re.search(r'\d', phrase))
    meassure = None
    field = None
    if search_by_name:
        print("Name found")
        flags[0] = 5
    #   for word in tokens:
    #     for i in range(len(synonym_list)):
    #       if word in synonym_list[i]:
    #         print('Boosting field', i, 'for', word, 'in synonym list - search by name')
    #         search_list[i] = 1
    #         break

    elif containsDigit: #check number
      popularity = False
      participation = False
      before_birth = False

      for word in tokens:
        # highest runs
        # lowest runs
        # highest wickets
        # lowest wickets
        # more than x matches
        # less than x matches
        # more than x runs
        # less than x runs
        # more than x wickets
        # less than x wickets
        
        if word.isdigit():
          num = int(word)
        if word in gte:
            meassure = 'gte'
        if word in lte:
            meassure = 'lte'
        if word in list_wickets:
            field = 'wickets'
            flags[5] = 1
        if word in list_runs:
            field = 'runs'
            flags[4] = 1


    else: #Not a name or not a digit
      # Identify numbers
      search_terms = []
      for w in range(len(tokens)):
          word = tokens[w]

          # Check whether a value from any list is present
          for i in range(len(all)):
              l =  all[i]
              for term in l:
                ts = term.split()
                for j in range(len(ts)):
                  if calSimilarity_words(word, ts[j]):
                    # tokens[w] = ts[j]
                    search_terms.append(ts[j])
                    print('Boosting field',i+2,'for',word,ts[j],'in all list')
                    flags[i+2] = 5
                    

          # Check whether token matches any synonyms
        #   for i in range(4):
        #       if word in synonym_list[i]:
        #           print('Boosting field', i, 'for', word, 'in synonym list')
        #           flags[i+2] = 5

      tokens = search_terms
    fields = boost(flags)


    phrase = " ".join(tokens)
    print(phrase, fields)
    res = []
    #Quering elasticsearch 
    if flags[0] == 5: #if have a name
            query_body = queries.exact_match(phrase)
            res = client.search(index=INDEX, body=query_body)
            resl = res['hits']['hits']
            print(resl)
            outputs = []
            for hit in resl:
              player = hit['_source']
              name = player["name"]
              birthday = player["birthday"]
              batting = player["batting"]
              bowling = player["bowling"]
              description = player["description"] 
              career = player["career"]
              matches = player["matches"]
              runs = player["runs"]
              wickets = player["wickets"] 
              top_score = player["top_score"]
              best_bowling = player["best_bowling"]
              outputs.append([name, birthday, batting, bowling, description, career, matches, runs, wickets, top_score, best_bowling])
            res = outputs
    elif flags[4] == 1 and meassure != None:
        print('runs', meassure, num)
        query_body = queries.field_value_condition_q(phrase, 'runs', num, meassure)
        res = client.search(index=INDEX, body=query_body)
        resl = res['hits']['hits']
        print(resl)
        outputs = []
        for hit in resl:
            player = hit['_source']
            name = player["name"]
            birthday = player["birthday"]
            batting = player["batting"]
            bowling = player["bowling"]
            description = player["description"] 
            career = player["career"]
            matches = player["matches"]
            runs = player["runs"]
            wickets = player["wickets"] 
            top_score = player["top_score"]
            best_bowling = player["best_bowling"]
            outputs.append([name, birthday, batting, bowling, description, career, matches, runs, wickets, top_score, best_bowling])
        res = outputs
    elif flags[5] == 1 and meassure != None:
        print('wickets')
        query_body = queries.field_value_condition_q(phrase, 'wickets', num, meassure)
        res = client.search(index=INDEX, body=query_body)
        resl = res['hits']['hits']
        print(resl)
        outputs = []
        for hit in resl:
            player = hit['_source']
            name = player["name"]
            birthday = player["birthday"]
            batting = player["batting"]
            bowling = player["bowling"]
            description = player["description"] 
            career = player["career"]
            matches = player["matches"]
            runs = player["runs"]
            wickets = player["wickets"] 
            top_score = player["top_score"]
            best_bowling = player["best_bowling"]
            outputs.append([name, birthday, batting, bowling, description, career, matches, runs, wickets, top_score, best_bowling])
        res = outputs
    else:
        print('searching no special')
        query_body = queries.agg_multi_match_q(phrase)
        res = client.search(index=INDEX, body=query_body)
        resl = res['hits']['hits']
        outputs = []
        for hit in resl:
            player = hit['_source']
            name = player["name"]
            birthday = player["birthday"]
            batting = player["batting"]
            bowling = player["bowling"]
            description = player["description"] 
            career = player["career"]
            matches = player["matches"]
            runs = player["runs"]
            wickets = player["wickets"] 
            top_score = player["top_score"]
            best_bowling = player["best_bowling"]
            outputs.append([name, birthday, batting, bowling, description, career, matches, runs, wickets, top_score, best_bowling])
        res = outputs

    return res