from django.urls import path,include
from .views import CakeRUDView,CakeAPIView,CakeListAPIView

urlpatterns = [
   
     path('',CakeListAPIView.as_view()),
      path('<pk>',CakeRUDView.as_view()), 
    
]
