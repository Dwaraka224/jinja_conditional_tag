from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':200,'b':30,'c':40}
    return render(request,'nestedif.html',context=d)