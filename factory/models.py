from django.db import models
from django.contrib.auth.models import User


class Factory(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    daily_production = models.PositiveIntegerField()
    # gunluk üretim kapasitesi
    city = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.city} - {self.name}"

    # fabrikanın nasıl görüneceği belirttik

    class Meta:
        verbose_name = "Factory"
        verbose_name_plural = "Factories"


class Machine(models.Model):
    factory = models.ForeignKey(
        Factory, on_delete=models.DO_NOTHING, related_name="machines")

# makine hangi fabrikada üretildi bilgisi related_name ile de fabrikada üretilen makinelere ulaşıyoruz.
    name = models.CharField(max_length=50)
    power = models.CharField(max_length=8)

    def __str__(self) -> str:
        return self.name
