import collections
from tkinter import *
from typing import Collection
from tkinter import messagebox
import random
import json

# .........................................Password generator......................#
def generate_password():
    letters =['a', 'b', 'c', 'd', 'e', f'', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers=['0','1','2','3','4','5','6','7','8','9']
    symbols=['!','#','$',"@",'%',"^","(",")",'*',"+"]

    nr_letters=random.randint(8,10)
    nr_symbols=random.randint(2,4)
    nr_numbers=random.randint(2,4)

    password_list=[]

    for char in range(nr_letters):
        password_list.append(random.choice(letters))
    for char in range(nr_symbols):
        password_list.append(random.choice(symbols))
    for char in range(nr_numbers):
        password_list.append(random.choice(numbers))
    random.shuffle(password_list)
    password=' '.join(map(str,password_list))
    password="".join(password.split())
    password_entry.delete(0,END)
    password_entry.insert(0,password)
    




#.........................................Save Password..............................#
def save():
    

    website_text=website_entry.get()
    email_text=email_entry.get()
    password_text=password_entry.get()
    new_data={
        website_text:{
            "email":email_text,
            "password":password_text
        }
    }
    
    #message box
    if len(website_text) or len(password_text):
        is_ok=messagebox.askokcancel(title=website_text,message=f"These are the details entered:\nEmail: {email_text} \npassword: {password_text}\nDo you want to save? ")
        if is_ok:
            try:
                with open("data.json",'r') as data_file:
                    data=json.load(data_file)
                    data.update(new_data)
                    
                     
            except FileNotFoundError:
                with open("data.json",'w') as data_file:
                    json.dump(new_data,data_file,indent=4)

            else:
                data.update(new_data)
                with open("data.json",'w') as data_file:
                    json.dump(data,data_file,indent=4)
                
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)
    else:
        messagebox.showerror(title="Empty Fields",message="Kindly fill the details correctly before saving")
#---------------------------------Find passowrd-----------------------------------------#
def find_password():
    website=website_entry.get()
    try:
        with open("data.json") as data_file:
            data=json.load(data_file)
            if website in data:
                email=data[website]['email']
                password=data[website]['password']
                messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showerror(title=website,message="This entry doesn't exist")


    except FileNotFoundError:
        messagebox.showerror(title="No Password saved",message="no entry exists")
    finally:
        website_entry.delete(0,END)   





#.........................................UI Setup....................................#
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(height=200,width=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

#labels
website_label=Label(text="Website:")
website_label.grid(row=1,column=0)

email_label=Label(text="E-Mail/Username:")
email_label.grid(row=2,column=0)

password_label=Label(text="Password:")
password_label.grid(row=3,column=0)


#entries
website_entry=Entry(width=24)
website_entry.grid(row=1,column=1,columnspan=1)
website_entry.focus()

email_entry=Entry(width=42)
email_entry.insert(0,"USER1@email.com")
email_entry.grid(row=2,column=1,columnspan=2)

password_entry=Entry(width=24)
password_entry.grid(row=3,column=1)

#buttons
generate_password_button=Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3,column=2)

add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)

search=Button(text="Search ",width=15,command=find_password)
search.grid(row=1,column=2)

window.mainloop()