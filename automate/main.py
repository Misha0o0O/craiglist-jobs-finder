from user_data import user_search, browse
from logic import criaglist, parsing, ai


def main():
    # retriving user suggest jobs to search, also web page links user wants to check
    user_jobs_perferred, test_links = user_search.job_type_search()
    
    # test_links is an array and purpose of this program is to check each link the user proves 
    size_of_search = len(test_links)


    while i != size_of_search:
        data = browse.load_page(test_links[i])
        job_links = criaglist.search_page(data)
        posted_jobs = parsing.title(job_links)
        result = ai.job_verifer(posted_jobs, user_jobs_perferred)
