import re
import os
from urllib import request, response
import criaglist_search


main_page = ['https://miami.craigslist.org/search/ggg#search=1~thumb~0~0','https://miami.craigslist.org/search/cpg#search=1~thumb~0~0']
posted_links = []


def adding_links():
    links = input("Enter Job Message Board Link: ")
    if adding_links := re.search(r'https://\w+\.[org|com|gov].+', links):
        main_page.append(adding_links.group(0))


def search_craiglist_gigs(urls):
    # this function looks through set of links 
    for i in urls:
        papel_datos = request.urlopen(i)
        jobs_repsoned = criaglist_search.search_page(papel_datos)

               
# adding_links()
search_craiglist_gigs(main_page)

