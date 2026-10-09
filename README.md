# Projet Python Système : Affichage des répertoires + Moniteur CPU
Application Python (Tkinter) permettant d'explorer l'arborescence d'un répertoire,
d'afficher les informations détaillées d'un fichier ou dossier sélectionné, et de
suivre en temps réel la performance du CPU.

**Auteur :** Jean-Christophe Serrano

**Date :** 21.08.2026

## Fonctionnalités

- **Arborescence** : parcours récursif d'un répertoire choisi via une boîte de
  dialogue, affiché dans un `Treeview`.
- **Informations** : en sélectionnant un fichier ou un dossier, affichage de :
  - son nom
  - son chemin complet
  - son type (extension ou "Dossier")
  - sa taille (en octets, ou nombre d'éléments pour un dossier)
  - sa date de dernière modification
  - ses permissions (lecture / écriture / exécution)
- **Moniteur CPU** (*Project*) : suivi en temps réel de l'utilisation du
  processeur (pourcentage global, fréquence, graphique sur 60 secondes,
  utilisation par cœur).

## Prérequis

- Python 3.9 ou supérieur
- [psutil] pour le moniteur CPU :

```bash
pip install psutil
```

## Installation

```bash
git clone https://github.com/Jean1197/ProjetDev_Affichage_des_repertoires_JCS
```

## Utilisation

1. Menu **File > display directory** pour choisir un répertoire à explorer.
2. Cliquer sur un élément de l'arborescence pour voir ses informations.
3. Le moniteur CPU (à droite) se met à jour automatiquement toutes les secondes.

## Structure du projet

.

|__ main.py # Script principal

|__ README.md

## Notes

- Le module de monitoring CPU (partie commentée `AJOUT`) a été développé avec
  l'aide de Claude (Anthropic).
- La récursion sur de très gros répertoires peut prendre du temps.
