from django.shortcuts import render

# Create your views here.
def bime(request):
    return render(request,'bime/bime.html')