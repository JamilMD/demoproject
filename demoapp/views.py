from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def demo(request):
    return render(request, "index.html")
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#     return render(request,"result.html",{'result':res,'result1':sub,'result2':mul,'result3':div})