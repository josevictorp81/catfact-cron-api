from django.db import models

class Fact(models.Model):
    fact = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = 'Fatos'
    
    def __str__(self) -> str:
        return self.fact