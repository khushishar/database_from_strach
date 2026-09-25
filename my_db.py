from kvstore import Kvstore
from table import Table

class Mydb:
    def __init__(self,dbname):
        self.kvstore=Kvstore(dbname)
        self.table={}
    def create_table(self,name):
        self.table[name]=Table(name,self.kvstore)
        print(f"Table {name} created")

    def get_table(self,name):
        return self.table.get(name)
    def close(self):
        self.kvstore.close()