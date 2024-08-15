import json

from django.db import models

# Create your models here.
class WebsiteElements(models.Model):
    id = models.AutoField('ID', primary_key=True)
    page = models.CharField('Страница', max_length=50)
    element_tag = models.CharField('Тег', max_length=300)

    def __str__(self):
        return self.element_tag

    class Meta:
        ordering = ['id']
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'

class WebsiteElementsMetadata(models.Model):
    metadata_id = models.AutoField('ID Метадаты', primary_key=True)
    website_element = models.ForeignKey('WebsiteElements', related_name='metadataset', on_delete=models.CASCADE)
    attribute = models.CharField('Атрибут', max_length=50)
    value = models.TextField('Значение')

    def __str__(self):
        return json.dumps({self.attribute: self.value})

    class Meta:
        verbose_name = 'Атрибут метадаты'
        verbose_name_plural = 'Набор метадаты'