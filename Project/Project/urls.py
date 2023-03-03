from django.urls import path

from django.contrib import admin
from Proj1.views import userForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userform/', userForm),

]
