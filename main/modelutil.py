import json

from django.core import serializers
from . import models


class ModelUtil:
    @staticmethod
    def serialize(*args):
        elements = [element for element in args]
        serializedModels = serializers.serialize("json", elements)

        return serializedModels

    @staticmethod
    def mergeMetadataAndElement(element):
        metadata = json.loads(ModelUtil.serialize(*models.WebsiteElementsMetadata.objects.filter(website_element=element['pk'])))
        element.update({'metadata': metadata})

        return element

    @staticmethod
    def mergeMetadatasAndElements(elements):
        return [ModelUtil.mergeMetadataAndElement(element) for element in elements]