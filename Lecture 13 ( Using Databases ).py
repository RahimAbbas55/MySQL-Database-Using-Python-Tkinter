from tkinter import *
from PIL import ImageTk , Image
import sqlite3

root = Tk()
root.title( "----Lecture 13----")
root.geometry("450x450")

#Databases

#Creat a database or connect to one
connection = sqlite3.connect ('Address_book.db')
#Create a cursor to operate with database
cursor = connection.cursor()
#Create table

# cursor.execute("""CREATE TABLE addresses(
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     state text,
#     zipcode integer)
#     """)

#Create Text Boxes
f_name = Entry ( root , width= 30)
f_name.grid ( row = 0 , column = 1 , padx = 20 , pady=(10,0))

l_name = Entry ( root , width= 30)
l_name.grid ( row = 1 , column = 1 , padx = 20)

address = Entry ( root , width= 30)
address.grid ( row = 2 , column = 1 , padx = 20)

city = Entry ( root , width= 30)
city.grid ( row = 3 , column = 1 , padx = 20)

state = Entry ( root , width= 30)
state.grid ( row = 4 , column = 1 , padx = 20)

ZipC = Entry ( root , width= 30)
ZipC.grid ( row = 5 , column = 1 , padx = 20)

delete_box = Entry ( root , width = 30)
delete_box.grid(row = 9 , column = 1 , pady = 5)

#Create text box labels

f_name_label = Label ( root , text = "First Name:").grid( row = 0 , column = 0 ,pady=(10,0))
l_name_label = Label ( root , text = "Last Name:").grid( row = 1 , column = 0)
adress_label = Label ( root , text = "Address:").grid( row = 2 , column = 0)
city_label = Label ( root , text = "City:").grid( row = 3 , column = 0)
state_label = Label ( root , text = "State:").grid( row = 4 , column = 0)
zipcode_label = Label ( root , text = "Zip Code:").grid( row = 5 , column = 0)
delete_box_label = Label ( root , text = "Delete ID:").grid ( row = 9 ,  column = 0 , pady = 5)

#Create function to delete

def update():
    connection = sqlite3.connect('Address_book.db')
    cursor = connection.cursor()

    id = delete_box.get()
    cursor.execute("""UPDATE addresses SET 
        first_name = :first ,
        last_name = :last ,
        address = :address ,
        city = :city , 
        state = :state ,
        zipcode = :zipcode
        
        WHERE oid  = :oid""" ,

        {
            'first' : f_name_editor.get() ,
            'last' : l_name_editor.get() ,
            'address' : address_editor.get() ,
            'city' : city_editor.get() ,
            'state' : state_editor.get() ,
            'zipcode' : ZipC_editor.get() ,
            'oid' : id

        }
        )

    connection.commit()
    connection.close()
    editor.destroy()

def delete():
    connection = sqlite3.connect('Address_book.db')
    cursor = connection.cursor()
    #delete_id = delete_box.get()
    cursor.execute("DELETE FROM addresses WHERE oid= " + delete_box.get() )


    connection.commit()
    connection.close()

#Create submit button & submit function
def submit():
    connection = sqlite3.connect('Address_book.db')
    cursor = connection.cursor()

    #Insert into table
    cursor.execute("INSERT INTO addresses VALUES (:f_name , :l_name , :address , :city , :state , :ZipC)" ,
            {
                'f_name' : f_name.get() ,
                'l_name' : l_name.get() ,
                'address' : address.get() ,
                'city' : city.get() ,
                'state' : state.get() ,
                'ZipC' : ZipC.get()
            })

    connection.commit()
    connection.close()

    #Clearing the fields after pressing submit
    f_name.delete(0 ,END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    ZipC.delete(0, END)

def query():

    global info
    info = Tk()
    info.title("All Records:")
    info.geometry("400x400")
    connection = sqlite3.connect('Address_book.db')
    cursor = connection.cursor()

    #To query the databse:
    cursor.execute("SELECT *,oid FROM addresses")
    records = cursor.fetchall()       #fetch all recordds in the database
    p = ""
    for record in records:
        p += str(record) + "\n"

    query_label = Label ( info , text = p).grid( row = 12 , column = 0 , columnspan = 2 )


    connection.commit()
    connection.close()

#Edit function to update a record
def edit():
    global editor
    editor = Tk()
    editor.title("----Edit Record----")
    editor.geometry("300x300")

    connection = sqlite3.connect('Address_book.db')
    cursor = connection.cursor()

    id = delete_box.get()
    # To query the databse:
    cursor.execute("SELECT *,oid FROM addresses WHERE oid=" + id)
    records = cursor.fetchall()  # fetch all records in the database

    p = ""
    for record in records:
        p += str(record) + "\n"

    #Create global variables

    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global ZipC_editor
    # Create Text Boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)

    ZipC_editor = Entry(editor, width=30)
    ZipC_editor.grid(row=5, column=1, padx=20)

    # delete_box = Entry(root, width=30)
    # delete_box.grid(row=9, column=1, pady=5)

    # Create text box labels

    f_name_label_editor = Label(editor, text="First Name:").grid(row=0, column=0, pady=(10, 0))
    l_name_label_editor = Label(editor, text="Last Name:").grid(row=1, column=0)
    adress_label_editor = Label(editor, text="Address:").grid(row=2, column=0)
    city_label_editor = Label(editor, text="City:").grid(row=3, column=0)
    state_label_editor = Label(editor, text="State:").grid(row=4, column=0)
    zipcode_label_editor = Label(editor, text="Zip Code:").grid(row=5, column=0)

    save_button = Button(editor, text="Save Record", command=update).grid(row=6, column=0, columnspan=2, pady=10,padx=10, ipadx=145)

    # Loop through results
    for record in records:
        f_name_editor.insert( 0 , record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        ZipC_editor.insert(0, record[5])









submit_button = Button ( root , text = "Add Credentials to Database." , command= submit).grid ( row = 6 , column = 0 ,columnspan= 2, pady =10 , padx =10 , ipadx = 100)

#Create a query button
query_button = Button( root , text = "Show Records" , command = query).grid( row = 7 , column = 0 , columnspan = 2 , pady = 10 , padx = 10 , ipadx = 137)

#Create a delete button

delete_button = Button( root , text = "Delete Records" , command = delete).grid( row = 10 , column = 0 , columnspan = 2 , pady = 10 , padx = 10 , ipadx = 135)

#Create update buttone

update_button = Button( root , text = "Edit Record" , command = edit).grid( row = 11   , column = 0 , columnspan = 2 , pady = 10 , padx = 10 , ipadx = 145)


#commit changes
connection.commit()
#End connection
connection.close()

root.mainloop()