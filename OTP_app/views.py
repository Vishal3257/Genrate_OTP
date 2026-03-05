from datetime import timedelta
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators  import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated 
from OTP_app.serializers import  OTPRequestSerializer, OTPVerifySerializer, UserSerializer
from OTP_app.models import User
from rest_framework import generics
from django.core.mail import send_mail


# Create your views here.

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
        

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)



@api_view(['POST'])
@permission_classes([AllowAny])
def send_otp(request):
    serializer = OTPRequestSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        try:
            user = User.objects.get(email=email)
            user.generate_otp()
            subject = 'OTP'
            expire_time = user.otp_created_at + timedelta(minutes=5)
            message = f'Your OTP is: {user.otp}'
            from_email = 'vt464670@gmail.com'  
            send_mail(subject, message, from_email, [email], fail_silently=False)
            return Response({'message': 'OTP sent successfully', 'expire_time': expire_time}, status=200)
        except User.DoesNotExist:
            return Response({'error': 'User with this email does not exist'}, status=404)
    return Response(serializer.errors, status=400)



@api_view(['POST'])
@permission_classes([AllowAny])
def login_verify_otp(request):
    serializer = OTPVerifySerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        otp = serializer.validated_data['otp']
        try:
            user = User.objects.get(email=email)
            if user.otp == otp:
                user.otp = None  
                user.save()
                token,created = Token.objects.get_or_create(user=user)
                return Response({'message': 'OTP verified successfully', 'token': token.key}, status=200)
            else:
                return Response({'error': 'Invalid OTP'}, status=400)
        except User.DoesNotExist:
            return Response({'error': 'User with this email does not exist'}, status=404)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    serializer = OTPVerifySerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        otp = serializer.validated_data['otp']
        try:
            user = User.objects.get(email=email)
            if user.otp == otp:
                user.otp = None  
                user.save()
                return Response({'message': 'Login successful'}, status=200)
            else:
                return Response({'error': 'Invalid OTP'}, status=400)
        except User.DoesNotExist:
            return Response({'error': 'User with this email does not exist'}, status=404)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.otp = None
    request.user.save()
    return Response({'message': 'Logged out successfully'}, status=200)

