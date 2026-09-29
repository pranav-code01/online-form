from django.contrib import admin
from django.urls import path
from forms.views import home, create_form, view_form, responses, login_view, register_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('create/', create_form, name='create_form'),

    path('form/<int:form_id>/', view_form, name='view_form'),

    path('responses/<int:form_id>/', responses, name='responses'),
    
    path('login/', login_view, name='login'),

    path('register/', register_view, name='register'),

    path('logout/', logout_view, name='logout'),
]