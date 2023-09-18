#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            raise ValueError("The value must be a string.")
        self.value = value
        
    def __str__(self):
        return self.value
    
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
      #splitting sentences based on the endmark
        sentences = re.split(r'[.?!]', self.value)
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)
    pass
