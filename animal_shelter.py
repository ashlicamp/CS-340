from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):

    def __init__(self,username,password):
        # init to connect to mongodb without authentication
        self.client = MongoClient('mongodb://localhost:47550')
        #init connect to mongodb with authentication
        #self.client = MongoClient('mongodb://%s:%s@localhost:47550/?authMechanism=DEFAULT&authSource=AAC' % (username, password))
        self.database = self.client['AAC']

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary   
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD. 
    def read_all(self,data):
        cursor = self.database.animals.find(data,{"_id":False}) ## return a cursor which is a pointer to a list of results ( Documents )
        return cursor
    
#         if data is not None:
#             return self.database.animals.find(data,{"_id":False})
#         else:
#             print('Nothing to read because data parameter is empty')
#             return False
        
    def read(self,data):
        return self.database.animals.find_one(data) ## returns only one document as a python dictionary
    
    def update(self,ID,updateData):
        if ID is not None:
            return self.database.animals.update_one(ID,{"$set":updateData})
        else:
            print("Error: Id not found.")
            
    def delete(self,ID):
        return self.database.animals.delete_one({"_id":ID})
        
        
        
    