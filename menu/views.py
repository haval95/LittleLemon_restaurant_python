from django.shortcuts import render
from .models import Menu_Item

def menu(request):
    query_param = request.GET.get('category', None)
    if query_param:
        queryset = Menu_Item.objects.filter(category_id=query_param).order_by('item_name')
    else:
        queryset = Menu_Item.objects.all().order_by('item_name')
    item_found = queryset.exists()
    context = {
        "items": queryset,
        'item_found': item_found
    }
    return render(request, "menu.html", context)
    
