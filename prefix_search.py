import os
import re
from directory_to_list import directory_to_list
from hash_value import value 




class prefix_searching:
    def __init__(self,myprefix):
        self.__word_hash={}
        self.__myprefix=myprefix
    def make_hash(self):
        for word in self.__myprefix:
            self.add_key(word)
            
    def add_key(self,word):
        for letter_index in range(0,len(word)):
                key_list=[]
                word_hash=self.get_word_hash()
                if(word_hash.has_key(word[0:letter_index+1])):
                    if(letter_index+1==len(word)):
                        word_hash[word[0:letter_index+1]].set_is_word(True)
                    
                    else:
                        continue
                else:
                    if(letter_index==0):
                        word_hash[word[0:letter_index+1]]=value(word,letter_index+1)
                    else:
                        word_hash[word[0:letter_index]].set_is_end(False)
                        word_hash[word[0:letter_index]].set_key_list(word[0:letter_index+1])
                        word_hash[word[0:letter_index+1]]=value(word,letter_index+1)

        
    def get_word_hash(self):
        return self.__word_hash
    def get_prefix(self,word,prefix):
        if(self.get_word_hash()[word].get_is_end()==True):
            print('one of the prefix for '+ prefix+ ' is '+word)
            
        else:
            if(self.get_word_hash()[word].get_is_word()==True):
                print('one of the prefix for '+ prefix+ ' is '+word)
            list=[]
            list=self.get_word_hash()[word].get_key_list()
            for k in list:
                self.get_prefix(k,prefix)
        
    def search_prefixes(self,prefix_list):
        temp_list=[]
        for i in prefix_list:
            temp_list.append(i.lower())
        prefix_list=temp_list
        for word in prefix_list:
            if(self.get_word_hash().has_key(word)):
                self.get_prefix(word, word)
            else:
                print(word+' doesnot exists')
               
