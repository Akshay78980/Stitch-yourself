from django.urls import path
from products.views import GetAvailableSizesAPI

urlpatterns = [
    path('product-sizes/<str:group_sku_number>/<str:product_color>/',GetAvailableSizesAPI.as_view(), name="get_available_sizes"),
]