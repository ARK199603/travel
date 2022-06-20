from django.shortcuts import render
from .models import Place
from .models import Fun
# Create your views here.


def demo(request):
    obj = Place.objects.all()
    obj1= Fun.objects.all()
    return render(request, 'index.html', {'result': obj,
                                          'res':obj1})
