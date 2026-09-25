import uuid
import json
class Row:
    def __init__(self,**columns):
        self.columns = columns
class Table:
    def __init__(self,name,Kvstore):
        self.name=name
        self.kvstore= Kvstore
    def insert(self,row):
        key =str(uuid.uuid4())
        self.kvstore.set(f"{self.name}:{key}",json.dumps(row.columns))
        return key
    def query(self,key):
        data=self.kvstore.get(f"{self.name}:{key}")
        if data:
            if data.startswith ("Key"):
                return None
            return Row(**json.loads(data))
        else:
            return "Not Found"
    def delete(self,key):
        self.kvstore.delete(f"{self.name}:{key}")
        print("Row deleted successfully")

    def list_rows(self):
        rows=[]
        prefix=f"{self.name}:"
        for key in self.kvstore.keys():
            if key.startswith(prefix):
                data=self.kvstore.get(key)
                if not data.startswith("Key"):
                    rows.append(Row(**json.loads(data)))
            else:
                rows.append(Row(**json.loads(data)))
        return rows
    def update(self,key,**updates):
        row=self.query(key)
        if row:
            row.columns.update(updates)
            self.kvstore.set(f"{self.name}:{key}",json.dumps(row.columns))
    def row_count(self):
        return len(self.list_rows())
    
    def clear_table(self):
        #perfix=f"{self.name}:"
        keys=self.kvstore.keys()
        for key in keys:
            self.kvstore.delete(key)
        print("Table {self.name} cleared")

