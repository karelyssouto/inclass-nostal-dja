from django.shortcuts import render
from .models import Decade, Fads
# Create your views here.


def decade_index(request):
    decades = Decade.objects.all()
    return render(request, 'nostaldja/decade_index.html', {'decades': decades})
