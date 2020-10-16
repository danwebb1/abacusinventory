from django.urls import include, path

urlpatterns = [
    path(r'v1/inventory/', include('api.urls')),
]
