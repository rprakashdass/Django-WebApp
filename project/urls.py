from django.contrib import admin
from django.urls import path, include
from app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home, name='home'),  # Add this line to define the root URL pattern
    path('', include('app.urls')),
]
