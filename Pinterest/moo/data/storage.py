"""
Storage interface
"""

import time

class Storage(object):
 
   def __init__(self):
      # initialize our storage, data is a placeholder
      self.data = {}

      # for demo
      self.data['created'] = time.ctime()

   def insert(self,name,value):
      print "---> insert:",name,value
      try:
         self.data[name] = value
         return "added"
      except:
         return "error: data not added"

   def remove(self,name):
      print "---> remove:",name

   def names(self):
      print "---> names:"
      for k in self.data.iterkeys():
        print 'key:',k

   def find(self,name):
      print "---> storage.find:",name
      if name in self.data:
         rtn = self.data[name]
         print "---> storage.find: got value",rtn
         return rtn
      else:
         return None
