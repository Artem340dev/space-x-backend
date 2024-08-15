from django.forms import ModelForm
from . import models


class WebsiteElementsForm(ModelForm):
    class Meta:
        model = models.WebsiteElements
        fields = ['page', 'element_tag']