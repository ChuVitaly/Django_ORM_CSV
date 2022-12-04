import csv
from django.http import HttpResponse
from django.shortcuts import render
from catalog_phones.models import Phone


def index(request):
    return HttpResponse("<h1>Главная страница</h1>")


# def create_catalog(request):
#     with open('catalog_phones/phones.csv', newline='') as csvfile:
#         reader = csv.DictReader(csvfile, delimiter=';')
#         for row in reader:
#             catalog = Phone(row['id'], row['name'], row['price'], row['image'], row['release_date'], row['lte_exists'])
#             catalog.save()
#         return HttpResponse("Все получилось!")


def create_page_catalog(request):
    phones = Phone.objects.all()
    return render(request, 'catalog_phones/catalog.html', {'phones': phones, 'title': 'Каталог', 'main': 'КАТАЛОГ'})
