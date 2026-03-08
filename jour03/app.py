import tkinter as tk
from tkinter import ttk
from product import Product
from category import Category
import csv
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Quit Button
def quit_app():
    plt.close("all")
    window.destroy()

# Database instances
product_manager = Product()
category_manager = Category()

# Window
window = tk.Tk()
window.title("Stock Management")
window.geometry("900x600")
window.protocol("WM_DELETE_WINDOW", quit_app)

# Table
table = ttk.Treeview(window,
    columns=("id", "name", "description", "price", "quantity", "category"),
    show="headings"
)
for column in ["id", "name", "description", "price", "quantity", "category"]:
    table.heading(column, text=column)
table.column("id", width=40)                                          
table.column("name", width=150)
table.column("description", width=200)
table.column("price", width=80)
table.column("quantity", width=80)
table.column("category", width=120)
table.pack(fill="both", expand=True, padx=10, pady=10)

# Table Refresh
def refresh():
    for item in table.get_children():
        table.delete(item)
    products = product_manager.read()
    for item in products:
        table.insert("", "end", values=item)

# Input Zone
frame = tk.Frame(window)
frame.pack(pady=10)

label_name = tk.Label(frame, text="Name :")
entry_name = tk.Entry(frame)
label_description = tk.Label(frame, text="Description :")
entry_description = tk.Entry(frame)
label_price = tk.Label(frame, text="Price :")
entry_price = tk.Entry(frame)
label_quantity = tk.Label(frame, text="Quantity :")
entry_quantity = tk.Entry(frame)
label_category = tk.Label(frame, text="Category ID :")
entry_category = tk.Entry(frame)

label_name.grid(row=0, column=0, padx=5, pady=3, sticky="e")
entry_name.grid(row=0, column=1, padx=5, pady=3)
label_description.grid(row=1, column=0, padx=5, pady=3, sticky="e")
entry_description.grid(row=1, column=1, padx=5, pady=3)
label_price.grid(row=2, column=0, padx=5, pady=3, sticky="e")
entry_price.grid(row=2, column=1, padx=5, pady=3)
label_quantity.grid(row=3, column=0, padx=5, pady=3, sticky="e")
entry_quantity.grid(row=3, column=1, padx=5, pady=3)
label_category.grid(row=4, column=0, padx=5, pady=3, sticky="e")
entry_category.grid(row=4, column=1, padx=5, pady=3)

# Add function
def add_product():
    name = entry_name.get()
    description = entry_description.get()
    price = entry_price.get()
    quantity = entry_quantity.get()
    category = entry_category.get()
    product_manager.create(name, description, price, quantity, category)
    refresh()

# Delete function
def delete_product():
    selection = table.selection()
    if selection:
        values = table.item(selection[0])["values"]
        product_id = values[0]  # First field is the ID 
        product_manager.delete(product_id)
        refresh()

# Modify function
def modify_product():
    selection = table.selection()
    if selection:
        values = table.item(selection[0])["values"]
        product_id = values[0]
        name = entry_name.get()
        description = entry_description.get()
        price = entry_price.get()
        quantity = entry_quantity.get()
        category = entry_category.get()
        product_manager.update(product_id, name, description, price, quantity, category)
        refresh()

# Filter function
def filter_by_category():
    value = combo.get()
    for item in table.get_children():
        table.delete(item)
    if value:
        products = product_manager.filter(value)
    else:
        products = product_manager.read()
    for item in products:
        table.insert("", "end", values=item)

# Filter zone
filter_frame = tk.Frame(window)
filter_frame.pack(pady=5)
categories = category_manager.read()
category_names = []
for cat in categories:
    category_names.append(cat[1])
combo = ttk.Combobox(filter_frame, values=category_names)
combo.pack(side="left", padx=5)
btn_filter = tk.Button(filter_frame, text="Filter",command=filter_by_category)
btn_filter.pack(side="left", padx=5)
btn_show_all = tk.Button(filter_frame, text="Show All", command=refresh)
btn_show_all.pack(side="left", padx=5)

# Export function
def export_csv():
    products = product_manager.read()
    with open("products.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["ID","Name","Description","Price","Quantity","Category"])
        writer.writerows(products)

# Charts function
def show_charts():
    products = product_manager.read()
    names = []
    prices = []
    quantities = []
    category_count = {}
    
    for p in products:
        names.append(p[1])
        prices.append(p[3])
        quantities.append(p[4])
        category_count[p[5]] = category_count.get(p[5], 0) + 1
        
    chart_window = tk.Toplevel(window)
    chart_window.title("Charts")
    chart_window.geometry("800x500")
    
    notebook = ttk.Notebook(chart_window)
    notebook.pack(fill="both", expand=True)
    
    # Tab 1 : bar chart quantities
    tab1 = tk.Frame(notebook)
    notebook.add(tab1, text="Quantities")
    fig1, ax1 = plt.subplots()
    ax1.bar(names, quantities)
    ax1.set_title("Stock Quantity by Product")
    plt.xticks(rotation=45, ha="right")
    fig1.tight_layout()
    canva = FigureCanvasTkAgg(fig1, tab1)
    canva.draw()
    canva.get_tk_widget().pack()
    
    # Tab 2 : bar chart prices
    tab2 = tk.Frame(notebook)
    notebook.add(tab2, text="Prices")
    fig2, ax2 = plt.subplots()
    ax2.bar(names, prices)
    ax2.set_title("Price by Product")
    plt.xticks(rotation=45, ha="right")
    fig2.tight_layout()
    canva = FigureCanvasTkAgg(fig2, tab2)
    canva.draw()
    canva.get_tk_widget().pack()
    
    # Tab 3 : bar chart categorie
    tab3 = tk.Frame(notebook)
    notebook.add(tab3, text="Category")
    fig3, ax3 = plt.subplots()
    ax3.pie(list(category_count.values()), labels=list(category_count.keys()))
    ax3.set_title("Product by Category")
    canva = FigureCanvasTkAgg(fig3, tab3)
    canva.draw()
    canva.get_tk_widget().pack()
    
# CRUD Buttons
btn_frame = tk.Frame(window)
btn_frame.pack(pady=5)

btn_add = tk.Button(btn_frame, text="Add", command=add_product)
btn_delete = tk.Button(btn_frame, text="Delete",command=delete_product)
btn_modify = tk.Button(btn_frame, text="Modify",command=modify_product)

btn_add.pack(side="left", padx=5)
btn_delete.pack(side="left", padx=5)
btn_modify.pack(side="left", padx=5)

# Utility Buttons
util_frame = tk.Frame(window)
util_frame.pack(pady=5)

btn_export_csv = tk.Button(util_frame, text="Export",command=export_csv)
btn_show_charts = tk.Button(util_frame, text="Charts",command=show_charts)
btn_quit = tk.Button(util_frame, text="Quit", command=quit_app)

btn_export_csv.pack(side="left", padx=5)
btn_show_charts.pack(side="left", padx=5)
btn_quit.pack(side="left", padx=5)


# Load products on start
refresh()

# Start app
window.mainloop()