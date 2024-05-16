import re
import data_parser
from user_data import user_search
from bs4 import BeautifulSoup
#Beautiful Soup for webpage data extraction 


# search for user perferred jobs from craiglist
user_perf = user_search.job_type_search()
# user_perf contains terms of jobs that user is in search of  


def search_page(data):
    #links posted by users for in-search of workers
    posted_links = []
    full_title = ''
    papel_datos = BeautifulSoup(data, 'html.parser')
    posted_links = papel_datos.find_all('a')
    # data is gathered but isnt structured well, parsing is need 
    # will now use a while loop and regex to sort what data is needed
    for i in posted_links:
       title_prefix = i.contents
       try:
            for parse in title_prefix:
                parse = parse.removeprefix(' <div class="title">')
                parse = parse.removesuffix("</div")
                
            else:
                continue            
       except KeyError:
           continue
      
