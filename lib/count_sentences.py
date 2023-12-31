#!/usr/bin/env python3

class MyString:
  
  def __init__(self, value=''):
      self._value = None
      self.value = value

  @property
  def value(self):
      return self._value

  @value.setter
  def value(self, val):
      if not isinstance(val, str):
          print(f'The value must be a string.')
      self._value = val
  
  def is_sentence(self):
      return self._value.endswith('.')
  
  def is_question(self):
      return self._value.endswith('?')
  
  def is_exclamation(self):
      return self._value.endswith('!')
  
  def count_sentences(self):
      sentence_enders = {'.', '!', '?'}
      count = 0
      words = self._value.split()
        
      for word in words:
        if any(word.endswith(char) for char in sentence_enders):
          count += 1

      return count