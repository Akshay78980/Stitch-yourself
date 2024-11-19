from rest_framework import serializers
from .models import Brand, Category, Product, ProductVariant

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'   

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model= Brand
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'




class ProductVariantSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model=ProductVariant
        fields = ('id','product','description','color','size','quantity',
                  'variant_price', 'image1', 'image2', 'image3', 'image4', 'image5')

    
