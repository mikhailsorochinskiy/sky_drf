from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = 'Add moderator user to the database'

    def handle(self, *args, **kwargs):
        user, created = User.objects.get_or_create(email='moderator@mail.ru')
        if created:
            user.set_password('qwerty')
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully created moderator: {user}'))
        else:
            self.stdout.write(self.style.WARNING(f'Moderator already exists: {user}'))
