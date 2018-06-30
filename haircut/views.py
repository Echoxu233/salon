from django.shortcuts import render 
from .models import Order

def home_page(request): 

    if request.method == "GET": 
        return render(request, 'haircut/home_page.html')  

    if request.method == "POST": 
        our_barber = request.POST.get("barber")
        our_customer = request.POST.get("customer")
        our_time = request.POST.get("time")
        order = Order.objects.create(
            barber=our_barber,
            customer=our_customer,
            time=our_time
        )
        all_orders = Order.objects.all()
        context = {'orders': all_orders}
        
        return render(request, 'haircut/home_page.html', context)

    all_orders = Order.objects.all()
    context = {'orders': all_orders}
    return render(request, 'haircut/home_page.html', context)
