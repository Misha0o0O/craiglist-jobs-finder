from user_data import storage

Example = ["Handyman", "Electrician", "Plumper", "TV Mounting", "Electronics Repair"]
test_links = ['https://miami.craigslist.org/search/ggg#search=1~thumb~0~0','https://miami.craigslist.org/search/cpg#search=1~thumb~0~0']

def adding_links():
    while True:
        try:    
            links = input("Enter Job Message Board Link: ")
            if adding_links := re.search(r'https://\w+\.[org|com|gov].+', links):
                test_links.append(adding_links.group(0))
            print("Ctrl-D to Hault Prompt")
        except EOFError:
            break

# type of jobs that should be picked and then replied to
def job_type_search():
    user_perference = []

    # checks for user submitted links to be search
    adding_links()
    while True:
        print(f"Examples of Jobs: {Example[0], Example[1], Example[2], Example[3], Example[4]}")  
        user_suggest = input("What job are you interested in finding? ") 
        if user_suggest == 'Hault':
            break
        print('Enter Hault to start search process')
        user_perference.append(user_suggest)
        # storage function to save those data enteries
    copy_ = user_perference
    storage.vault(copy_)
    return user_perference, test_links
        