from user_data import storage

Example = ["Handyman", "Electrician", "Plumper", "TV Mounting", "Electronics Repair"]

# type of jobs that should be picked and then replied to
def job_type_search():
    user_perference = []
    while True:
        f"Examples of Jobs: {Example[0], Example[1], Example[2], Example[3], Example[4]}"  
        user_suggest = input("What job are you interested in finding? ") 
        if user_suggest == 'Hault':
            break
        print('Enter Hault to start search process')
        user_perference.append(user_suggest)
        # storage function to save those data enteries
    copy_ = user_perference
    storage.vault(copy_)
    return user_perference
        