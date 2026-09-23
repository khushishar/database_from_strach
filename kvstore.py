import shelve
class kvstore:

    def __init__(self,db_name):
        self.db_name=db_name
        self.db= shelve.open(db_name)
    def get(self,key):
        if self.db.get(key):
            return self.db.get(key)
        else:
            return f"Key {key} is unavailable in {self.db_name}"
    def set(self,key,value):
        self.db[key]=value
        self.db.sync()
    def keys(self):
        return list(self.db.keys())
    def values (self):
        return list(self.db.values())
    def items(self):
        return list(self.db.items())
    def clear(self):
        self.db.clear()
        self.db.sync()
    def delete (self,key):
        if key in self.db:
            del self.db[key]
            self.db.sync()
    def close(self):
        self.db.close()

kv= kvstore("test.db")
kv.set("name","Khushi Sharma")
name=kv.get("niame")
print(f"Heloo my name is {name}")
