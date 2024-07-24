import tkinter as tk
from tkinter import messagebox
import customtkinter
from models.item import Item

cart = []

def add_to_cart(item):
    # Update cart or display a message
    cost = item.price
    quantity = 1 
    for cart_item in cart_items:
        if cart_item.item_id == item.item_id:
            cart_item.quantity += 1
            cart_item.price = cost * quantity
            update_cart_display()
            return

    new_item = Item(item.item_id , item.name, cost, item.description, quantity)
    cart_items.append(new_item)
    update_cart_display()

def remove_from_cart(item):
    global cart_items
    # Remove the item from the cart
    cart_items = [i for i in cart_items if i.item_id != item.item_id]
    update_cart_display()

def clear_cart():
    global cart_items
    cart_items = []
    update_cart_display()

def update_cart_display():
    # Clear the cart display
    try:
        for widget in cart.winfo_children():
            widget.destroy()
    except:
         pass
    
    # Create the cart header
    customtkinter.CTkLabel(cart_frame, text="Cart", font=("Arial", 28),  text_color="white").grid(row=0, column=0, columnspan=5, pady=10, padx=10)
    
    # Create a scrollable frame for cart items
    cart = customtkinter.CTkScrollableFrame(cart_frame, width=500, height=500, fg_color="#878787")
    cart.grid(row=1, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)

    # Create column headers for cart
    cart_headers = ["ID", "Name", "Price", "Quantity", "Remove"]
    for col, cart_header in enumerate(cart_headers):
        customtkinter.CTkLabel(cart,  text_color="white", font=("Arial", 18) ,text=cart_header).grid(row=0, column=col, sticky="nsew", padx=5, pady=5)
    
    # Display each item in the cart
    for row, item in enumerate(cart_items, start=1):
        customtkinter.CTkLabel(cart, text=item.item_id, text_color="white", pady="20").grid(row=row, column=0, sticky="nsew", padx=5, pady=5)
        customtkinter.CTkLabel(cart, text=item.name, text_color="white", pady="20").grid(row=row, column=1, sticky="nsew", padx=5, pady=5)
        customtkinter.CTkLabel(cart, text=item.price, text_color="white", pady="20").grid(row=row, column=2, sticky="nsew", padx=5, pady=5)
        customtkinter.CTkLabel(cart, text=item.quantity, text_color="white", pady="20").grid(row=row, column=3, sticky="nsew", padx=5, pady=5)
        
        # Button to remove item from cart
        btn = customtkinter.CTkButton(cart, text="Remove",text_color="white" , command=lambda i=item: remove_from_cart(i))
        btn.grid(row=row, column=4, sticky="nsew", padx=5, pady=5)
    
    # Configure grid weights to allow resizing
    for col in range(5):
        cart.grid_columnconfigure(col, weight=1)
    for row in range(len(cart_items) + 1):  # Adding 1 to account for header row
        cart.grid_rowconfigure(row, weight=1)
    
    if 'cart_btns' in globals():
        for widget in cart_btns.winfo_children():
            widget.destroy()
    else:
        cart_btns = customtkinter.CTkFrame(cart_frame , fg_color="#333333")
        cart_btns.grid(row=2, column=0, columnspan=5, pady=10, sticky="ew")
    
    # Add buttons to cart_btns frame
    clear_btn = customtkinter.CTkButton(cart_btns, text="Clear", text_color="white", command=clear_cart)
    clear_btn.grid(row=0, column=0, padx=10)
    
    add_order_btn = customtkinter.CTkButton(cart_btns, text="Add Order", text_color="white")
    add_order_btn.grid(row=0, column=1, padx=10)

def itemswindow(items, itemsTab):
    global cart_frame, cart_items
    cart_items = []  # Initialize cart items list

    # Create a frame for the table
    table_frame =  customtkinter.CTkScrollableFrame(itemsTab , width=800, height=200)
    table_frame.pack(side="left", fill="both", padx=20, pady=20)

    # Create column headers
    headers = ["ID", "Name", "Price", "Quantity", "Add to Cart"]
    for col, header in enumerate(headers):
       customtkinter.CTkLabel(table_frame,fg_color="black", text_color="white" , text=header).grid(row=0, column=col, sticky="nsew")

    # Create the side frame for cart items
    cart_frame = customtkinter.CTkFrame(itemsTab , width=500)
    cart_frame.pack(side="right", fill="both")
 
        
    # Insert items into the table
    for row, item in enumerate(items, start=1):
        customtkinter.CTkLabel(table_frame, text=item.item_id, text_color="white" , pady="20").grid(row=row, column=0, sticky="nsew")
        customtkinter.CTkLabel(table_frame, text=item.name, text_color="white" , pady="20").grid(row=row, column=1, sticky="nsew")
        customtkinter.CTkLabel(table_frame, text=item.price, text_color="white", pady="20").grid(row=row, column=2, sticky="nsew")
        customtkinter.CTkLabel(table_frame, text=item.quantity, text_color="white" , pady="20").grid(row=row, column=3, sticky="nsew")
        btn = customtkinter.CTkButton(table_frame, text="Add", text_color="white" , command=lambda i=item: add_to_cart(i))
        btn.grid(row=row, column=4, sticky="nsew")

    # Configure grid weights to allow resizing
    for col in range(5):
        table_frame.grid_columnconfigure(col, weight=1)
    for row in range(len(items) + 1):
        table_frame.grid_rowconfigure(row, weight=1)