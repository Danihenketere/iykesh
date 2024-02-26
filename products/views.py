from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.contrib import messages 
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.conf import settings
# from order.models import Order
from .utils import id_generator
import time
import json
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.

# HOME PAGE
def homeview(request):	
	if request.user.is_authenticated:
			products = Product.objects.all()
			paginator = Paginator(products, 12)
			page_number = request.GET.get('page')
			# slide = Slide.objects.get(pk=1)
			slide = Slide.objects.get()
			page_obj = Paginator.get_page(paginator, page_number)
			carts = Cart.objects.filter(user=request.user)
			context = {
				'slide':slide,
				'carts': carts,
				'products': products,
				'page_obj': page_obj,
			}
			return render(request, 'home.html', context)
	else:
			products = Product.objects.all()
			# slide = Slide.objects.get(pk=1)
			slide = Slide.objects.get()
			paginator = Paginator(products, 12)
			page_number = request.GET.get('page')
			page_obj = Paginator.get_page(paginator, page_number)
			context = {
				'slide':slide,
				'products': products,
				'page_obj': page_obj,
				}
			return render(request, 'home.html', context)
	
# PRODUCT PAGE
def product_page(request, id):
	if request.user.is_authenticated:
		products = Product.objects.all()
		product = Product.objects.get(pk=id)
		carts = Cart.objects.filter(user=request.user)
		paginator = Paginator(products, 12)
		page_number = request.GET.get('page')
		page_obj = Paginator.get_page(paginator, page_number)
		context = {
		'carts': carts,
		'product': product,
		'page_obj': page_obj,
		}
		return render(request, 'product_page.html', context)
	else:
		products = Product.objects.all()
		product = Product.objects.get(pk=id)

		paginator = Paginator(products, 12)
		page_number = request.GET.get('page')
		page_obj = Paginator.get_page(paginator, page_number)
		context = {
		'product': product,
		'page_obj': page_obj,
		}
		return render(request, 'product_page.html', context)

# ADD PRODUCT
@login_required
def add_product(request):
	if request.method == 'POST':
		name = request.POST['product_name']
		category = request.POST['category']
		mode = request.POST['mode']
		sub_category = request.POST.get('sub-category')
		description = request.POST['description']
		initial_price = request.POST['initial_price']
		final_price = request.POST['current_price']
		original_pics = request.FILES.get('original_picture')
		pics1 = request.FILES.get('pic1')
		pics2 = request.FILES.get('pic2')
		pics3 = request.FILES.get('pic3')


		product = Product(name=name, category=category,mode=mode, sub_category=sub_category,  description=description, initial_price=initial_price, final_price=final_price, original_pics=original_pics, pics1=pics1, pics2=pics2, pics3=pics3)
		product.save()
		messages.success(request, 'Product saved successfully')
		return render(request, 'add_product.html')

	return render(request, 'add_product.html')



# EDIT PRODUCT
@login_required
def edit_product(request, id):
	product = Product.objects.get(pk=id)
	if request.method == 'POST':
		name = request.POST['product_name']
		category = request.POST['category']
		mode = request.POST['mode']
		sub_category = request.POST.get('sub-category')
		description = request.POST['description']
		initial_price = request.POST['initial_price']
		final_price = request.POST['current_price']
		original_pics = request.FILES.get('original_picture')
		pics1 = request.FILES.get('pic1')
		pics2 = request.FILES.get('pic2')
		pics3 = request.FILES.get('pic3')


		product.name = name
		product.category = category
		product.sub_category = sub_category
		product.mode = mode
		product.description = description
		product.initial_price = initial_price
		product.final_price = final_price
		product.original_pics = original_pics
		product.pics1 = pics1
		product.pics2 = pics2
		product.pics3 = pics3

		product.save()
		messages.success(request, 'Product updated successfully')
		return redirect('home')



	context = {
	'product': product,
	'values': product,
	}

	return render(request, 'edit_product.html', context)

# DELETE PRODUCT
@login_required
def delete_product(request, id):
	product = Product.objects.get(pk=id)
	product.delete()
	messages.success(request, 'Expense deleted succesfully')
	return redirect('home')

# ADD SLIDE
def addslide(request):
	if request.method == 'POST':
		slide1 = request.FILES.get('slide1')
		slide1_heading = request.POST['slide1_heading']
		slide1_subheading = request.POST['slide1_subheading']
		slide1_writeup = request.POST['slide1_writeup']
            
		slide2 = request.FILES.get('slide2')
		slide2_heading = request.POST['slide2_heading']
		slide2_subheading = request.POST['slide2_subheading']
		slide2_writeup = request.POST['slide2_writeup']
		
		slide3 = request.FILES.get('slide3')
		slide3_heading = request.POST['slide3_heading']
		slide3_subheading = request.POST['slide3_subheading']
		slide3_writeup = request.POST['slide3_writeup']
		

		slide4 = request.FILES.get('slide4')
		slide4_heading = request.POST['slide4_heading']
		slide4_subheading = request.POST['slide4_subheading']
		slide4_writeup = request.POST['slide4_writeup']

		slide = Slide(slide1pics=slide1, slide1heading=slide1_heading,slide1subheading=slide1_subheading, slide1writeup=slide1_writeup,\
					slide2pics=slide2, slide2heading=slide2_heading,slide2subheading=slide2_subheading, slide2writeup=slide2_writeup,\
					slide3pics=slide3, slide3heading=slide3_heading,slide3subheading=slide3_subheading, slide3writeup=slide3_writeup,\
					slide4pics=slide4, slide4heading=slide4_heading,slide4subheading=slide4_subheading, slide4writeup=slide4_writeup,\
		)
		slide.save()
		messages.success(request, 'Product saved successfully')
		return render(request, 'add_slide.html')

	return render(request, 'add_slide.html')

# MATERIAL CATEGORY
def category_page1(request):
	if request.user.is_authenticated:
		products = Product.objects.filter(category='Material')
		paginator = Paginator(products, 12)
		page_number = request.GET.get('page')
		# slide = Slide.objects.get(pk=1)
		slide = Slide.objects.get()
		page_obj = Paginator.get_page(paginator, page_number)
		carts = Cart.objects.filter(user=request.user)
		context = {
			'cat': 'Material',
			'slide':slide,
			'carts': carts,
			'products': products,
			'page_obj': page_obj,
		}
		return render(request, 'category_page.html', context)
	else:
		products = Product.objects.filter(category='Material')
		# slide = Slide.objects.get(pk=1)
		slide = Slide.objects.get()
		paginator = Paginator(products, 12)
		page_number = request.GET.get('page')
		page_obj = Paginator.get_page(paginator, page_number)
		context = {
			'cat': 'Material',
			'slide':slide,
			'products': products,
			'page_obj': page_obj,
			}
		return render(request, 'category_page.html', context)
	
# FOAM CATEGORY
def category_page2(request):
	if request.user.is_authenticated:
		products = Product.objects.filter(category='Foam')
		paginator = Paginator(products, 12)
		page_number = request.GET.get('page')
		# slide = Slide.objects.get(pk=1)
		slide = Slide.objects.get()
		page_obj = Paginator.get_page(paginator, page_number)
		carts = Cart.objects.filter(user=request.user)
		context = {
			'cat': 'Foam',
			'slide':slide,
			'carts': carts,
			'products': products,
			'page_obj': page_obj,
		}
		return render(request, 'category_page.html', context)
	else:
		products = Product.objects.filter(category='Foam')
		# slide = Slide.objects.get(pk=1)
		slide = Slide.objects.get()
		paginator = Paginator(products, 12)
		page_number = request.GET.get('page')
		page_obj = Paginator.get_page(paginator, page_number)
		context = {
			'cat': 'Foam',
			'slide':slide,
			'products': products,
			'page_obj': page_obj,
			}
		return render(request, 'category_page.html', context)

# TOOL CATEGORY
def category_page3(request):
	if request.user.is_authenticated:
		products = Product.objects.filter(category='Tool')
		paginator = Paginator(products, 12)
		page_number = request.GET.get('page')
		# slide = Slide.objects.get(pk=1)
		slide = Slide.objects.get()
		page_obj = Paginator.get_page(paginator, page_number)
		carts = Cart.objects.filter(user=request.user)
		context = {
			'cat': 'Tool',
			'slide':slide,
			'carts': carts,
			'products': products,
			'page_obj': page_obj,
		}
		return render(request, 'category_page.html', context)
	else:
		products = Product.objects.filter(category='Tool')
		# slide = Slide.objects.get(pk=1)
		slide = Slide.objects.get()
		paginator = Paginator(products, 12)
		page_number = request.GET.get('page')
		page_obj = Paginator.get_page(paginator, page_number)
		context = {
			'cat': 'Tool',
			'slide':slide,
			'products': products,
			'page_obj': page_obj,
			}
		return render(request, 'category_page.html', context)

# WOOD CATEGORY
def category_page4(request):
	if request.user.is_authenticated:
		products = Product.objects.filter(category='Wood')
		paginator = Paginator(products, 12)
		page_number = request.GET.get('page')
		# slide = Slide.objects.get(pk=1)
		slide = Slide.objects.get()
		page_obj = Paginator.get_page(paginator, page_number)
		carts = Cart.objects.filter(user=request.user)
		context = {
			'cat': 'Wood',
			'slide':slide,
			'carts': carts,
			'products': products,
			'page_obj': page_obj,
		}
		return render(request, 'category_page.html', context)
	else:
		products = Product.objects.filter(category='Wood')
		# slide = Slide.objects.get(pk=1)
		slide = Slide.objects.get()
		paginator = Paginator(products, 12)
		page_number = request.GET.get('page')
		page_obj = Paginator.get_page(paginator, page_number)
		context = {
			'cat': 'Wood',
			'slide':slide,
			'products': products,
			'page_obj': page_obj,
			}
		return render(request, 'category_page.html', context)

# FURNITURE CATEGORY
def category_page5(request):
	if request.user.is_authenticated:
		products = Product.objects.filter(category='Furniture')
		paginator = Paginator(products, 12)
		page_number = request.GET.get('page')
		# slide = Slide.objects.get(pk=1)
		slide = Slide.objects.get()
		page_obj = Paginator.get_page(paginator, page_number)
		carts = Cart.objects.filter(user=request.user)
		context = {
			'cat': 'Wood',
			'slide':slide,
			'carts': carts,
			'products': products,
			'page_obj': page_obj,
		}
		return render(request, 'category_page.html', context)
	else:
		products = Product.objects.filter(category='Furniture')
		# slide = Slide.objects.get(pk=1)
		slide = Slide.objects.get()
		paginator = Paginator(products, 12)
		page_number = request.GET.get('page')
		page_obj = Paginator.get_page(paginator, page_number)
		context = {
			'cat': 'Wood',
			'slide':slide,
			'products': products,
			'page_obj': page_obj,
			}
		return render(request, 'category_page.html', context)
	
# ABOUT US	
def about_us(request):
	return render(request, 'about_us.html')


# SAMPLES
def samples(request):
	if request.user.is_authenticated:
		products = Product.objects.all()
		carts = Cart.objects.filter(user=request.user)
		context = {
		'carts': carts,
		'products': products,
		}
		return render(request, 'samples.html', context)
	else:
		products = Product.objects.all()
		context = {
		'products': products,
		}
		return render(request, 'samples.html', context)
	

# CONTACT US
def contact_us(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		send_mail(
			message_name,# subject
			message,# message
			message_email,# from
			[settings.EMAIL_HOST_USER],#to
			)

		return render(request, 'contact_us.html', {
			"message_name": message_name,
			})
	else:
		return render(request, 'contact_us.html', {})
	


# EDIT SLIDE
def edit_slide(request):
	# slide = Slide.objects.get(pk=1)
	slide = Slide.objects.get()

	if request.method == 'POST':
		slide.slide1heading = request.POST['slide1heading']
		slide.slide2heading = request.POST['slide2heading']
		slide.slide3heading = request.POST['slide3heading']
		slide.slide4heading = request.POST['slide4heading']

		slide.slide1subheading = request.POST['slide1subheading']
		slide.slide2subheading = request.POST['slide2subheading']
		slide.slide3subheading = request.POST['slide3subheading']
		slide.slide4subheading = request.POST['slide4subheading']

		slide.slide1writeup = request.POST['slide1writeup']
		slide.slide2writeup = request.POST['slide2writeup']
		slide.slide3writeup = request.POST['slide3writeup']
		slide.slide4writeup = request.POST['slide4writeup']

		slide.slide1pics = request.FILES.get('slide1pics')
		slide.slide2pics = request.FILES.get('slide2pics')
		slide.slide3pics = request.FILES.get('slide3pics')
		slide.slide4pics = request.FILES.get('slide4pics')
		slide.save()
		context = {
			'value': slide,
		}
		messages.success(request, 'Product updated successfully')
		return render(request, 'edit_slide.html', context)
	context = {
	'value': slide,
	}

	return render(request, 'edit_slide.html', context)

# ORDER
def orders(request):
	orders = Order.objects.all()

	context = {
	'orders': orders,
	}
	return render(request, 'orders.html', context)

from django.core.mail import send_mail

def send_welcome_email(request):
    subject = 'Welcome to My Site'
    message = 'Thank you for creating an account!'
    from_email = 'nwankwodaniel287@gmail.com'
    recipient_list = ['nwankwodaniel287@gmail.com']
    send_mail(subject, message, from_email, recipient_list)
	
    return redirect('home')

# ADD Cart
from django.http import JsonResponse
@login_required
def add_cart(request, id):
	product = Product.objects.get(pk=id)
	chec = Cart.objects.filter(product=product, user=request.user).exists()
	print(chec)
	if chec:
		# messages.success(request, 'Product already in the cart')
		# return redirect('home')
		return JsonResponse({'message_error': 'Product already in the cart'}, status=400)

    		
	else:
		cart = Cart()
		cart.product = product
		cart.user = request.user
		cart.save()
		# messages.success(request, 'Product added to the cart')
		# return redirect('home')
		return JsonResponse({'message_success': 'Product Added to Cart'})
	

		# if not str(username).isalnum():
		# 	return JsonResponse({'username_error_message': 'The username most be an alpha numeric number'}, status=400)


		# if User.objects.filter(username=username).exists():
		# 	return JsonResponse({'username_error_message': 'Sorry username is used, chose another one'}, status=409)

# 		# return JsonResponse({'username_validate': True})
	
# CART
def cart(request):
	if request.user.is_authenticated:
		carts = Cart.objects.filter(user=request.user)

		context = {
		'carts': carts,
		}
		return render(request, 'cart.html', context)
	else:
		return render(request, 'cart.html', context)

# DELETE FROM CART
@login_required
def delete_from_cart(request, id):
	product = Product.objects.get(pk=id)
	cart = Cart.objects.filter(product=product, user = request.user)
	cart.delete()
	return redirect('cart')


# OPEN PAYMENT
@login_required
def open_payment(request):
	if request. method == 'POST':
		totalcost = request.POST.get('totalcost')
		carts = Cart.objects.filter(user=request.user)
		order_id = id_generator()
	
		for cart in carts:
			Order.objects.create(total_price=totalcost,item=cart.product.name,\
			rate=cart.product.final_price, order_id=order_id, username=cart.user.username, email=cart.user.email,quantity=cart.quantity)
		carts.delete()
	return render(request, 'index.html',{
		'totalcost': totalcost,
		'pk_public': settings.PAYSTACK_PUBLIC_KEY,})


# DELETE PRODUCT
@login_required
def delete_product(request, id):
	product = Product.objects.get(pk=id)
	product.delete()
	messages.success(request, 'Expense deleted succesfully')
	return redirect('home')

# SEARCH PRODUCT
def search_products(request):
	if request.method == 'POST':
		search_str = json.loads(request.body).get('searchText', '')
		products = Product.objects.filter(name__icontains = search_str) | Product.objects.filter(
			initial_price__istartswith = search_str) | Product.objects.filter(
			description__icontains = search_str) | Product.objects.filter(
			category__icontains = search_str) | Product.objects.filter(
			sub_category__icontains = search_str) | Product.objects.filter(
			mode__icontains = search_str) | Product.objects.filter(
			final_price__istartswith = search_str)
		data = products.values()
		return JsonResponse(list(data), safe= False)


# RELATED PRODUCT
def related_products(request):

	if request.method == 'POST':
		search_str = json.loads(request.body).get('searchText')
		product = Product.objects.get(pk=search_str)
		products = Product.objects.filter(sub_category__icontains = product.sub_category) 
		data = products.values()
		return JsonResponse(list(data), safe= False)
	
# QUANTUM
@login_required
def quantum(request):

	if request.method == 'POST':
		user_id = json.loads(request.body).get('user_id')
		cart_id = json.loads(request.body).get('cart_id')
		quantity = json.loads(request.body).get('quantity')
		cart = Cart.objects.get(pk=cart_id)
		cart.quantity = quantity
		cart.save()
		return JsonResponse({"message": "Cart updated"})


# DELETE ORDER
def delete_order(request, id):
	try:
		order = Order.objects.get(pk=id)
		order.delete()
		orders = Order.objects.all()

		context = {
		'orders': orders,
		}
		return render(request, 'orders.html', context)
	except:
		return HttpResponse('<h1 style="color: red;">No such page in existence</h1>')
	