import csv
from django.http import HttpResponse, request
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


def show_catalog(request):
    phones = Phone.objects.all()
    # sort = request.GET.get['sort']
    new = {}
    name_list = []
    value_list = []
    prices_list = []
    # sort_phones = (sorted(new.items()))
    for i in phones:
        keys_phones = [i.name]
        values_phones = [i.price, i.image]
        s = dict.fromkeys(keys_phones, values_phones)
        # print(s)
        new.update(s)
    # x = sorted(new, key=lambda i: i.name)
    # print(new[1]['Iphone X'])
    # new.sort(key=lambda d: d['name'])
    # print(x)
    # print(type(new))
    sorted_new = dict(sorted(new.items()))
    print(sorted_new.keys())
    for i in sorted_new.keys():
        name_list.append(i)
    print(name_list)
    print(type(sorted_new))
    for k in sorted_new.values():
        value_list.append(k)
    # print(value_list)
    # print(value_list[1][0])
    for i in value_list:
        prices_list.append(i[0])
    print(prices_list)
    return render(request, 'catalog_phones/cat.html', {'phones': name_list, 'prices': prices_list, 'title': 'Каталог_One', 'main': 'КАТАЛОГ_One'})




def create_page_catalog(request):
    phones = Phone.objects.all()
    return render(request, 'catalog_phones/catalog.html', {'phones': phones, 'title': 'Каталог', 'main': 'КАТАЛОГ'})


# def sort_name(request, sort='name'):
#     for s in Phone.objects.order_by('name'):
#         c = s.name
#         return HttpResponse(c)



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
