from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,"Main_app/register.html")