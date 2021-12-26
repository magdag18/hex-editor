import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.iconbitmap("hexeditor_icon.ico")
root.title("hexeditor")
root.state('zoomed')

###commands για το menu

###...    

###menu
menubar = tk.Menu(root)

show_menu = tk.Menu(menubar, tearoff = "off")
analyse_menu = tk.Menu(menubar, tearoff = "off")
more_menu = tk.Menu(menubar, tearoff = "off")

menubar.add_cascade(label = "Προβολή", menu = show_menu)
menubar.add_cascade(label = "Ανάλυση", menu = analyse_menu)
menubar.add_cascade(label = "Επιπρόσθετα", menu = more_menu)

###Προβολή(menu)
adjust_image = tk.PhotoImage(file = "adjust_image.png" ).subsample(50)
show_menu.add_command(label = "Προσαρμογή στο μήκος του παραθύρου", image=adjust_image, compound=tk.LEFT)
show_menu.add_command(label = "Bytes ανα σειρά...")

show_menu.add_separator()

show_menu.add_command(label="Επιθεωρητής δεδομένων",accelerator="Ctrl+Alt+D")
#root.bind
show_menu.add_command(label="Checksums",accelerator="Ctrl+Alt+C")
#root.bind
show_menu.add_command(label="Αποτέλεσμα αναζήτησης", accelerator="Ctrl+Alt+S")
#root.bind

show_menu.add_separator()

show_menu.add_command(label ="Επόμενο παράθυρο εργαλείων",accelerator="Alt+F7")
show_menu.add_command(label="Προηγούμενο παράθυρο εργαλείων",accelerator="Shift + Alt +F7")

show_menu.add_separator()

refresh_image = tk.PhotoImage(file="refresh_image.png").subsample(20)
show_menu.add_command(label="Ανανέωση",image=refresh_image,compound=tk.LEFT)

###Ανάλυση(menu)

statistics_image = tk.PhotoImage(file= "statistics_image.png").subsample(40)
analyse_menu.add_command(label = "Στατιστικές",image = statistics_image,compound = tk.LEFT)

analyse_menu.add_command(label = " Αθροίσματα ελέγχου...")

analyse_menu.add_command(label = " Σύγκριση δεδομένων",accelerator="Ctrl+K")
#root.bind

###Επιπρόσθετα(menu)

open_first_memory_image = tk.PhotoImage(file = "open_first_memory_image.png").subsample(10)
more_menu.add_command(label="Άνοιγμα πρωτεύουσας μνήμης...", image = open_first_memory_image, compound= tk.LEFT, accelerator="Shift+Ctrl+M")
#root.bind
more_menu.add_command(label="Άνοιγμα δίσκου...")

more_menu.add_separator()

more_menu.add_command(label = "Επιλογές...")


root.config(menu = menubar)

###κουμπιά

save = tk.PhotoImage(file = "save_image.png").subsample(15)
save_button = tk.Button(root, image=save, borderwidth= 0).grid(padx = 5, column=0, row = 0 )

open_first_memory_button = tk.Button(root, image=open_first_memory_image, borderwidth= 0).grid(padx = 5, column=1, row = 0)


###combobox

box_value = tk.StringVar()
combobox1 = ttk.Combobox(root,textvariable= box_value)
combobox1.bind("<<ComboboxSelected>>",lambda event : box_value==combobox1.get())
combobox1['values']=('8','16','24','32')    
combobox1.current(0)
combobox1.grid(row = 0,column = 3)
### box_value -> σε συνάρτηση 


root.mainloop()
