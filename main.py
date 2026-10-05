# Projet Python Système : Affichage des répertoires + Moniteur CPU
# Jean-Christophe Serrano
# 21.08.2026

import tkinter as tk
from tkinter import ttk # pour le treeview
from tkinter import *
from tkinter import filedialog # boite dialogue pour chercher un répertoire
from pathlib import Path # fonctions de répertoire
from datetime import datetime

node_paths = {} #garder les chemins complets

def display_file_info(event):
    selected_nodes = tree.selection() #fichier sélectionné
    if not selected_nodes:
        return

    file_path = node_paths[selected_nodes[0]]
    if not file_path.exists():
        return

    file_info = file_path.stat()

    # Formatage de la date de modification
    mod_time = datetime.fromtimestamp(file_info.st_mtime).strftime("%d/%m/%Y %H:%M:%S")

    # Détermination des permissions (lecture/écriture/exécution)
    mode = file_info.st_mode
    perms = f"{'r' if mode & 0o400 else '-'}{'w' if mode & 0o200 else '-'}{'x' if mode & 0o100 else '-'}"

    # Adaptation des valeurs selon qu'il s'agit d'un dossier ou d'un fichier
    if file_path.is_dir():
        file_type = "Dossier"
        # Calcule le nombre d'éléments contenus dans le répertoire
        try:
            item_count = len(list(file_path.iterdir()))
            size_display = f"{item_count} élément(s)"
        except PermissionError:
            size_display = "Accès refusé"
    else:
        file_type = file_path.suffix or "Fichier sans extension"
        size_display = f"{file_info.st_size} octets"

    # Liste d'associations (champ Entry, valeur à insérer)
    fields_to_update = [
        (info_entry1, file_path.name or str(file_path)),
        (info_entry2, str(file_path.resolve())),
        (info_entry3, file_type),
        (info_entry4, size_display),
        (info_entry5, mod_time),
        (info_entry6, perms)
    ]

    # Mise à jour de chaque zone de texte
    for entry, value in fields_to_update:
        entry.delete(0, tk.END)
        entry.insert(0, value)

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


# ======================================================================
# AJOUT : moniteur CPU dans project_frame (pip install psutil) aidé par l'IA (claude)
# ======================================================================
import psutil

class CpuMonitorFrame(ttk.Frame):
    INTERVALLE_MS = 1000   # rafraîchissement (ms)
    HISTORIQUE = 60        # nombre de points du graphique
    HAUTEUR = 100          # hauteur du graphique

    def __init__(self, parent):
        super().__init__(parent, padding=10)
        self.historique = [0.0] * self.HISTORIQUE

        # Pourcentage global + infos
        self.lbl_total = ttk.Label(self, text="CPU : 0 %", font=("Segoe UI", 20, "bold"))
        self.lbl_total.pack(anchor="w")
        self.lbl_infos = ttk.Label(self, text="")
        self.lbl_infos.pack(anchor="w", pady=(0, 8))

        # Graphique (s'adapte à la largeur disponible)
        self.canvas = tk.Canvas(self, height=self.HAUTEUR, bg="#111", highlightthickness=1, highlightbackground="#444")
        self.canvas.pack(fill="x")

        # Barres par cœur (2 colonnes pour gagner de la place)
        ttk.Label(self, text="Utilisation par cœur",
                  font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(10, 2))
        zone = ttk.Frame(self)
        zone.pack(fill="x")
        self.barres, self.labels_coeurs = [], []
        nb = psutil.cpu_count(logical=True)
        par_colonne = (nb + 1) // 2
        for i in range(nb):
            ligne, col = i % par_colonne, (i // par_colonne) * 3
            ttk.Label(zone, text=f"C{i}", width=4).grid(row=ligne, column=col, sticky="w")
            barre = ttk.Progressbar(zone, length=140, maximum=100)
            barre.grid(row=ligne, column=col + 1, padx=3, pady=1)
            lbl = ttk.Label(zone, text="0 %", width=5, anchor="e")
            lbl.grid(row=ligne, column=col + 2, padx=(0, 12))
            self.barres.append(barre)
            self.labels_coeurs.append(lbl)

        psutil.cpu_percent(interval=None, percpu=True)  # amorçage de psutil
        self.after(self.INTERVALLE_MS, self.actualiser)

    def actualiser(self):
        par_coeur = psutil.cpu_percent(interval=None, percpu=True)
        total = sum(par_coeur) / len(par_coeur)

        self.lbl_total.config(text=f"CPU : {total:.1f} %")
        texte = (f"{psutil.cpu_count(logical=False)} cœurs physiques / "
                 f"{psutil.cpu_count(logical=True)} logiques")
        freq = psutil.cpu_freq()
        if freq:
            texte += f"  •  {freq.current:.0f} MHz"
        self.lbl_infos.config(text=texte)

        for barre, lbl, v in zip(self.barres, self.labels_coeurs, par_coeur):
            barre["value"] = v
            lbl.config(text=f"{v:.0f} %")

        self.historique = (self.historique + [total])[-self.HISTORIQUE:]
        self.tracer()
        self.after(self.INTERVALLE_MS, self.actualiser)

    def tracer(self):
        c = self.canvas
        c.delete("all")
        largeur = max(c.winfo_width(), 100)
        h = self.HAUTEUR
        for pct in (25, 50, 75):
            y = h - h * pct / 100
            c.create_line(0, y, largeur, y, fill="#333", dash=(2, 4))
            c.create_text(4, y - 6, text=f"{pct}%", fill="#666",
                          anchor="w", font=("Segoe UI", 7))
        pas = largeur / (self.HISTORIQUE - 1)
        pts = []
        for i, v in enumerate(self.historique):
            pts.extend((i * pas, h - h * v / 100))
        c.create_polygon(0, h, *pts, largeur, h, fill="#1b4d2e", outline="")
        c.create_line(*pts, fill="#3ddc84", width=2)


cpu_monitor = CpuMonitorFrame(project_frame)
cpu_monitor.pack(fill=BOTH, expand=True)
# ======================================================================


window.mainloop()