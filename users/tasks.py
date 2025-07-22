from django.utils import timezone
from datetime import timedelta
from .models import User
from celery import shared_task

@shared_task
def check_last_login():
    time_threshold = timezone.now() - timedelta(days=31)
    users_to_block = User.objects.filter(
        last_login__isnull=False,
        last_login__lte=time_threshold,
        is_active=True
    ).exclude(is_staff=True).exclude(is_superuser=True)
    blocked_users = list(users_to_block.values('id', 'email', 'last_login'))
    print(blocked_users)
    if blocked_users:
        updated = users_to_block.update(is_active=False)
        print(f"\n=== Блокировка пользователей ===")
        print(f"Проверка на: {timezone.now()}")
        print(f"Не заходили с: {time_threshold}")
        print(f"Заблокировано: {updated} пользователей")

        for user in blocked_users:
            print(f"ID: {user['id']} | Email: {user['email']} | Последний вход: {user['last_login']}")
    else:
        print("\nНет пользователей для блокировки")

    return len(blocked_users)
