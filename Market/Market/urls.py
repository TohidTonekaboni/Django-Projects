from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('items/', include('item.urls')),
    path('dashboard', include('dashboard.urls')),
    path('inbox/', include('conversation.urls')),
    path("", include("core.urls"))
]
