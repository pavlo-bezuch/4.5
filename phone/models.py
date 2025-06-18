from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=50, default="Unknown")
    founded_year = models.PositiveIntegerField(default=2000)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Smartphone(models.Model):
    OS_CHOICES = [
        ('Android', 'Android'),
        ('iOS', 'iOS'),
        ('HarmonyOS', 'HarmonyOS'),
    ]

    COLOR_CHOICES = [
        ('black', 'Чорний'),
        ('white', 'Білий'),
        ('blue', 'Синій'),
        ('red', 'Червоний'),
    ]

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="smartphones")
    model_name = models.CharField(max_length=100)
    os = models.CharField(max_length=20, choices=OS_CHOICES, default='Android')
    screen_size = models.FloatField(help_text="У дюймах", default=6.5)
    ram_gb = models.PositiveSmallIntegerField(default=4)
    storage_gb = models.PositiveSmallIntegerField(default=64)
    battery_mah = models.PositiveIntegerField(default=4000)
    has_5g = models.BooleanField(default=False)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='black')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand.name} {self.model_name}"
