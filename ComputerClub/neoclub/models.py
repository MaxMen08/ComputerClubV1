from django.db import models


class Player(models.Model):
    """Игрок"""
    name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    nick_name = models.CharField(max_length=50, verbose_name="Никнейм")

    class Meta:
        verbose_name = "Игрок"
        verbose_name_plural = "Игроки"

    def __str__(self):
        return f"{self.name} - {self.nick_name}"


class Hall(models.Model):
    """Зал"""
    title = models.CharField(max_length=50, verbose_name="Название зала")

    class Meta:
        verbose_name = "Зал"
        verbose_name_plural = "Залы"

    def __str__(self):
        return self.title


class Computers(models.Model):
    """Компьютеры"""
    number = models.IntegerField(null=True, blank=True, verbose_name="Номер компьютера")
    characteristics = models.TextField(null=True, blank=True, verbose_name="Характеристика")
    hall = models.ForeignKey('Hall', null=True, on_delete=models.PROTECT, verbose_name="Зал")

    class Meta:
        verbose_name = "Компьютер"
        verbose_name_plural = "Компьютеры"

    def __str__(self):
        return  f"{self.number}"


class Visit(models.Model):
    """Посещение"""
    player = models.ForeignKey('Player', null=True, on_delete=models.PROTECT, verbose_name="Игрок")
    date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Дата посещения")
    time = models.IntegerField(max_length=3, verbose_name="Кол-во минут")
    computers = models.ForeignKey('Computers', null=True, on_delete=models.CASCADE, verbose_name="Компьютер")

    class Meta:
        verbose_name = "Посещение"
        verbose_name_plural = "Посещения"

    def __str__(self):
        return f"{self.player}"
