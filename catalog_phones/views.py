import csv
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

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


def sort_phone(request):
    # phones = Phone.objects.all()
    sort = request.GET.get['sort']
        # return render(request, 'catalog_phones/catalog.html', {'phones': phones, 'title': 'Каталог', 'main': 'КАК ДЕЛА?'})
    return HttpResponse(f'Hello {sort}')

def create_page_catalog(request):
    phones = Phone.objects.all()
    return render(request, 'catalog_phones/catalog.html', {'phones': phones, 'title': 'Каталог', 'main': 'КАТАЛОГ'})





def show_product(request, id):
    name = request.GET.get('name')
    output = f'Телефон: {name}'
    return HttpResponse(output)

    # section = get_object_or_404(Phone, slug=slug)
    # sort = request.GET.getlist('sort')
    # phones = Phone.objects.all().order_by(*sort)
    # template = 'product.html'
    # context = {
    #     'section': section,
    #     'phones': phones
    # }
    # return render(request, template, context)
