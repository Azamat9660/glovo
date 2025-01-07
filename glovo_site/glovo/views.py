from rest_framework import viewsets, permissions, generics,status
from .serializers import *
from .models import *
from .filters import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({'detail': 'Неверные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

class UserProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSimpleSerializers


class StoreListApiView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = StoreFilter
    search_fields = ['store_name']
    permission_classes = [permissions.IsAuthenticated]


class StoreDetailApiView(generics.RetrieveUpdateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreDetailSerializers
    permission_classes = [permissions.IsAuthenticated]


class StoreCreateIPIView(generics.CreateAPIView):
    serializer_class = StoreSerializers


class StoreEDITAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers

class ProductListApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['store_name']
    ordering_fields = ['price']



class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializers


class ProductComboListApiView(generics.ListAPIView):
    queryset = ProductCombo.objects.all()
    serializer_class = ProductComboListSerializers


class ProductComboDetailApiView(generics.RetrieveAPIView):
    queryset = ProductCombo.objects.all()
    serializer_class = ProductComboDetailSerializers


class ProductPhotosViewSet(viewsets.ModelViewSet):
    queryset = ProductPhotos.objects.all()
    serializer_class = ProductPhotosSerializer



class OrderListApiView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializers


class OrderDetailApiView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializers



class CourierListApiView(generics.ListAPIView):
    queryset = Courier.objects.all()
    serializer_class = CourierListSerializers


class CourierDetailApiView(generics.RetrieveAPIView):
    queryset = Courier.objects.all()
    serializer_class = CourierDetailSerializers



class ReviewListApiView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializers


class ReviewDetailApiView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializers