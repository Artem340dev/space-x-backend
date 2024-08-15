import json

from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from . import forms, models

from . import modelutil

# Create your views here.
def createWebsiteElement(request):
    if request.method == 'POST':
        form = forms.WebsiteElementsForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 200, 'text': 'The form has been saved successful!'})

        return JsonResponse({'status': 10, 'text': 'The attributes have not been provided properly!'})

    return JsonResponse({'status': 11, 'text': 'This method processes only POST requests!'})

def getAllElements(request):
    elements = models.WebsiteElements.objects.all()
    response = modelutil.ModelUtil.mergeMetadatasAndElements(json.loads(modelutil.ModelUtil.serialize(*elements)))

    return HttpResponse(json.dumps(response), content_type='application/json')

def getElement(request):
    if request.method == 'GET':
        response = None
        if 'id' in request.GET:
            id = request.GET.get('id')
            element = json.loads(modelutil.ModelUtil.serialize(models.WebsiteElements.objects.get(id=id)))[0]
            response = modelutil.ModelUtil.mergeMetadataAndElement(element)

        if 'element_tag' in request.GET and 'page' in request.GET:
            element_tag = request.GET.get('element_tag')
            page = request.GET.get('page')

            element = json.loads(modelutil.ModelUtil.serialize(models.WebsiteElements.objects.get(element_tag=element_tag, page=page)))[0]
            response = modelutil.ModelUtil.mergeMetadataAndElement(element)

        if 'page' in request.GET:
            page = request.GET.get('page')

            elements = json.loads(modelutil.ModelUtil.serialize(*models.WebsiteElements.objects.filter(page=page)))
            response = modelutil.ModelUtil.mergeMetadatasAndElements(elements)

        if response is not None:
            return HttpResponse(json.dumps(response), content_type='application/json')

        return JsonResponse({'status': 12, 'text': 'Some parameters seem to be missed!'})

    return JsonResponse({'status': 11, 'text': 'This method processes only GET requests!'})

def saveElement(request):
    print(request)

    return JsonResponse({'status': 11, 'text': 'dick'})

def saveElements(request):
    if request.method == 'GET':
        elements = json.loads(request.GET['elements'])
        print(elements)

        for element in elements:
            metadataList = models.WebsiteElementsMetadata.objects.filter(website_element=element['pk'])

            for metadata in metadataList:
                filteredMetadata = [item for item in element['metadata'] if item['fields']['attribute'] == metadata.attribute]

                if len(filteredMetadata) > 0:
                    metadata.value = filteredMetadata[0]['fields']['value']
                    metadata.save()

    return JsonResponse({'status': 11, 'text': 'This method processes only GET requests!'})