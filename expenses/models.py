from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nazwa kategorii")

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Expense(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="expenses",
        verbose_name="Kategoria"
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        verbose_name="Kwota"
    )
    date = models.DateField(verbose_name="Data")
    description = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Opis"
    )

    class Meta:
        verbose_name = "Wydatek"
        verbose_name_plural = "Wydatki"
        ordering = ["-date"]

    def __str__(self):
        return f"{self.category} - {self.amount} zł"