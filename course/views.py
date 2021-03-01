from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import course
from django.db.models import Q
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')

def results(request):
    if request.method=='POST':
        sc= request.POST['course']
        if sc:
            match=course.objects.filter(Q(name__icontains=sc))
            if match:
                return render(request,'results.html',{'sc':match})
            else:
                print('Not found')
        else:
            return redirect('results')
    return render(request,'results.html')