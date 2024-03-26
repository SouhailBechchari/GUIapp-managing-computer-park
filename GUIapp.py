import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


class AjouterMaterielPopup:
    def __init__(self, parent, callback):
        self.parent = parent
        self.callback = callback

        self.popup = tk.Toplevel(parent)
        self.popup.title("Ajouter un matériel")

        self.label_type = tk.Label(self.popup, text="Type:", fg="blue")
        self.label_type.grid(row=0, column=0)
        self.combobox_type = ttk.Combobox(self.popup, values=["PC PORTABLE", "ORDINATEUR", "IMPRIMANTE", "SOURIS", "CLAVIER", "CASQUE", "MANETTE"])
        self.combobox_type.grid(row=0, column=1)
        self.combobox_type.bind("<<ComboboxSelected>>", self.on_type_selected)

        self.label_nom = tk.Label(self.popup, text="Nom:", fg="blue")
        self.label_nom.grid(row=1, column=0)
        self.entry_nom = tk.Entry(self.popup)
        self.entry_nom.grid(row=1, column=1)

        self.label_marque = tk.Label(self.popup, text="Marque:", fg="blue")
        self.label_marque.grid(row=2, column=0)
        self.entry_marque = tk.Entry(self.popup)
        self.entry_marque.grid(row=2, column=1)

        self.label_modele = tk.Label(self.popup, text="Modèle:", fg="blue")
        self.label_modele.grid(row=3, column=0)
        self.entry_modele = tk.Entry(self.popup)
        self.entry_modele.grid(row=3, column=1)

        self.label_date_acquisition = tk.Label(self.popup, text="Date d'acquisition:", fg="blue")
        self.label_date_acquisition.grid(row=4, column=0)  
        self.entry_date_acquisition = tk.Entry(self.popup)
        self.entry_date_acquisition.grid(row=4, column=1)

        self.label_code = tk.Label(self.popup, text="Code:", fg="blue")
        self.label_code.grid(row=5, column=0)
        self.entry_code = tk.Entry(self.popup)
        self.entry_code.grid(row=5, column=1)

        self.label_processeur = tk.Label(self.popup, text="Processeur:", fg="blue")
        self.label_processeur.grid(row=6, column=0)
        self.entry_processeur = tk.Entry(self.popup)
        self.entry_processeur.grid(row=6, column=1)
        self.entry_processeur.grid_remove()

        self.label_type_impression = tk.Label(self.popup, text="Type d'impression:", fg="blue")
        self.label_type_impression.grid(row=7, column=0)
        self.entry_type_impression = tk.Entry(self.popup)
        self.entry_type_impression.grid(row=7, column=1)
        self.entry_type_impression.grid_remove()

        self.label_bluetooth = tk.Label(self.popup, text="Bluetooth:", fg="blue")
        self.label_bluetooth.grid(row=8, column=0)
        self.checkbox_bluetooth = tk.Checkbutton(self.popup, text="Oui", variable=tk.BooleanVar())
        self.checkbox_bluetooth.grid(row=8, column=1)
        self.checkbox_bluetooth.grid_remove()
        self.bluetooth_var = tk.BooleanVar()
        self.checkbox_bluetooth = tk.Checkbutton(self.popup, text="Bluetooth", variable=self.bluetooth_var)
        self.checkbox_bluetooth.grid(row=8, column=1)


        self.btn_ajouter = tk.Button(self.popup, text="Ajouter", command=self.ajouter_materiel, bg="green", fg="white")
        self.btn_ajouter.grid(row=9, columnspan=2)

    def on_type_selected(self, event):
        selected_type = self.combobox_type.get()

        if selected_type in ["PC PORTABLE", "ORDINATEUR"]:
            self.entry_processeur.grid()
        else:
            self.entry_processeur.grid_remove()

        if selected_type == "IMPRIMANTE":
            self.entry_type_impression.grid()
        else:
            self.entry_type_impression.grid_remove()

        if selected_type in ["CASQUE", "CLAVIER", "SOURIS", "MANETTE"]:
            self.checkbox_bluetooth.grid()
        else:
            self.checkbox_bluetooth.grid_remove()

    def ajouter_materiel(self):
        nom = self.entry_nom.get()
        marque = self.entry_marque.get()
        modele = self.entry_modele.get()
        date_acquisition = self.entry_date_acquisition.get()
        code = self.entry_code.get()
        processeur = self.entry_processeur.get()
        type_impression = self.entry_type_impression.get()

    # Fix here: get the value of the checkbox using 'IntVar().get()'
        bluetooth = "Oui" if self.bluetooth_var.get() else ""

        if nom and marque and modele and date_acquisition and code:
            self.callback({
            "type": self.combobox_type.get(),
            "nom": nom,
            "marque": marque,
            "modele": modele,
            "date_acquisition": date_acquisition,
            "code": code,
            "processeur": processeur,
            "type_impression": type_impression,
            "bluetooth": bluetooth
        })
            self.popup.destroy()
        else:
            messagebox.showwarning("Attention", "Veuillez remplir tous les champs.")


class AjouterClientPopup:
    def __init__(self, parent, callback):
        self.parent = parent
        self.callback = callback

        self.popup = tk.Toplevel(parent)
        self.popup.title("Ajouter un client")

        self.label_nom = tk.Label(self.popup, text="Nom:", fg="blue")
        self.label_nom.grid(row=0, column=0)
        self.entry_nom = tk.Entry(self.popup)
        self.entry_nom.grid(row=0, column=1)

        self.label_prenom = tk.Label(self.popup, text="Prénom:", fg="blue")
        self.label_prenom.grid(row=1, column=0)
        self.entry_prenom = tk.Entry(self.popup)
        self.entry_prenom.grid(row=1, column=1)

        self.label_materiels_achetes = tk.Label(self.popup, text="Matériels achetés:", fg="blue")
        self.label_materiels_achetes.grid(row=2, column=0)
        self.entry_materiels_achetes = tk.Entry(self.popup)
        self.entry_materiels_achetes.grid(row=2, column=1)

        self.label_date_achat = tk.Label(self.popup, text="Date d'achat:", fg="blue")
        self.label_date_achat.grid(row=3, column=0)
        self.entry_date_achat = tk.Entry(self.popup)
        self.entry_date_achat.grid(row=3, column=1)

        self.label_prix_achat = tk.Label(self.popup, text="Prix d'achat:", fg="blue")
        self.label_prix_achat.grid(row=4, column=0)
        self.entry_prix_achat = tk.Entry(self.popup)
        self.entry_prix_achat.grid(row=4, column=1)

        self.label_num_cin = tk.Label(self.popup, text="Numéro CIN:", fg="blue")
        self.label_num_cin.grid(row=5, column=0)
        self.entry_num_cin = tk.Entry(self.popup)
        self.entry_num_cin.grid(row=5, column=1)

        self.btn_ajouter = tk.Button(self.popup, text="Ajouter", command=self.ajouter_client, bg="green", fg="white")
        self.btn_ajouter.grid(row=6, columnspan=2)

    def ajouter_client(self):
        nom = self.entry_nom.get()
        prenom = self.entry_prenom.get()
        materiels_achetes = self.entry_materiels_achetes.get()
        date_achat = self.entry_date_achat.get()
        prix_achat = self.entry_prix_achat.get()
        num_cin = self.entry_num_cin.get()

        if nom and prenom and materiels_achetes and date_achat and prix_achat and num_cin:
            self.callback({
                "nom": nom,
                "prenom": prenom,
                "materiels_achetes": materiels_achetes,
                "date_achat": date_achat,
                "prix_achat": prix_achat,
                "num_cin": num_cin
            })
            self.popup.destroy()
        else:
            messagebox.showwarning("Attention", "Veuillez remplir tous les champs.")

class ParcInformatiqueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de Parc Informatique")
        

        self.db_connection = sqlite3.connect("parcinformatique.db")
        self.db_cursor = self.db_connection.cursor()

        self.background_image = tk.PhotoImage(file="bg.gif")

        # Afficher l'image de fond dans un label
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        


        self.initialize_database()

        self.materiels = []
        self.clients = []

        self.create_gui()

    def initialize_database(self):
        self.db_cursor.execute("""
            CREATE TABLE IF NOT EXISTS materiels (
                id_materiel int PRIMARY KEY AUTOINCREMENT,
                type varchar(10),
                nom varchar(10),
                marque varchar(10),
                modele varchar(10),
                date_acquisition DATE,
                code int,
                processeur varchar(10),
                type_impression varchar(10),
                bluetooth varchar(10)
            )
        """)

        self.db_cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id_client int PRIMARY KEY AUTOINCREMENT,
                nom varchar(10),
                prenom varchar(10),
                materiels_achetes varchar(10),
                date_achat DATE,
                prix_achat int,
                num_cin int
            )
        """)

    def create_gui(self):
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        self.label = tk.Label(self.frame, text="BechchariSouhail's Tech Center", font=('Verdana', 20,'italic',  'bold'), fg="#001F3F")
        self.label.grid(row=0, columnspan=2)

        self.listbox_materiels = tk.Listbox(self.frame, width=50, font=('Verdana', 10 , 'italic'))
        self.listbox_materiels.grid(row=1, columnspan=3)

        self.listbox_clients = tk.Listbox(self.frame, width=50, font=('Verdana', 10 , 'italic'))
        self.listbox_clients.grid(row=2, columnspan=3)

        self.btn_ajouter_materiel = tk.Button(self.frame, text="Ajouter Matériel", font=('Garamond', 13, 'bold'), command=self.ajouter_materiel_popup, bg="black", fg="white")
        self.btn_ajouter_materiel.grid(row=3, column=0, padx=5, pady=5, sticky="ew")  # Aligner à l'Est-Ouest (left-right)

        self.btn_ajouter_client = tk.Button(self.frame, text="Ajouter Client", font=('Garamond', 13, 'bold'),  command=self.ajouter_client_popup, bg="black", fg="white")
        self.btn_ajouter_client.grid(row=3, column=1, padx=5, pady=5, sticky="ew")  # Aligner à l'Est-Ouest (left-right)

        self.btn_supprimer = tk.Button(self.frame, text="Supprimer Matériel", font=('Garamond', 13, 'bold'),  command=self.supprimer_materiel, bg="black", fg="white")
        self.btn_supprimer.grid(row=4, column=0,columnspan=2, padx=5, pady=5, sticky="ew")  # Aligner à l'Est-Ouest (left-right)

        self.btn_afficher_materiels = tk.Button(self.frame, text="Afficher Matériels", font=('Garamond', 13, 'bold'),  command=self.afficher_materiels, bg="black", fg="white")
        self.btn_afficher_materiels.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew")  # Aligner à l'Est-Ouest (left-right)

        self.btn_afficher_clients = tk.Button(self.frame, text="Afficher Clients", font=('Garamond', 13, 'bold'), command=self.afficher_clients, bg="black", fg="white")
        self.btn_afficher_clients.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="ew")  # Aligner à l'Est-Ouest (left-right)
    def ajouter_materiel_popup(self):
        AjouterMaterielPopup(self.root, self.ajouter_materiel)

    def ajouter_materiel(self, data):
        self.materiels.append(data)
        self.ajouter_element("materiels", data)

    def ajouter_client_popup(self):
        AjouterClientPopup(self.root, self.ajouter_client)

    def ajouter_client(self, data):
        self.clients.append(data)
        self.ajouter_element("clients", data)

    def ajouter_element(self, table_name, data):
        try:
            placeholders = ', '.join(['?' for _ in range(len(data))])
            columns = ', '.join(data.keys())
            values = tuple(data.values())
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            self.db_cursor.execute(query, values)
            self.db_connection.commit()
            messagebox.showinfo("Succès", "Données ajoutées avec succès.")
        except sqlite3.Error as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'ajout des données : {e}")

    def afficher_materiels(self):
        self.listbox_materiels.delete(0, tk.END)
        self.db_cursor.execute("SELECT * FROM materiels")
        materiels = self.db_cursor.fetchall()
        if materiels:
            for materiel in materiels:
                self.listbox_materiels.insert(tk.END, materiel)
        else:
            self.listbox_materiels.insert(tk.END, "Aucun matériel disponible.")

    def afficher_clients(self):
        self.listbox_clients.delete(0, tk.END)
        self.db_cursor.execute("SELECT * FROM clients")
        clients = self.db_cursor.fetchall()
        if clients:
            for client in clients:
                self.listbox_clients.insert(tk.END, client)
        else:
            self.listbox_clients.insert(tk.END, "Aucun client enregistré.")

    def supprimer_materiel(self):
        selection = self.listbox_materiels.curselection()
        if selection:
            index = selection[0]
            item_id = index + 1  
            self.refresh_materiels_from_db() 
        if index < len(self.materiels):
            self.materiels.pop(index)
            self.db_cursor.execute("DELETE FROM materiels WHERE id=?", (item_id,))
            self.db_connection.commit()
            self.refresh_lists()
        else:
             messagebox.showwarning("Attention", "Veuillez sélectionner un matériel à supprimer.")

    def refresh_materiels_from_db(self):
        self.materiels.clear()
        self.db_cursor.execute("SELECT * FROM materiels")
        materiels = self.db_cursor.fetchall()
        if materiels:
            for materiel in materiels:
                self.materiels.append(materiel)
    def refresh_lists(self):
        self.listbox_materiels.delete(0, tk.END)
        for materiel in self.materiels:
            self.listbox_materiels.insert(tk.END, materiel)

        self.listbox_clients.delete(0, tk.END)
        for client in self.clients:
            self.listbox_clients.insert(tk.END, client)

root = tk.Tk()
root.iconbitmap('icon.ico') 
app = ParcInformatiqueApp(root)

root.geometry("1000x900")

root.mainloop()
