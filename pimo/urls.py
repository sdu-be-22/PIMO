from django.urls import include, path
from rest_framework import routers
from .views import PostViewSet, OfferViewSet, OrderViewSet
from . import views
router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet, )
router.register(r'offers', OfferViewSet, )
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('index/', views.index),
    path('index/My-Orders.html/', views.index2),
    path('index/My-Offers.html/', views.index3),
    path('index/Create-Order.html/', views.index4),
    path('index/login.html/', views.index5),
    path('index/registration.html', views.index6),
    path("logout", views.logout_request, name= "logout"),
    path("MakeOffer", views.make_offer),
    path("Offers", views.offers)
]
