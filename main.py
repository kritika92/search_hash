import os
import re
import directory_to_list from directory_to_list
import prefix_searching from prefix_search

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
