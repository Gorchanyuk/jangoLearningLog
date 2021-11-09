from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Topic(models.Model):
    """Тема, которую изучает пользователь"""
    text = models.CharField(max_length=200, verbose_name='Текст')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    class Meta:
        verbose_name = 'Тему'
        verbose_name_plural = 'Темы'

    def __str__(self):
        """Вщзвращает строковое представление модели"""
        return self.text

    def get_absolute_url(self):
        return reverse('learning_logs:topic', kwargs={'topic_id': self.pk})


class Entry(models.Model):
    """Информация, изученная пользователем по теме"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Тема')
    text = models.TextField(verbose_name='Текст')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['date_added', 'topic', 'text']

    def __str__(self):
        """Возвращает строковое представление модели"""
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text

    def get_absolute_url(self):
        return reverse('learning_logs:edit_entry', kwargs={'entry_id': self.pk})


class Pizza(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.text


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.text
