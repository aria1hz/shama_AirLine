from django.shortcuts import render

# Create your views here.


def contactus(request):
        return render(request,"contactus/contactus.html")
    
    
def success(request):
    if request.method=='POST':
        pm=request.POST['pm']
        print (pm)
    return render(request,"contactus/success.html")