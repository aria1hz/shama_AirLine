from django.shortcuts import render,redirect
from.models import Bus
from account.models import User
from persiantools.jdatetime import JalaliDate



def home(request):
    return render(request,"home/index.html")
def loged(request):
    # namesss=User.objects.all()
    return render(request,"home/loged.html")
def ticket(request):
    data=Bus.objects.all()
    startt=request.GET.get("startt")
    endd=request.GET.get("endd")
    movee=request.GET.get("movee")
    
    if startt !='' and startt is not None:
        data=data.filter(start__icontains=startt)
    if endd !='' and endd is not None:
        data=data.filter(end__icontains=endd)
    if movee !='' and movee is JalaliDate:
        movee = JalaliDate.to_gregorian()
        data=data.filter(movetime__icontains=movee)
    if endd =='' :
        return render(request,"home/index.html")
    if startt =='' :
        return render(request,"home/index.html")
    else:
        context={
            'tickets':data
        }
        return render(request,"home/tickets.html",context)
    


    # query_dict=request.GET
    # query=query_dict.get('searched')
    # article_obj=None
    # if query is not None:
    #     article_obj=Bus.objects.get(start=query)
    # context={
    #     'object':article_obj
    # }

# def search(request):
#     if request.method=='POST':
#         searched=request.POST['searched']
#         venues=Bus.objects.filter(start=searched)
#         return render(request,"home/tickets.html",{'searched':searched},{'venues':venues})
#     else:
#         return render(request,"home/index.html")