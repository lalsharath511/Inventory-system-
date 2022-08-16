from django.urls import path
from .views import *
urlpatterns = [
    path('',log,name="login"),
    path('add_pro',inventory,name="add_pro"),
    path('prolist',product_list,name="prolist"),
    path('delpo/<poid>',del_product,name='delpo'),
    path('productedit/<int:id>', productedit, name='productedit'),
    path('productupdate/<int:id>', productupdate, name='productupdate'),
    
]