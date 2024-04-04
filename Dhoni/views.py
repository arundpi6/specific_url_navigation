from django.shortcuts import render

# Create your views here.
def captain(request):
    return render(request,'captain.html')