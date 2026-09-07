# exemple de répertoire

from pathlib import Path # librairie "système"

folder = Path(".") # définir le répertoire ("." = rép courant)
# folder = Path("c:\\")

for item in folder.iterdir(): # boucle sur les élements du rép

    if item.is_file(): # cas d'un fichier
        print(item.name)

    elif item.is_dir(): # cas d'un répertoire
        print("📁", item.name)