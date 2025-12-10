import sqlite3


def create_db():
    connect=sqlite3.connect("phonebook.db")
    cursor=connect.cursor()
    
    # table for the phone book
    cursor.execute(''' create table if not exists contacts(
        id integer primary key autoincrement,
        name text not null,
        phone text not null
        
    )''')
    
    # table for notes 
    cursor.execute('''
                   create table if not exists notes(
                       id integer primary key autoincrement,
                       title text not null,
                       content text not null
                   )
       ''')
    connect.commit()
    cursor.close()
    
    
if __name__=='__main__':
    create_db()