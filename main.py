from my_db import Mydb
from table import Row

def main():
    db=Mydb("My.db")
    db.create_table("Students")
    db.create_table("classes")
    students=db.get_table("Students")
    row1=Row(id=1,name="Khushi Sharma",email="Trial@gmail.com")
    row2=Row(id=2,name="Sankalp Gaur",email="Sankalp@gmail.com")
    key1=students.insert(row1)
    key2=students.insert(row2)
    query_std1=students.query(key1)
    query_std2=students.query(key2)
    print(f"Data of std1: {query_std1}")
    print(f"columns of std1: {query_std1.columns}")
    
    students.update(key1,name="Khushi")
    query_std1_updated=students.query(key1)
    print(f"updated columns of std1: {query_std1_updated.columns}")
    students.delete(key2)
    all_row=students.list_rows()
    print([row.columns for row in all_row])
if __name__=="__main__":
    main()
