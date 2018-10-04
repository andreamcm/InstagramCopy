# Universidad del Valle de Guatemala
# Autora: Andrea Maria Cordon Mayen
# Carne: 16076
# mainmenu.py
# MENU PRINCIPAL DE LA APLICACION DE POSTS (INSTAGRAM)

# Se importan los comandos a utilizar dentro del menu
from django.core.management.base import BaseCommand
#from user import createUser
#from commands import *
from django.contrib.auth.models import User

# Se da al usuario la bienvenida al programa
print ("Bienvenido a InstagramCopy")
print ("Puede seleccionar cualquiera de las siguientes opciones")
print ("1. Registarse\n2. Ver usuarios\n3. Acceder\n4. Salir")
eleccion = input("¿Qué acción desea realizar?: ")

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        while True:
            if (eleccion == "1"):
                print ("Cantidad antes:", User.objects.all().count())
                nombre = input("Ingrese su primer nombre: ")
                apellido = input("Ingrese su primer apellido: ")
                username = input("Ingrese su nombre de usuario: ")
                email = input("Ingrese su correo electronico: ")
                mi_usuario = User(first_name=nombre, last_name=apellido, username=username, email=email)
                mi_usuario.save()
                print ("Cantidad despues:", User.objects.all().count())
                break
            elif (eleccion == '2'):
                for user in User.objects.all():
                    print ("pk={}: {} {} - {}".format(user.pk, user.first_name, user.last_name, user.username, user.email))
                break
            elif (eleccion == '3'):
                usuario = input('Ingrese su nombre de usuario: ')
                correo = input('Ingrese su correo electronico:')
                try: 
                    acceso = User.objects.get(username = usuario, email = correo)
                except:
                    print ('Este usuario no existe. Intentelo de nuevo')
                break

            elif (eleccion == '4'):
                print ("Gracias por usar InstagramCopy")
                break