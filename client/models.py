from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Client(models.Model):
    """Модель Client для хранения информации о клиентах веб-приложения"""

    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    patronymic = models.CharField(max_length=50, verbose_name="Отчество", **NULLABLE)

    email = models.EmailField(max_length=100, verbose_name="Почта")

    comment = models.TextField(verbose_name="Комментарий", **NULLABLE)

    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, verbose_name="Владелец", **NULLABLE
    )

    def __str__(self):
        """Возвращает строковое представление объекта"""
        return f"{self.last_name} {self.first_name} ({self.email})"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
