#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
          self.value = ""
          print("The value must be a string.")
        else:
            self.value = value
        
    def __str__(self):
        return self.value
    
    def is_sentence(self):
      return self.value.endswith('.')
    
    def is_question(self):
      return self.value.endswith('?')
    
    def is_exclamation(self):
      return self.value.endswith('!')
    
    def ends_with_period(self):
        if not self.value:
          return False
        return self.value.endswith('.')
    
    def ends_with_question_mark(self):
        if not self.value:
          return False
        return self.value.endswith('?')
  
    def ends_with_exclamation_mark(self):
        if not self.value:
          return False
        return self.value.endswith('!')
    
    def count_sentences(self):
        if not self.value:
            return 0
      #splitting sentences based on the end mark
        sentences = re.split(r'[.?!]', self.value)
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)
    pass
