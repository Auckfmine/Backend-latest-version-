from django.urls import path,include 
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('',views.DateView)
urlpatterns = [

    path('api/v1/date',include(router.urls)),
    

]




    
