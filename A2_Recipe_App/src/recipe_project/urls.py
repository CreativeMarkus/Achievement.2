from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import login_view, logout_view


def logout_success_view(request):
    from django.shortcuts import render
    return render(request, 'auth/success.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls', namespace='recipes')),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('logout-success/', logout_success_view, name='logout-success'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
