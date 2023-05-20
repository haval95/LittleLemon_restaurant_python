from django.shortcuts import render, redirect
from .models import order, table
from django.http import JsonResponse
from menu import models
from django.contrib import messages

def add_to_cart(request, item_id):
    cart = request.session.get("cart", {})
    total_price = request.session.get("total_price", 0)
    if request.method == "GET":
        if str(item_id) in cart:
            cart[str(item_id)].update(
                {
                    "quantity": cart[str(item_id)]["quantity"] + 1,
                }
            )
        else:
            cart[str(item_id)] = {
                "id": item_id,
                "quantity": 1,
            }

        item = models.Menu_Item.objects.get(id=item_id)
        cart[str(item_id)].update(
            {
                "name": item.item_name,
                "price": item.item_price,
                "image": item.image.url,
            }
        )

        total_price += item.item_price
    elif request.method == "POST":
        if str(item_id) in cart:
            if cart[str(item_id)]["quantity"] > 1:
                cart[str(item_id)]["quantity"] -= 1
                total_price -= cart[str(item_id)]["price"]
            else:
                item = models.Menu_Item.objects.get(id=item_id)
                del cart[str(item_id)]
                total_price -= item.item_price

    request.session["cart"] = cart
    request.session["total_price"] = total_price
    request.session.save()
    messages.success(request, 'Your message here.')
    return redirect(request.META.get("HTTP_REFERER"))


def Cart(request):
    return render(request, "cart.html")


def Order(request):
    if request.method == "POST":
        cart = request.session.get("cart", {})
        table_num = int(request.POST.get("table-number"))
        table_num = table.objects.get(table_number=table_num)
        myOrder = order.objects.create(table_number=table_num)
        myOrder.save()
        for key, value in cart.items():
            item_id = key
            item = models.Menu_Item.objects.get(id=item_id)
            myOrder.ord_items.add(item)
        del request.session['cart']
        del request.session['total_price']
        return redirect(request.META.get("HTTP_REFERER"))
    
