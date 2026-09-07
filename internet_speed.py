#!/usr/bin/env python3
"""
Testeur de vitesse internet - Interface Tkinter
Mesure le ping, la vitesse de téléchargement et d'envoi.

Installation requise :
    pip install speedtest-cli

Lancement :
    python3 testeur_vitesse_internet.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
import threading

try:
    import speedtest
except ImportError:
    speedtest = None


class TesteurVitesseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Testeur de vitesse internet")
        self.root.geometry("420x480")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self.test_en_cours = False
        self._construire_interface()

    # ---------- Construction de l'UI ----------
    def _construire_interface(self):
        couleur_fond = "#1e1e2e"
        couleur_carte = "#2a2a3c"
        couleur_texte = "#f0f0f5"
        couleur_accent = "#7c9eff"

        titre = tk.Label(
            self.root, text="Vitesse Internet",
            font=("Segoe UI", 20, "bold"),
            bg=couleur_fond, fg=couleur_texte
        )
        titre.pack(pady=(25, 5))

        sous_titre = tk.Label(
            self.root, text="Mesurez votre ping, débit descendant et montant",
            font=("Segoe UI", 10),
            bg=couleur_fond, fg="#a0a0b8"
        )
        sous_titre.pack(pady=(0, 20))

        # Cadre des résultats (3 cartes)
        cadre_resultats = tk.Frame(self.root, bg=couleur_fond)
        cadre_resultats.pack(pady=10)

        self.label_ping = self._creer_carte(cadre_resultats, "PING", "-- ms", couleur_carte, couleur_texte, 0)
        self.label_download = self._creer_carte(cadre_resultats, "TÉLÉCHARGEMENT", "-- Mbps", couleur_carte, couleur_texte, 1)
        self.label_upload = self._creer_carte(cadre_resultats, "ENVOI", "-- Mbps", couleur_carte, couleur_texte, 2)

        # Barre de progression
        self.barre_progression = ttk.Progressbar(
            self.root, mode="indeterminate", length=340
        )
        self.barre_progression.pack(pady=25)

        # Statut
        self.label_statut = tk.Label(
            self.root, text="Prêt à démarrer le test",
            font=("Segoe UI", 10), bg=couleur_fond, fg="#a0a0b8"
        )
        self.label_statut.pack(pady=(0, 15))

        # Bouton de lancement
        self.bouton_test = tk.Button(
            self.root, text="Lancer le test", font=("Segoe UI", 12, "bold"),
            bg=couleur_accent, fg="white", activebackground="#5f7fe0",
            relief="flat", padx=20, pady=10, cursor="hand2",
            command=self.lancer_test
        )
        self.bouton_test.pack(pady=10)

        # Nom du serveur utilisé
        self.label_serveur = tk.Label(
            self.root, text="", font=("Segoe UI", 8),
            bg=couleur_fond, fg="#6c6c86"
        )
        self.label_serveur.pack(pady=(15, 0))

    def _creer_carte(self, parent, titre, valeur_initiale, couleur_carte, couleur_texte, colonne):
        cadre = tk.Frame(parent, bg=couleur_carte, width=115, height=100)
        cadre.grid(row=0, column=colonne, padx=8)
        cadre.grid_propagate(False)

        label_titre = tk.Label(
            cadre, text=titre, font=("Segoe UI", 8, "bold"),
            bg=couleur_carte, fg="#a0a0b8"
        )
        label_titre.pack(pady=(18, 5))

        label_valeur = tk.Label(
            cadre, text=valeur_initiale, font=("Segoe UI", 14, "bold"),
            bg=couleur_carte, fg=couleur_texte
        )
        label_valeur.pack()

        return label_valeur

    # ---------- Logique du test ----------
    def lancer_test(self):
        if self.test_en_cours:
            return

        if speedtest is None:
            messagebox.showerror(
                "Module manquant",
                "Le module 'speedtest-cli' n'est pas installé.\n\n"
                "Installez-le avec :\npip install speedtest-cli"
            )
            return

        self.test_en_cours = True
        self.bouton_test.config(state="disabled", text="Test en cours...")
        self.barre_progression.start(12)
        self.label_ping.config(text="-- ms")
        self.label_download.config(text="-- Mbps")
        self.label_upload.config(text="-- Mbps")
        self.label_serveur.config(text="")

        thread = threading.Thread(target=self._executer_test, daemon=True)
        thread.start()

    def _executer_test(self):
        try:
            self._mettre_a_jour_statut("Recherche du meilleur serveur...")
            st = speedtest.Speedtest()
            st.get_best_server()

            serveur = st.results.server
            self._mettre_a_jour_statut("Test du ping...")
            ping = st.results.ping

            self._mettre_a_jour_statut("Test de téléchargement...")
            download = st.download() / 1_000_000  # bits/s -> Mbps

            self._mettre_a_jour_statut("Test d'envoi...")
            upload = st.upload() / 1_000_000  # bits/s -> Mbps

            self.root.after(0, self._afficher_resultats, ping, download, upload, serveur)

        except Exception as e:
            self.root.after(0, self._afficher_erreur, str(e))

    def _mettre_a_jour_statut(self, texte):
        self.root.after(0, lambda: self.label_statut.config(text=texte))

    def _afficher_resultats(self, ping, download, upload, serveur):
        self.label_ping.config(text=f"{ping:.0f} ms")
        self.label_download.config(text=f"{download:.1f} Mbps")
        self.label_upload.config(text=f"{upload:.1f} Mbps")
        self.label_serveur.config(
            text=f"Serveur : {serveur.get('sponsor', '?')} - {serveur.get('name', '?')}"
        )
        self.label_statut.config(text="Test terminé")
        self._reinitialiser_bouton()

    def _afficher_erreur(self, message_erreur):
        self.label_statut.config(text="Erreur pendant le test")
        messagebox.showerror("Erreur", f"Une erreur est survenue :\n{message_erreur}")
        self._reinitialiser_bouton()

    def _reinitialiser_bouton(self):
        self.barre_progression.stop()
        self.bouton_test.config(state="normal", text="Lancer le test")
        self.test_en_cours = False


if __name__ == "__main__":
    root = tk.Tk()
    app = TesteurVitesseApp(root)
    root.mainloop()