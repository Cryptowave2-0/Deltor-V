rocket_list = {"rocket":
    {
        "num": 1,
        "mun": 2
    }
}

import datetime

#fusée1 = {"name": 2}
#print(fusée1["name"],open('rocket save.json', 'r'))



# with open('rocket save.json', 'w+') as file:
#    json.dump(fusée1, file)






# les imports
import os
import json
from tkinter import *
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
#nique ta mère sale fils de pute...
#( entrez une valeur ici )



wind = Tk()
wind.title("Delta-V")
wind.geometry("700x480")
wind.minsize(200, 250)
wind.maxsize(200, 250)
wind.iconbitmap("logo.ico")
wind.config(background='#1C2833')

def edit():
    def recupere():
        e1v1 = int(entree1.get())
        e1v2 = int(entree2.get())
        e1v3 = int(entree3.get())
        e1v4 = int(entree4.get())
        e2v1 = int(entree5.get())
        e2v2 = int(entree6.get())
        e2v3 = int(entree7.get())
        e2v4 = int(entree8.get())
        e3v1 = int(entree9.get())
        e3v2 = int(entree10.get())
        e3v3 = int(entree11.get())
        e3v4 = int(entree12.get())
        e4v1 = int(entree13.get())
        e4v2 = int(entree14.get())
        e4v3 = int(entree15.get())
        e4v4 = int(entree16.get())
        e5v1 = int(entree17.get())
        e5v2 = int(entree18.get())
        e5v3 = int(entree19.get())
        mcu = str(entree21.get())
        e5v4 = int(entree20.get())

    window = Tk()
    window.title("Delta-V")
    window.geometry("700x480")
    window.minsize(700, 540)
    window.maxsize(700, 540)
    window.iconbitmap("logo.ico")
    window.config(background='#1C2833')

    name_of_rocket = "sdfsfsfsfvcsvc"

    label_title = Label(window, text="Editer  un fichier", bg='#1C2833', font=("Cascadia", 30), fg='#46FF49').pack()
    label_subtitle = Label(window, text=name_of_rocket, bg='#1C2833', font=("Cascadia", 10), fg='#46FF49').pack()

    label_subtitle = Label(window, text="Masse d'ergols ( en tonnes, premier étage ) :"
                                            "\nMasse à vide ( en tonnes, premier étage ) :"
                                            "\nMasse total ( en tonnes, premier étage ) :"
                                            "\nVitesse d'éjection des gazs* ( en m/s, premier étage ) :"
                                            "\n(*) Masse d'ergols ( en tonnes, deuxième étage ) :"
                                            "\n(*) Masse à vide ( en tonnes, deuxième étage ) :"
                                            "\n(*) Masse total ( en tonnes, deuxième étage ) :"
                                            "\n(*) Vitesse d'éjection des gazs* ( en m/s, deuxième étage ) :"
                                            "\n(*) Masse d'ergols ( en tonnes, troisième étage ) :"
                                            "\n(*) Masse à vide ( en tonnes, troisième étage ) :"
                                            "\n(*) Masse total ( en tonnes, troisième étage ) :"
                                            "\n(*) Vitesse d'éjection des gazs* ( en m/s, troisième étage ) :"
                                            "\n(*) Masse d'ergols ( en tonnes, quatrième étage ) :"
                                            "\n(*) Masse à vide ( en tonnes, quatrième étage ) :"
                                            "\n(*) Masse total ( en tonnes, quatrième étage ) :"
                                            "\n(*) Vitesse d'éjection des gazs* ( en m/s, quatrième étage ) :"
                                            "\n(*) Masse d'ergols ( en tonnes, cinquième étage ) :"
                                            "\n(*) Masse à vide ( en tonnes, cinquième étage ) :"
                                            "\n(*) Masse total ( en tonnes, cinquième étage ) :"
                                            "\n(*) Vitesse d'éjection des gazs* ( en m/s, cinquième étage ) :"
                                            "\nMasse de la charge utile :"
                                            "\n\n"
                                            "\n*Ve = ( isp de tout les moteurs de l'étage aditionné "
                                            "\ndisvisé par le nombre de moteurs ) fois 9,81"
                                            "\n(*) = facultatif"
                           , bg='#1C2833', font=("Cascadia", 12), fg='#46FF49').pack(side=LEFT)

    value = IntVar()
    value.set('')
    entree1 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                    relief=FLAT)
    entree1.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree2 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                    relief=FLAT)
    entree2.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree3 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                    relief=FLAT)
    entree3.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree4 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                    relief=FLAT)
    entree4.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree5 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                    relief=FLAT)
    entree5.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree6 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                    relief=FLAT)
    entree6.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree7 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                    relief=FLAT)
    entree7.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree8 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                    relief=FLAT)
    entree8.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree9 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                    relief=FLAT)
    entree9.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree10 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                     relief=FLAT)
    entree10.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree11 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                     relief=FLAT)
    entree11.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree12 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                     relief=FLAT)
    entree12.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree13 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                     relief=FLAT)
    entree13.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree14 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                     relief=FLAT)
    entree14.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree15 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                     relief=FLAT)
    entree15.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree16 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                     relief=FLAT)
    entree16.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree17 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                     relief=FLAT)
    entree17.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree18 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                     relief=FLAT)
    entree18.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree19 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                     relief=FLAT)
    entree19.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree20 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                     relief=FLAT)
    entree20.pack(padx=10, pady=1)

    value = StringVar()
    value.set('')
    entree21 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                     relief=FLAT)
    entree21.pack(padx=10, pady=1)

    bouton = Button(window, text="Valider", command=recupere, cursor="target")
    bouton.pack(side=BOTTOM, padx=10, pady=20)

    window.mainloop()

def create():
    def recupere():
        if entree1.get() == str:
            return
        else:
            me1 = int(entree1.get())
            mv1 = int(entree2.get())
            mt1 = int(entree3.get())
            ve1 = int(entree4.get())
            if entree00.get() == int or '':
                return
            else :
                name = str(entree00.get())
            if entree21.get() == str:
                return
            else :
                mcu = str(entree21.get())
            if entree5.get() == str:
                return
            else:
                me2 = int(entree5.get())
                mv2 = int(entree6.get())
                mt2 = int(entree7.get())
                ve2 = int(entree8.get())
                if entree9.get() == str:
                    return
                else:
                    me3 = int(entree9.get())
                    mv3 = int(entree10.get())
                    mt3 = int(entree11.get())
                    ve3 = int(entree12.get())
                    if entree13.get() == str:
                        return
                    else:
                        me4 = int(entree13.get())
                        mv4 = int(entree14.get())
                        mt4 = int(entree15.get())
                        ve4 = int(entree16.get())
                        if entree17.get() == str:
                            return
                        else:
                            me5 = int(entree17.get())
                            mv5 = int(entree18.get())
                            mt5 = int(entree19.get())
                            ve5 = int(entree20.get())

#        print(f"{me1} + {me2} = {me1 + me2}")

    window = Tk()
    window.title("Delta-V")
    window.geometry("700x480")
    window.minsize(700, 535)
    window.maxsize(700, 535)
    window.iconbitmap("logo.ico")
    window.config(background='#1C2833')

    label_title = Label(window, text="Créer un fichier ", bg='#1C2833', font=("Cascadia", 30), fg='#46FF49').pack()

    label_subtitle = Label(window, text="Nom de la fusée :"
                                            "\nMasse d'ergols ( en tonnes, premier étage ) :"
                                            "\nMasse à vide ( en tonnes, premier étage ) :"
                                            "\nMasse total ( en tonnes, premier étage ) :"
                                            "\nVitesse d'éjection des gazs* ( en m/s, premier étage ) :"
                                            "\n(*) Masse d'ergols ( en tonnes, deuxième étage ) :"
                                            "\n(*) Masse à vide ( en tonnes, deuxième étage ) :"
                                            "\n(*) Masse total ( en tonnes, deuxième étage ) :"
                                            "\n(*) Vitesse d'éjection des gazs* ( en m/s, deuxième étage ) :"
                                            "\n(*) Masse d'ergols ( en tonnes, troisième étage ) :"
                                            "\n(*) Masse à vide ( en tonnes, troisième étage ) :"
                                            "\n(*) Masse total ( en tonnes, troisième étage ) :"
                                            "\n(*) Vitesse d'éjection des gazs* ( en m/s, troisième étage ) :"
                                            "\n(*) Masse d'ergols ( en tonnes, quatrième étage ) :"
                                            "\n(*) Masse à vide ( en tonnes, quatrième étage ) :"
                                            "\n(*) Masse total ( en tonnes, quatrième étage ) :"
                                            "\n(*) Vitesse d'éjection des gazs* ( en m/s, quatrième étage ) :"
                                            "\n(*) Masse d'ergols ( en tonnes, cinquième étage ) :"
                                            "\n(*) Masse à vide ( en tonnes, cinquième étage ) :"
                                            "\n(*) Masse total ( en tonnes, cinquième étage ) :"
                                            "\n(*) Vitesse d'éjection des gazs* ( en m/s, cinquième étage ) :"
                                            "\nMasse de la charge utile :"
                                            "\n\n"
                                            "\n*Ve = ( isp de tout les moteurs de l'étage aditionné "
                                            "\ndisvisé par le nombre de moteurs ) fois 9,81"
                                            "\n(*) = facultatif"
                           , bg='#1C2833', font=("Cascadia", 12), fg='#46FF49').pack(side=LEFT)

    value = StringVar()
    value.set('')
    entree00 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                    relief=FLAT)
    entree00.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree1 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                    relief=FLAT)
    entree1.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree2 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                    relief=FLAT)
    entree2.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree3 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                    relief=FLAT)
    entree3.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree4 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                    relief=FLAT)
    entree4.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree5 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                    relief=FLAT)
    entree5.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree6 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                    relief=FLAT)
    entree6.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree7 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                    relief=FLAT)
    entree7.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree8 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                    relief=FLAT)
    entree8.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree9 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                    relief=FLAT)
    entree9.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree10 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                     relief=FLAT)
    entree10.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree11 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                     relief=FLAT)
    entree11.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree12 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                     relief=FLAT)
    entree12.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree13 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                     relief=FLAT)
    entree13.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree14 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                     relief=FLAT)
    entree14.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree15 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                     relief=FLAT)
    entree15.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree16 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                     relief=FLAT)
    entree16.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree17 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                     relief=FLAT)
    entree17.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree18 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                     relief=FLAT)
    entree18.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree19 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                     relief=FLAT)
    entree19.pack(padx=10, pady=1)

    value = IntVar()
    value.set('')
    entree20 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                     relief=FLAT)
    entree20.pack(padx=10, pady=1)

    value = StringVar()
    value.set('')
    entree21 = Entry(window, textvariable=value, width=40, bg='#000025', font=("Cascadia", 7), fg='#46FF49',
                     relief=FLAT)
    entree21.pack(padx=10, pady=1)

    bouton = Button(window, text="Valider", command=recupere, cursor="target")
    bouton.pack(side=BOTTOM, padx=10, pady=20)

    menubar = Menu(window)

    menubar.add_cascade(label="Quitter", command=window.quit)
    window.config(menu=menubar)

    window.mainloop()


label_title = Label(wind, text="Acceuil ", bg='#1C2833', font=("Cascadia", 30), fg='#46FF49').pack()


if os.path.exists('rocket save.json'):
    with open('rocket save.json', 'r') as file:
        add = file.read()
        json_interrior = json.loads(add)
        file.close()
else:
    print("le fichier n'hexiste pas mais je le créer pour vous")

for rocket in json_interrior:
    print(rocket)
    print(json_interrior[rocket]["me1"])






bouton = Button(wind, text="Start", highlightcolor='#1C2833', command=create, cursor="target")
bouton.pack(fill=X, padx=5, pady=10, side=BOTTOM)

menubar = Menu(wind)

menu1 = Menu(menubar, tearoff=1)
menu1.add_command(label="Créer", command=create)
menu1.add_command(label="Editer", command=edit)
menu1.add_separator()
menu1.add_command(label="Quitter", command=(wind.quit))
menubar.add_cascade(label="Fichier", menu=menu1)
wind.config(menu=menubar)


wind.mainloop()