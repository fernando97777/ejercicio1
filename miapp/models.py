from django.db import models


class Profile(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name="Nombre"
    )
    age = models.PositiveIntegerField(
        verbose_name="Edad"
    )

    def __str__(self):
        return self.name

