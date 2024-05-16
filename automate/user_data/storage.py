import json
import os

def vault(user_info):
    #user_info is an array of user defined jobs for search
    if  os.path.isfile('/automate/user_data/user_entry.json'):
        with open('user_entry.json', 'w', encoding='utf-8') as user_jobs:
            # user entered job tags for search is now stored 
            for i in user_info:
                user_jobs.json.dumps(dict({"Job_Type":i,
                                            "ID": len(i)}))
    else:
        with open('user_entry.json', 'x', encoding='utf-8') as user_jobs:
            # user entered job tags for search is now stored 
            for i in user_info:
                user_jobs.json.dumps(dict({"Job_Type":i,
                                            "ID": len(i)})) 

