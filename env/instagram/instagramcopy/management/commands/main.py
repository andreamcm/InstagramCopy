# Universidad del Valle de Guatemala
# Autora: Andrea Maria Cordon Mayen
# Carne: 16076
# main.py
# MAPLICACION DE POSTS (INSTAGRAMCOPY)

# Se importan los comandos a utilizar dentro del menu
from django.core.management.base import BaseCommand
import instagramcopy.models as modelos
from django.contrib.auth.models import User

# Se definen las funciones de los menus a utilizar (NO IMPLEMENTADOS, PERO PENSADOS)
# Menu principal de la instagramcopy
def menu_principal():
    print ("Bienvenido a InstagramCopy")
    print ("Puede seleccionar cualquiera de las siguientes opciones")
    print ("1. Registarse\n2. Ver usuarios\n3. Acceder\n4. Salir")
    eleccion = input("¿Qué acción desea realizar?: ")

# Menu principal de cada usuario
def menu_usuario():
    print ("Bienvenido " + User.objects.get(first_name))
    print ("Puede realizar lo siguiente: ")
    print ("1. Hacer un post\n2. Ver todos los posts\n3. Borrar un post\n4. Salir")
    eleccion_usuario = input("¿Qué acción desea realizar?")

# Se da al usuario la bienvenida al programa
print ("\n BIENVENIDO A INSTAGRAM COPY\n")

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        while (True):
            # Se ingresa al menu principal
            print ("\n MENU PRINCIPAL ")
            print ("----------------\n")
            print ("Puede seleccionar cualquiera de las siguientes opciones")
            print ("1. Registarse\n2. Ver usuarios\n3. Acceder\n4. Salir")
            # Se permite ingresar una de las opciones
            eleccion = input("¿Qué acción desea realizar?: ")
            # Si seleccionan crear un usuario
            if (eleccion == '1'):
                print ("\n CREANDO UN USUARIO ")
                print ("--------------------\n")
                print ("Cantidad antes: ", User.objects.all().count())
                nombre = input("Ingrese su primer nombre: ")
                apellido = input("Ingrese su primer apellido: ")
                username = input("Ingrese su nombre de usuario: ")
                email = input("Ingrese su correo electronico: ")
                mi_usuario = User(first_name=nombre, last_name=apellido, username=username, email=email)
                mi_usuario.save()
                print ("Cantidad despues:", User.objects.all().count())
            # Si selecciona ver usuarios creados
            elif (eleccion == '2'):
                print ("\n USUARIOS CREADOS ")
                print ("------------------\n")
                for user in User.objects.all():
                    print ("pk={}: {} {} - {} - {}".format(user.pk, user.first_name, user.last_name, user.username, user.email))
            # Si selecciona ingresar a un perfil
            elif (eleccion == '3'):
                print ("\n INGRESO A TU PERFIL ")
                print ("-------------------------\n")
                usuario = input('Ingrese su nombre de usuario: ')
                correo = input('Ingrese su correo electronico: ')
                # Verificar si el usuario existe
                try: 
                    acceso = User.objects.get(username = usuario, email = correo)
                # Si el usuario no existe
                except:
                    print ('Este usuario no existe. Intentelo de nuevo')
                # Si el usuario existe
                while (True):
                    # Bienvenida personalizada al usuario
                    print ("\n BIENVENIDO {} ".format(acceso.first_name))
                    print ("---------------\n") 
                    print ("Puede realizar lo siguiente: ")
                    print ("1. Hacer un post\n2. Darle like a un post\n3. Borrar un post\n4. Salir")
                    # Se le presenta la opcion de escoger una opcion como usuario
                    eleccion_usuario = input("¿Qué acción desea realizar?")
                    # Si desea crear un post
                    if (eleccion_usuario == '1'):
                        print (" \nCREANDO UN POST ")
                        print ("-----------------\n")
                        print ("Cantidad antes: ", modelos.Post.objects.all().count())
                        titulo = input("Ingrese el titulo del post: ")
                        contenido = input("Ingrese el contenido del post: ")
                        usuarito = acceso.username
                        print(usuarito)
                        mi_post = modelos.Post(title=titulo, content=contenido, posted_by=usuarito)
                        mi_post.save()
                        print ("Cantidad despues: ", modelos.Post.objects.all().count())
                    # Si desea darle like a un post
                    elif (eleccion_usuario == '2'):
                        print (" \nLIKE A UN POST ")
                        print ("-------------------\n")
                        for post in modelos.Post.objects.all():
                            print ("Post: {}\nContenido: {}\nBy: {}\nLikes: {}\n\n".format(post.title, post.content, post.posted_by, post.liked_by.count()))
                            likefor = input("¿A que post le gustaria darle like (titulo)?: ")
                            try:
                                posti = modelos.Post.get(title=likefor)
                            except:
                                print ("Este post no existe")
                    # Si desea eliminar un post personal
                    elif (eleccion_usuario == '3'):
                        print (" \nELIMINANDO UN POST ")
                        print ("-------------------\n")
                    # Si desea salir del perfil
                    elif (eleccion_usuario == '4'):
                        break
            # Si desea salir de la aplicacion
            elif (eleccion == '4'):
                print ("Gracias por usar InstagramCopy")
                break
