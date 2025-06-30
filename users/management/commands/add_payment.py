from django.core.management.base import BaseCommand
from users.models import Payment, User
from materials.models import Course

class Command(BaseCommand):
    help = 'Add test payment to the database'

    def handle(self, *args, **kwargs):
        course, _ = Course.objects.get_or_create(name='Golang', description='Востребованный ЯП')
        user, _ = User.objects.get_or_create(email='test@mail.ru')
        payment, created = Payment.objects.get_or_create(user=user, paid_course=course, amount=100000, type='BANK_TRANSFER')
        if created:
            self.stdout.write(self.style.SUCCESS(f'Successfully added payment: {payment}'))
        else:
            self.stdout.write(self.style.WARNING(f'Payment already exists: {payment}'))
