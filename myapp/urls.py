from django.urls import path
from myapp import views

urlpatterns=[
    path('', views.home, name='home'),
    path('create_pdf/', views.pdf_report_create, name='create_pdf')
]