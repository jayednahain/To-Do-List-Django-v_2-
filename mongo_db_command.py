"""

data base name : Student_information


"""
import pymongo
import dns

client = pymongo.MongoClient("mongodb+srv://student_detail:nahian123456@cluster0.tg5zg.mongodb.net/<student_detail>?retryWrites=true&w=majority")
db_obj = client['student_detail']
collection_obj= db_obj['information']
print(client.list_database_names())



#print(my_client.list_database_names())
