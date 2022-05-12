from pymongo import MongoClient

class Database:
    def __init__(self):
        mydb = None
        mycol = None

    def create_db(self):
        client = MongoClient('localhost', 27017)
        self.mydb = client['faces_db']
        print("Database created........")
        self.mycol = self.mydb["human_faces"]

    def collections(self, decode_face):
        print(decode_face)
        myquery = {"decode_face": decode_face}
        for doc in self.mycol.find(myquery):
            num = 0
            if doc:
                print(doc['num'])
                num = int(doc['num']) + 1
            mydict = {"decode_face": decode_face, "num": str(num)}
            doc.insert_one(mydict)

    def read(self, decode_face):
        num = 0
        myquery = {"decode_face": decode_face}
        for doc in self.mycol.find(myquery):
            num = doc['num'] + 1
        return num

