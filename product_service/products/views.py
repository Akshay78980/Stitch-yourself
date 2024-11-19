from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView

from .models import Category, Product, ProductVariant
from .serializers import CategorySerializer, ProductSerializer, ProductVariantSerializer

from rest_framework.response import Response

from django.views.generic import TemplateView
# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductVariantViewSet(viewsets.ModelViewSet):
    queryset = ProductVariant.objects.all().distinct('product','color')
    serializer_class = ProductVariantSerializer



class ProductListView(TemplateView):
    template_name = 'product_list.html'

class ProductView(TemplateView):
    template_name = 'product_view.html'


class GetAvailableSizesAPI(APIView):
    def get(self, request,group_sku_number,product_color):
        size_order = ['XS','S','M','L','XL','XXL','XXXL']
        sizes = ProductVariant.objects.filter(product__group_sku_number=group_sku_number,color=product_color).values_list('size',flat=True).distinct()
        sizes_list = list(sizes)
        sorted_list = sorted(sizes_list,key=lambda size: size_order.index(size),reverse=False)
        return Response({'sizes': sorted_list})
    

# def getAvailableStockCount(request,id):
#     if request.method == 'GET' and id is not None:
#         stock_count = ProductVariant.objects.get(id=id).quantity

#         return Response({'available_stock':stock_count})

