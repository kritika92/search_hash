import os
import re
from directory_to_list import directory_to_list 
from prefix_search import prefix_searching

dirfilepath=input('type the filepath if the directory: ')
dir_to_list=directory_to_list(dirfilepath)
dir_to_list.setprefixes()
myprefix=dir_to_list.get_myprefix()

file_list=dir_to_list.get_file_list()
pre_search=prefix_searching(myprefix)
pre_search.make_hash()
a=[]
a.append('a')
a.append('As')
pre_search.search_prefixes(a)
