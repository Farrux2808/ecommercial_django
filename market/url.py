from django.contrib import admin
from django.conf.urls import url
from .views import add_category
from .views import get_categorys
from .views import get_category
from .views import del_category
from .views import update_category
from .views import add_measurement
from .views import get_measurements
from .views import get_measurement
from .views import del_measurement
from .views import update_measurement
from .views import add_product
from .views import get_products

app_name = 'flight'

urlpatterns = [
    url(r'^addcategory/$', add_category),
    url(r'^getcategorys/$', get_categorys),
    url(r'^getcategory/$', get_category),
    url(r'^delcategory/$', del_category),
    url(r'^updatecategory/$', update_category),
    url(r'^addmeasurement/$', add_measurement),
    url(r'^getmeasurements/$', get_measurements),
    url(r'^getmeasurement/$', get_measurement),
    url(r'^delmeasurement/$', del_measurement),
    url(r'^updatemeasurement/$', update_measurement),
    url(r'^addproduct/$', add_product),
    url(r'^getproducts/$', get_products)

]