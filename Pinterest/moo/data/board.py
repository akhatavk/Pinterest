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
    board_db = server.create('board')
except couchdb.PreconditionFailed:
    board_db = server['board']    

class Board(Document):
     
         board_name = TextField()
         
         pins=ListField(DictField(Mapping.build(
         pin_id = TextField(),
         pin_name = TextField(),
         pin_url=TextField(),
         comments=ListField(DictField(Mapping.build(
         creator = TextField(),
         comment_text = TextField()
         )))
         )))
         
 
         def create_board(self,board_name,user_name):
             pass
                           
   
            
          
           
'''
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
     
     