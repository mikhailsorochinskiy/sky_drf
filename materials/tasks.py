from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task(bind=True, max_retries=3)
def send_mail_update_course(self, recipients, course_name):
    if recipients:
        try:
            send_mail(subject='Обновление курса.', message=f'Материалы курса {course_name} обновились!',
                      from_email=settings.EMAIL_HOST_USER, recipient_list=recipients, fail_silently=False)
        except Exception as e:
            print(f'Ошибка при отправке письма: {e}')
            raise self.retry(exc=e, countdown=60)  # Повтор через 60 секунд
