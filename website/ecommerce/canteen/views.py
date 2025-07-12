from django.shortcuts import render, get_object_or_404
from .models import Canteen


def menu_list(request):
    ob_menu=Canteen.objects.all()
    return render(request, 'menu_list.html', {'menus': ob_menu})

def menu_detail(request, pk):
    ob_menu = get_object_or_404(Canteen, pk=pk)
    return render(request, 'menu_detail.html', {'menu': ob_menu})
