import sys
import json
import tkinter as tk
from tkinter import ttk
import customtkinter

from models.item import Item
from tabs.itmes_window import itemswindow

#https://customtkinter.tomschimansky.com/documentation/widgets/frame
#https://www.w3schools.com/python/python_variables.asp
#https://docs.python.org/3/library/tkinter.html

def main():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")
    items = get_json_data()

    app = customtkinter.CTk()
    app.title("Simple POS")
    app.minsize(1200, 800)
   # Tab controls
    tabControl = ttk.Notebook(app)
    itemsTab = customtkinter.CTkFrame(tabControl)
    orderTab = customtkinter.CTkFrame(tabControl)
    customersTab = customtkinter.CTkFrame(tabControl)
    tabControl.add(itemsTab, text='Items')
    tabControl.add(orderTab, text='Orders')
    tabControl.add(customersTab, text='Customers')
    tabControl.pack(expand=1, fill="both")

    # Call the itemswindow function to populate the items tab
    itemswindow(items, itemsTab)
  

    # Run the Tkinter main loop
    app.mainloop()

def get_json_data():
    with open('data/items.json', 'r') as file:
        data = json.load(file)

    # Create Item instances from JSON data
    items = [Item(**item) for item in data]
    return items


# Define a function to handle adding to cart
def add_to_cart(item):
    print(f"Added to cart: {item.name}")

main()