from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=120)
    
    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.category_name