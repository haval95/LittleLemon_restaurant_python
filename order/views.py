from django.shortcuts import render
from .models import order
import json
from django.http import JsonResponse
from menu import models
def add_to_cart(request, item_id):
    if request.method == 'GET':
        cart = request.session.get('cart', {})
        total_price = request.session.get('total_price', 0)

        if str(item_id) in cart:
            # Item already exists in the cart, increase the quantity
            cart[str(item_id)].update({
                'quantity': cart[str(item_id)]['quantity'] + 1,
            })
        else:
            # Item doesn't exist in the cart, add a new entry
            cart[str(item_id)] = {
                'id': item_id,
                'quantity': 1,
            }

        item = models.Menu_Item.objects.get(id=item_id)
        cart[str(item_id)].update({
            'name': item.item_name,
            'price': item.item_price,
            'image': item.image.url,
        })

        total_price += item.item_price

        request.session['cart'] = cart
        request.session['total_price'] = total_price
        request.session.save()
        response_data = {
            'status': 'success',
            'message': 'Item added to cart successfully.',
        }
        print(cart)
        return JsonResponse(response_data, status=204)
    

    
    
def Order(request):
    if request.method == "GET":
        queryset = None
        item_found = False
        if request.GET.get('table'):
            table = request.GET.get('table')
            queryset = order.objects.filter(table_number=table, is_deliverd=False)
            item_found = queryset.exists()

        context = {
            "orders": queryset,
            "item_found": item_found
        }
        

            
        return render(request, "order.html", context)
            
            
        
