from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', homeview, name='home'),
    path('add_slide', addslide, name='add_slide'),
    path('product<int:id>', product_page, name="product_page"),
    path('category_page1', csrf_exempt(category_page1), name="category_page1"),
	path('category_page2', csrf_exempt(category_page2), name="category_page2"),
	path('category_page3', csrf_exempt(category_page3), name="category_page3"),
	path('category_page4', csrf_exempt(category_page4), name="category_page4"),
	path('category_page5', csrf_exempt(category_page5), name="category_page5"),
    path('about_us', about_us, name='about_us'),
    path('samples', samples, name="samples"),
    path('contact_us', contact_us, name='contact_us'),
	path('add-product', add_product, name="add_product"),
	path('edit_slide', edit_slide, name="edit_slide"),
    path('orders', orders, name='orders'),
    path('send-welcome-email/', send_welcome_email, name='send_welcome_email'),
    path('add_cart/<int:id>', add_cart, name="add_cart"),
    path('cart', cart, name="cart"),
    path('delete_from_cart/<int:id>', delete_from_cart, name="delete_from_cart"),
    path('open_payment', open_payment, name='open_payment'),
    path('edit-product/<int:id>', edit_product, name="edit_product"),
    path('delete-product/<int:id>', delete_product, name="delete_product"),
    path('quantum', csrf_exempt(quantum), name='quantum'),
	path('delete_order/<int:id>', delete_order, name='delete_order'),
    path('search_products', csrf_exempt(search_products), name="search_products"),
   

    # path('', homeview.as_view(), name='home'),
    # path('add_slide', AddSlide.as_view(), name='add_slide'),
	# # 
	# 
	# path('search_products', csrf_exempt(search_products), name="search_products"),
	# path('related_products', csrf_exempt(related_products), name="related_products"),
	# 
	# 

]