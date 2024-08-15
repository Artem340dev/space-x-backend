from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.WebsiteElements)
admin.site.register(models.WebsiteElementsMetadata)