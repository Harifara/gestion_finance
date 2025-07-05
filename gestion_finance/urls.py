from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # <-- doit être là
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),  # tes autres routes
]
