from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

from .models import Salespeople, Customers, Orders

def first(request):
    """ Выбор заказчика по имени """
    return render(request, 'variant_23/first.html')

def second(request):
    """
    23.	Вывести список номеров заказов 
        сопровождающихся именем заказчика, 
        который создавал эти заказы.
    """
    customer_name = request.POST['name']
    try:
        costomer = Customers.objects.filter(CNAME__exact = customer_name)[0]
    except:
        raise Http404('Заказчик {0} не найден!'.format(customer_name))

    orders_list = Orders.objects.filter(CNUM__exact=costomer.CNUM)

    summ = 0
    for order in orders_list:
        summ += order.AMT

    return render(request, 
        'variant_23/second.html', 
        {
            'costomer': costomer, 
            'orders_list': orders_list, 
            'summ': summ
        })
