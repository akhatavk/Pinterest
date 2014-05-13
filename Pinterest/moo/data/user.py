'''
Created on May 11, 2014

@author: akshay
'''

from datetime import datetime
from couchdb import Server
from couchdb.mapping import Document, TextField, IntegerField, DateTimeField,ListField,DictField,Mapping
import couchdb
try:
    server = Server()
    user_db = server.create('user')
except couchdb.PreconditionFailed:
    user_db = server['user']    

class User(Document):
      user_name = TextField()
      
      password=TextField()
     
      name = TextField()
     
      boards=ListField(dict(Mapping.build(
         board_id = TextField(),
         board_name=TextField()        
     )))
 

      def create_user(self,user_name,name,password):
          print 'IN Create User'
          if user_name not in user_db:
             user=User(id=user_name,user_name=user_name,name=name,password=password)
             user.store(user_db)
             return user_name
          else:
             return None
            
      def auth_user(self,user_name,password):
          if user_name not in user_db:
              return None
          else:
              user = User.load(user_db, user_name)
              if user.password==password:
                 return user_name
              else:
                 return None
              
      def getBoards(self,user_name):
          user = User.load(user_db, user_name)
          return user.boards         
      
      def verify_token(self,token):
          if token in user_db:
              return token
          else:
             return None  
         
      def dupCheckBoard(self,user_id,board_name):
          user = User.load(user_db,user_id)
          if search(user.boards,'board_name',board_name):
             return False
          else:
             return True 
          
           
'''board_name
returns a dictonary object in the list where 
attribute_name is the attribute name of dictonary and 
searh_value is the value to search for for that attribute 
'''
def search(list_name,attribute_name,search_value):
    return (element for element in list_name if element[attribute_name] == search_value).next()



'''
user = User.load(db, 'akshay')

search(user.boards,'board_name','Amol Board1').board_name='Amol Board3'

# user.boards[user.boards.index(dict(board_name='Amol Board'))].board_name='Amol Board1'



comment1=[dict(creator='Sumant1',comment_text='This is a comment')]
user = User(id='akshay',user_name='akshay1',first_name='Akshay1',boards=[dict(board_id='1',board_name='board1',pins=[dict(pin_id=1,pin_name='pin1',pin_url='url1',comments=comment1)])])

user.store(db)
'''
     
     