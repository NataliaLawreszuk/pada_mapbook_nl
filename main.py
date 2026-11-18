from tkinter import *
import tkintermapview

# def oczywiscie_ze_tak():
#     print('oczywiscie ze tak')
#
root = Tk()
root.geometry('1024x768')
root.title('Mapbook')
#
# label = Label(root, text='Czy geoinformatyka rządzi?')
# label.grid(row=0, column=0)
#
# guzik_tak = Button(root, text='tak', command=oczywiscie_ze_tak)
# guzik_tak.grid(row=1, column=0)
#
# guzik_nie = Button(root, text='nie')
# guzik_nie.grid(row=1, column=1)

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

button_pokaz_szczegoly = Button(ramka_lista_obiektow, text= 'Pokaż szczegóły')
button_edytuj_obiekt = Button(ramka_lista_obiektow, text='Edytuj obiekt')
button_usun_obiekt = Button(ramka_lista_obiektow, text='Usun obiekt')
#button_dodaj_obiekt = Button(ramka_lista_obiektow, text='Dodaj obiekt')

label_lista_obiektow.grid(row=0, column=0)
listbox_lista_obiektow.grid(row=1, column=0)
button_pokaz_szczegoly.grid(row=2, column=0)
button_edytuj_obiekt.grid(row=2, column=1)
button_usun_obiekt.grid(row=2, column=2)

#RAMKA FORMULARZ
label_formularz = Label(ramka_formularz, text='Formularz:')
label_name = Label(ramka_formularz, text='Imię:')
label_location = Label(ramka_formularz, text='Miejscowość:')
label_posts = Label(ramka_formularz, text='Postów:')
entry_name = Entry(ramka_formularz)
entry_location = Entry(ramka_formularz)
entry_posts = Entry(ramka_formularz)
button_dodaj_obiekt = Button(ramka_formularz, text='Dodaj obiekt')

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