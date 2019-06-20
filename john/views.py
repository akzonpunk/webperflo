from django.shortcuts import render, HttpResponse

# Create your views here.
def tulipan(request):
    return render(request,'john/sol.html')

def margarita(request):
    return render(request,'john/equa.html')

def girasol(request):
    return render(request,'john/bit.html')

def rosa(request):
    return render(request,'john/source.html')
