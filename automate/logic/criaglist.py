from bs4 import BeautifulSoup
#Beautiful Soup for webpage data extraction 


def search_page(data):
    #links posted by users for in-search of workers
    posted_links = []
    full_title = ''
    papel_datos = BeautifulSoup(data, 'html.parser')
    posted_links = papel_datos.find_all('a')
    return posted_links
    
