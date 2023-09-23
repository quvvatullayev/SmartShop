from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=120)
    
    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.title
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=120)
    description = models.TextField()
    img = models.ImageField(upload_to='../product_imgs')
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.title
    