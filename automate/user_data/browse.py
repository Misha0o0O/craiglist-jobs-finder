import re
import os
from urllib import request, response

def load_page(urls):
    papel_datos = request.urlopen(urls)
    return papel_datos
            

