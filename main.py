# Projet Python Système : Affichage des répertoires + autre
# Jean-Christophe Serrano
# 21.08.2026

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from pathlib import Path
from datetime import datetime

node_paths = {} #garder les chemins complets

def display_file_info(event):
    selected_nodes = tree.selection() #fichier sélectionné
    if not selected_nodes:
        return

    file_path = node_paths[selected_nodes[0]]
    if not file_path.is_file():
        return

    file_info = file_path.stat()

    # Formatage de la date de modification
    mod_time = datetime.fromtimestamp(file_info.st_mtime).strftime("%d/%m/%Y %H:%M:%S")

    # Détermination des permissions (lecture/écriture/exécution)
    mode = file_info.st_mode
    perms = f"{'r' if mode & 0o400 else '-'}{'w' if mode & 0o200 else '-'}{'x' if mode & 0o100 else '-'}"

    # Liste d'associations (champ Entry, valeur à insérer)
    fields_to_update = [
        (info_entry1, file_path.name),
        (info_entry2, str(file_path.resolve())),
        (info_entry3, file_path.suffix or "Fichier sans extension"),
        (info_entry4, f"{file_info.st_size} octets"),
        (info_entry5, mod_time),
        (info_entry6, perms)
    ]

    # Mise à jour de chaque zone de texte
    for entry, value in fields_to_update:
        entry.delete(0, tk.END)
        entry.insert(0, value)

# afficher un répertoire

def display_directory():
    tree.delete(*tree.get_children()) # vider le treeview
    node_paths.clear()
    root_folder = Path(filedialog.askdirectory()) # demander un répertoire

    # insérer le noeud racine (déjà ouvert)
    root_node = tree.insert("","end", text=f"📁 {root_folder.resolve()}",open=True )
    # garder l'info du chemin complet
    node_paths[root_node] = root_folder

    # appeler la recherche des noeuds enfants
    populate_tree(tree, root_node, root_folder)

    # afficher le tableau des node
    for node, path in node_paths.items():
        print(node, ":", path)

# recherche des noeuds enfants (récursif)
def populate_tree(tree, parent, folder):
    # pour tous les noeuds enfants du folder
    for item in folder.iterdir():
        item_name = f"📁 {item.name}" if item.is_dir() else f"🗎 {item.name}"
        node = tree.insert(parent, "end", text=item_name)
        node_paths[node] = item # garder l'info du chemin complet
        if item.is_dir():
            # cas d'un répertoire, rappeler les enfants de l'enfant (peut être long)
            populate_tree(tree,node,item)

window = tk.Tk()

window.title("File Explorer JCS")
window.geometry("1600x800")
window.configure(bg="#F0F0F0")

menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=False) # menu non détachable
file_menu.add_command(label="display directory", command=display_directory)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=window.destroy)
menu_bar.add_cascade(label="File", menu=file_menu) #ajouter File au menu
window.config(menu=menu_bar)

maintree_frame = LabelFrame(window)
maintree_frame.grid(row=0, column=0) # placement s'étire dans toutes direction
maintree_frame.rowconfigure(0, weight=1) # ligne du treeview
maintree_frame.columnconfigure(0, weight=1) # première colonne de la frame
style = ttk.Style() #pour mettre un Style au ttkvieux
maintree_frame.pack(side=LEFT, fill=BOTH, pady=20, padx=10)

tree_frame = LabelFrame(maintree_frame, text="Arborescence", width=500)
tree_frame.grid_propagate(False) # placement s'étire dans toutes direction
tree_frame.rowconfigure(0, weight=1) # ligne du treeview
tree_frame.columnconfigure(0, weight=1) # première colonne de la frame
style = ttk.Style() #pour mettre un Style au ttkvieux
style.configure(
    "Treeview",
    font=("Arial", 12),
    rowheight=28,
    #fieldbackground="lightgreen",
)
tree_frame.pack(side=LEFT, expand=True, fill=BOTH)

maininfo_frame = LabelFrame(window)
maininfo_frame.pack(side=LEFT, fill=BOTH, pady=20, padx=10)

info_frame = LabelFrame(maininfo_frame, text="Informations")
info_frame.rowconfigure(0, weight=1) # ligne du treeview
info_frame.columnconfigure(0, weight=1) # première colonne de la frame
info_frame.pack(side=LEFT, expand=True, fill=BOTH)

mainproject_frame = LabelFrame(window)
mainproject_frame.pack(side=LEFT, expand=True, fill=BOTH, pady=20, padx=10)

project_frame = LabelFrame(mainproject_frame, text="Project")
project_frame.pack(side=LEFT, expand=True, fill=BOTH)

tree = ttk.Treeview(tree_frame)
tree.grid(row=0, column=0, sticky="nsew") # placement, s'étire partout
# Quand on sélectionne un fichier, on appelle display_file_info
tree.bind("<<TreeviewSelect>>", display_file_info)

info_name = ttk.Label(info_frame, text="Nom:")
info_name.pack(anchor="w", padx=5, pady=10)
info_entry1 = tk.Entry(info_frame, width=45)
info_entry1.pack(anchor="w", padx=8)
info_path = tk.Label(info_frame, text="Chemin:")
info_path.pack(anchor="w", padx=5, pady=10)
info_entry2 = tk.Entry(info_frame, width=45)
info_entry2.pack(anchor="w", padx=8)
info_type = ttk.Label(info_frame, text="Type:")
info_type.pack(anchor="w", padx=5, pady=10)
info_entry3 = tk.Entry(info_frame, width=45)
info_entry3.pack(anchor="w", padx=8)
info_size = ttk.Label(info_frame, text="Size:")
info_size.pack(anchor="w", padx=5, pady=10)
info_entry4 = tk.Entry(info_frame, width=45)
info_entry4.pack(anchor="w", padx=8)
info_modified = ttk.Label(info_frame, text="Modifié le:")
info_modified.pack(anchor="w", padx=5, pady=10)
info_entry5 = tk.Entry(info_frame, width=45)
info_entry5.pack(anchor="w", padx=8)
info_permissions = ttk.Label(info_frame, text="Permissions:")
info_permissions.pack(anchor="w", padx=5, pady=10)
info_entry6 = tk.Entry(info_frame, width=45)
info_entry6.pack(anchor="w", padx=8)

window.mainloop()