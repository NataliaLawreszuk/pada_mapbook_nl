from tkinter import *
import tkintermapview
from mapbook_shared.controler import get_coordinates

users: list = []

def add_user():
    name = entry_name.get()
    location = entry_location.get()
    posts = entry_posts.get()

    x, y = get_coordinates(location)
    map_widget.set_marker(x, y, text=name)

    users.append(
        {'name':name, 'location':location,'posts':posts, 'marker':map_widget.set_marker(x, y, text=name), 'x':x,
         'y':y})
    print('to jest lista', users)

    entry_name.delete(0, 'end')
    entry_location.delete(0, 'end')
    entry_posts.delete(0, 'end')
    entry_name.focus()
    show_users()

def show_users():
    listbox_lista_obiektow.delete(0, 'end')
    for idx, user in enumerate(users):
        listbox_lista_obiektow.insert(idx, user['name'])

def remove_user():
    i = listbox_lista_obiektow.index(ACTIVE)
    print(i)
    users[i]['marker'].delete()
    users.pop(i)
    show_users()

def edit_user():
    i = listbox_lista_obiektow.index(ACTIVE)
    entry_name.insert(0, users[i]['name'])
    entry_location.insert(0, users[i]['location'])
    entry_posts.insert(0, users[i]['posts'])
    button_dodaj_obiekt.config(text= 'Zapisz zmiany', command = lambda:update_user(i))

def update_user(i):
    new_name = entry_name.get()
    new_location = entry_location.get()
    new_posts = entry_posts.get()
    users[i]['name'] = new_name
    users[i]['location'] = new_location
    users[i]['posts'] = new_posts
    x,y = get_coordinates(new_location)
    users[i]['marker'].delete()
    users[i]['marker'] = map_widget.set_marker(x,y, text = entry_name.get())


    show_users()
    button_dodaj_obiekt.config(text= 'Dodaj obiekt', command = add_user)
    entry_name.delete(0, 'end')
    entry_location.delete(0, 'end')
    entry_posts.delete(0, 'end')
    entry_name.focus()

def show_user_details():
    i = listbox_lista_obiektow.index(ACTIVE)
    tmp_user = users[i]['name']
    tmp_location = users[i]['location']
    tmp_posts = users[i]['posts']
    label_name_szczegoly_obiektu_wartosc.configure(text=tmp_user)
    label_location_szczegoly_obiektu_wartosc.config(text=tmp_location)
    label_posts_szczegoly_obiektu_wartosc.config(text=tmp_posts)

    map_widget.set_marker(users[i]['x'],users[i]['y'])
    map_widget.set_zoom(11)



root = Tk()
root.geometry('1024x768')
root.title('Mapbook')

#RAMKI
ramka_lista_obiektow = Frame(root)
ramka_formularz = Frame(root)
ramka_szczegoly_obiektu = Frame(root)
ramka_mapa = Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektu.grid(row=1, column=0, columnspan=2)
ramka_mapa.grid(row=2, column=0, columnspan=7)

#RAMKA LISTA OBIEKTÓW
label_lista_obiektow = Label(ramka_lista_obiektow, text='Lista obiektow:')
listbox_lista_obiektow = Listbox(ramka_lista_obiektow)

button_pokaz_szczegoly = Button(ramka_lista_obiektow, text= 'Pokaż szczegóły', command = show_user_details)
button_edytuj_obiekt = Button(ramka_lista_obiektow, text='Edytuj obiekt', command=edit_user)
button_usun_obiekt = Button(ramka_lista_obiektow, text='Usun obiekt', command=remove_user)
#button_dodaj_obiekt = Button(ramka_lista_obiektow, text='Dodaj obiekt')

label_lista_obiektow.grid(row=0, column=0)
listbox_lista_obiektow.grid(row=1, column=0)
button_pokaz_szczegoly.grid(row=2, column=0)
button_edytuj_obiekt.grid(row=2, column=1,)
button_usun_obiekt.grid(row=2, column=2)

#RAMKA FORMULARZ
label_formularz = Label(ramka_formularz, text='Formularz:')
label_name = Label(ramka_formularz, text='Imię:')
label_location = Label(ramka_formularz, text='Miejscowość:')
label_posts = Label(ramka_formularz, text='Postów:')
entry_name = Entry(ramka_formularz)
entry_location = Entry(ramka_formularz)
entry_posts = Entry(ramka_formularz)
button_dodaj_obiekt = Button(ramka_formularz, text='Dodaj obiekt', command=add_user)

label_formularz.grid(row=0, column=0)
label_name.grid(row=1, column=0)
label_location.grid(row=2, column=0)
label_posts.grid(row=3, column=0)
entry_name.grid(row=1, column=1)
entry_location.grid(row=2, column=1)
entry_posts.grid(row=3, column=1)
button_dodaj_obiekt.grid(row=4, column=0)

#RAMKA SZCZEGÓLY OBIEKTU
label_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text='Szczegóły obiektu:')
label_name_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text='Imię: ')
label_name_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text='.....')
label_location_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text='Miejscowość: ')
label_location_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text='.....')
label_posts_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text='Postów: ')
label_posts_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text='.....')

label_szczegoly_obiektu.grid(row=0, column=0)
label_name_szczegoly_obiektu.grid(row=1, column=0)
label_name_szczegoly_obiektu_wartosc.grid(row=1, column=1)
label_location_szczegoly_obiektu.grid(row=1, column=2)
label_location_szczegoly_obiektu_wartosc.grid(row=1, column=3)
label_posts_szczegoly_obiektu.grid(row=1, column=4)
label_posts_szczegoly_obiektu_wartosc.grid(row=1, column=5)

#RAMKA MAPA
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1024, height=500, corner_radius=5)
map_widget.set_position(52.23, 19.00)
map_widget.set_zoom(6)

map_widget.grid(row=0, column=0,columnspan=7)

root.mainloop()