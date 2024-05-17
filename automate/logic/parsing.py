

def title(job_listings):
    # data is gathered but isnt structured well, parsing is need 
    # will now use a while loop and regex to sort what data is needed
    full_title = []
    for i in job_listings:
       title_prefix = i.contents
       try:
            for parse in title_prefix:
                if parse != '\n':
                  full_title.append(parse.string)    
            else:
                continue            
       except KeyError:
           continue
    return full_title  