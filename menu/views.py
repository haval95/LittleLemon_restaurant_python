from django.shortcuts import render
from .models import Menu_Item, Category

def menu(request):
    query_param = request.GET.get('category', None)
    categories = Category.objects.all().order_by("category_name")
    if query_param:
        queryset = Menu_Item.objects.filter(category_id=query_param).order_by('item_name')
        item_found = queryset.exists()
    else:
        queryset = Menu_Item.objects.all().order_by('item_name')
        item_found = queryset.exists()
    context = {
    "items": queryset,
    "item_found": item_found,
    "categories": categories,
    "query_param": int(query_param) if query_param and query_param.isdigit() else None,
}

    return render(request, "menu.html", context)
    

def detail(request, id):
    queryset = Menu_Item.objects.filter(id=id).values()
    item_found = queryset.exists()
    context = {
        "item": queryset[0] if item_found else None,
        "item_found": item_found,
    }
    
    return render(request, "detail.html", context)