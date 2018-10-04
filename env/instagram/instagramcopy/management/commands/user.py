from django.core.management.base import BaseCommand

from instagramcopy.models import User


class CreateUser(BaseCommand):
    def handle(self, *args, **kwargs):
        print ("Cantidad antes:", Iser.objects.all().count())
        nombre = input("Ingrese su primer nombre: ")
        apellido = input("Ingrese su primer apellido: ")
        username = input("Ingrese su nombre de usuario: ")
        email = input("Ingrese su email: ")
        mi_usuario = User(nombre=nombre, apellido=apellido, username=username, email=email)
        mi_usuario.save()
        print ("Cantidad despues:", Iser.objects.all().count())