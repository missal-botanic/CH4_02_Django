from django.contrib import admin
from django.urls import path, include

#from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/articles/', include('articles.urls')),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/products/', include('products.urls')),
   # path('silk/', login_required(include('silk.urls', namespace='silk')))
]

urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]