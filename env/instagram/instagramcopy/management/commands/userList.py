from django.core.management.base import BaseCommand

from instagramcopy.models import Post

class UserList(BaseCommand):
    def handle(self, *args, **kwargs):
        print("Los usuarios creados son los siguientes:\n", User.objects.all())
