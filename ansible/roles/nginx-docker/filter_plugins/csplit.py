#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {'csplit': self.a_filter}
 
    def a_filter(self, text,delim,pos):
        print text
        a_new_variable = text.split(delim,pos)
        return a_new_variable
