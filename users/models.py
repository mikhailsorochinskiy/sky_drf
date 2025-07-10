from django.db import models
from django.contrib.auth.models import AbstractUser
from materials.models import Course, Lesson


class User(AbstractUser):
    username = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(unique=True, verbose_name='Email')
    phone_number = models.CharField(max_length=15, blank=True, null=True, help_text='Введите номер телефона', verbose_name='Телефон')
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True, verbose_name="Аватар",
                              help_text='Загрузите фото для вашей аватарки')
    city = models.CharField(max_length=50, blank=True, null=True, help_text='Ваш город', verbose_name='Город')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.email}'


class Payment(models.Model):
    PAYMENT_CHOICES = [
        ("BANK_TRANSFER", "Банковский перевод"),
        ("CASH", "Наличными"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты')
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Оплаченный курс",
        blank=True,
        null=True,
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        verbose_name="Оплаченный урок",
        blank=True,
        null=True,
    )
    amount = models.DecimalField(decimal_places=2, max_digits=20, verbose_name="Сумма")
    type = models.CharField(
        max_length=50, choices=PAYMENT_CHOICES, verbose_name="Способ оплаты"
    )

    def __str__(self):
        return f'{self.user}:{self.payment_date}:{self.type}:{self.amount}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'


class Subscribe(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
        verbose_name="курс",
        related_name="course_subscribe",
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', related_name='user_subscribe')

    def __str__(self):
        return f"{self.user} подписан на {self.course.name}"

    class Meta:
        unique_together = ("user", "course")
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
