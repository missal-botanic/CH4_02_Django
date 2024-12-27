
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


from django.core.cache import cache # 추가

@api_view(["GET"])
def product_list(request):
    cache_key = "product_list" # 
    print(cache_key)

    if not cache.get(cache_key): # 캐시에 없을 경우
        print("cache miss")
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        json_response = serializer.data
        cache.set(cache_key, json_response, 10) # key, value cache.set(cache_key, json_response, 5) 캐시 5초 만료
    
    response_data = cache.get(cache_key)
    return Response(response_data)

