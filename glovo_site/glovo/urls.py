from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'product_photos', ProductPhotosViewSet,  basename='product_photos'),

urlpatterns = [

   path('register/', RegisterView.as_view(), name='register'),
   path('login/', CustomLoginView.as_view(), name='login'),
   path('logout/', LogoutView.as_view(), name='logout'),

   path('', include(router.urls)),
   path('', StoreListApiView.as_view(), name='stores_list'),
   path('stores/<int:pk>/',  StoreDetailApiView.as_view(), name='stores_detail'),
   path('stores/create/', StoreCreateIPIView.as_view(), name='stores_create'),
   path('stores/create/<int:pk>/',StoreEDITAPIView.as_view(), name='stores_edit'),
   path('products/',  ProductListApiView.as_view(), name='products_list'),
   path('products/<int:pk>/',  ProductDetailApiView.as_view(), name='products_detail'),
   path('combo_products/', ProductComboListApiView.as_view(), name='combo_products_list'),
   path('combo_products/<int:pk>/', ProductComboDetailApiView.as_view(), name='combo_products_detail'),
   path('order/', OrderListApiView.as_view(), name='order_list'),
   path('order/<int:pk>/',  OrderDetailApiView.as_view(), name='order_detail'),
   path('user/', UserProfileListAPIView.as_view(), name='user_list'),
   path('user/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
   path('courier/', CourierListApiView.as_view(), name='courier_list'),
   path('courier/<int:pk>/',  CourierDetailApiView.as_view(),  name='courier_detail'),
   path('review/', ReviewListApiView.as_view(), name='review_list'),
   path('review/<int:pk>/',  ReviewDetailApiView.as_view(),  name='review_detail')

 ]