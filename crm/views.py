from django.shortcuts import render
from .models import Order
from cms.models import CmsSlider
# Create your views here.

def first_page(request):
    object_list = Order.objects.all()
    slider_list = CmsSlider.objects.all()
    return render(request, 'crm/index.html', {'object_list': object_list, 'slider_list': slider_list})


def thanks(request):
    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name = name, order_phone = phone)
    element.save()
    return render(request, 'crm/thanks.html', {'name': name, 'phone': phone})