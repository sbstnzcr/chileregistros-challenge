from django.db import models


class UnidadFiscalizable(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Sancion(models.Model):
    class Meta:
        verbose_name_plural = "sanciones"

    expediente = models.CharField(max_length=20)
    unidad_fiscalizable = models.ForeignKey(
        UnidadFiscalizable, on_delete=models.CASCADE
    )
    nombre_razon_social = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    detalle_link = models.URLField()

    def __str__(self):
        return self.expediente
