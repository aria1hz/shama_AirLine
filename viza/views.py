from django.shortcuts import render
from .models import Viza_items
from django.core.paginator import Paginator
# Create your views here.



def viza(request):
    data =Viza_items.objects.all()
    # paginator = Paginator(data, 2)
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)
    return render(request,'viza/Viza.html', {'viza_items':data} )
# , {'page_obj':page_obj,'paginator':paginator}



def single_viza(request,slug):
    data = Viza_items.objects.all()
    return render(request,'viza/singleViza.html', {'vizaitem':data} )