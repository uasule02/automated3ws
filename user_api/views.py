from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer, ExcelFileSerializer
from rest_framework import permissions, status
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from .models import ExcelFile
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from .validations import custom_validation, validate_email, validate_password

class get_current_user(APIView):
    def get(self, request):
        user = request.user
        data = {
            'email': user.email,
            'username': user.username,
        }
        return JsonResponse(data)


class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

'''class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(status=status.HTTP_200_OK)'''

class UserLogin(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = (SessionAuthentication,)
	##
	def post(self, request):
		data = request.data
		assert validate_email(data)
		assert validate_password(data)
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.check_user(data)
			login(request, user)
			return Response(serializer.data, status=status.HTTP_200_OK)


class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)

class ExcelFileListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        excel_files = ExcelFile.objects.filter(user=request.user)
        serializer = ExcelFileSerializer(excel_files, many=True)
        return Response(serializer.data)

class ExcelFileUploadView(APIView):
    
    #authentication_classes = (SessionAuthentication,)
    def post(self, request):
        serializer = ExcelFileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

'''
class ExcelFileUploadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ExcelFileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

'''


'''from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer, ExcelFileSerializer
from rest_framework import permissions, status
from .validations import custom_validation, validate_email, validate_password
from rest_framework import generics
from .models import ExcelFile, AppUser
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.exceptions import ValidationError

class UserRegister(APIView):
	permission_classes = (permissions.AllowAny,)
	def post(self, request):
		clean_data = custom_validation(request.data)
		serializer = UserRegisterSerializer(data=clean_data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.create(clean_data)
			if user:
				return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data
        assert validate_email(data)
        assert validate_password(data)

        email = data['email']
        password = data['password']
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            raise ValidationError('Invalid credentials')


class UserLogout(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = ()
	def post(self, request):
		logout(request)
		return Response(status=status.HTTP_200_OK)


class UserView(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)
	##
	def get(self, request):
		serializer = UserSerializer(request.user)
		return Response({'user': serializer.data}, status=status.HTTP_200_OK)

class ExcelFileListView(generics.ListAPIView):
    serializer_class = ExcelFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ExcelFile.objects.filter(user=self.request.user)

class ExcelFileUploadView(generics.CreateAPIView):
    serializer_class = ExcelFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Skip authentication and assume login is successful
        user = AppUser.objects.get_or_create(username=username)[0]
        login(request, user)
        return JsonResponse({'message': 'Login successful'}) 
		'''

'''class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        data = request.data
        try:
            assert validate_email(data)
            assert validate_password(data)
        except AssertionError:
            return Response(
                {'error': 'Invalid email or password.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid():
            user = serializer.check_user(data)
            if user is not None:
                login(request, user)
                return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(
            {'error': 'Invalid email or password.'},
            status=status.HTTP_400_BAD_REQUEST
        )
'''
