from django.db import models

class Recepie(models.Model):
    name = models.CharField('name', max_length=50)
    description = models.TextField('description')
    active = models.BooleanField('active', default=True)
    image = models.ImageField('image', upload_to='recepie', default='no-image.png')

    def __str__(self):
        return f'Recepie.{self.name}'

