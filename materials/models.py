from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Курс')
    preview = models.ImageField(upload_to='course_photo', blank=True, null=True, verbose_name="Превью", help_text='Загрузите превью курса')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='Урок')
    preview = models.ImageField(upload_to='lesson_photo', blank=True, null=True, verbose_name="Превью", help_text='Загрузите превью урока')
    description = models.TextField(verbose_name='Описание')
    video_url = models.URLField(verbose_name='Ссылка на видео')
    course = models.ForeignKey(Course, on_delete=models.CASCADE,)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
