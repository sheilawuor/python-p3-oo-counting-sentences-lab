#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self.value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")
    
    def is_sentence(self):
        return self.value.endswith('.')
    
    def is_question(self):
        return self.value.endswith('?')
    
    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        if not self.value:
            return 0
        
        # Replace multiple punctuation with single punctuation
        text = self.value.replace('!!', '!').replace('...', '.')
        
        # Split on sentence-ending punctuation
        sentences = []
        for char in ['.', '!', '?']:
            text = text.replace(char, '|')
        
        # Split and filter out empty strings
        parts = [part.strip() for part in text.split('|') if part.strip()]
        
        return len(parts)
