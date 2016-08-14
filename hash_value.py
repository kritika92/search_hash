import os
import re

class value:
    def __init__(self,word,word_index):
        self.__is_word=None
        self.__is_end=True
        self.__key_list=[]
        self.__word=None
        if(word_index==len(word)-1):
            self.set_is_word(True)
        else:
            self.set_is_word(False)
        if(self.get_is_word()):
            self.set_word(word)
            
        
    def set_key_list(self,key):
        self.__key_list.append(key)
        self.set_is_end(False)
    def get_key_list(self):
        return self.__key_list
    def set_is_word(self,status):
        self._is_word=status
    def get_is_word(self):
        return self.__is_word
    def set_word(self,word):
        self.__word=word
    def get_word(self):
        return self.__word
    def set_is_end(self,status):
        self.__is_end=status
    def get_is_end(self):
        return self.__is_end
    
