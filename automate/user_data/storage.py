import json
import os

def vault(user_info):
    
    with open('user_entry.json', 'w', encoding='utf-8') as user_jobs:
            # user entered job tags for search is now stored 
        for i in user_info:
            user_jobs.dumps({"Job_Type":i,
                                "ID": len(i)})

