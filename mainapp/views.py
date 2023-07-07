from django.shortcuts import render
import pandas as pd
from .forms import ExcelFileForm
from openpyxl import load_workbook
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
#from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer
from rest_framework import permissions, status
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required, permission_required
from .models import ExcelFile
from .serializers import ExcelFileSerializer
from rest_framework import generics


class ExcelFileListView(generics.ListAPIView):
    serializer_class = ExcelFileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        queryset = ExcelFile.objects.filter(user=current_user)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset:
            message = "You have not yet uploaded a file."
            return Response({"message": message})
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


'''class ExcelFileListView(generics.ListAPIView):
    serializer_class = ExcelFileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        return ExcelFile.objects.filter(user=current_user)'''




#uploading file
def upload_excel(request):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    if request.method == 'POST':
        form = ExcelFileForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = form.save(commit=False)
            excel_file.user = request.user  # Assign the user who uploaded the file
            excel_file.save()

            #excel_file = form.save()  # Save the uploaded file to the database

            # Read the uploaded Excel file using Pandas
            df = pd.read_excel(excel_file.file.path)

            # Get the column names from the DataFrame
            column_names = df.columns.tolist()

            # Get the number of rows and columns
            num_rows = df.shape[0]
            num_cols = df.shape[1]

            # Open the workbook using openpyxl to access additional properties
            workbook = load_workbook(excel_file.file.path)
            sheet = workbook.active

            # Get the name of the active sheet
            sheet_name = sheet.title

           # Get the data types of all cells
            data_types = df.dtypes.to_dict()

            # Display a success message along with the column names
            success_message = 'Excel file uploaded successfully'
            return render(request, 'mainapp/index.html', {'form': form, 'success_message': success_message, 'column_names': column_names})
    else:
        form = ExcelFileForm()
    
    return render(request, 'mainapp/index.html', {'form': form})



#Check uploaded file
'''def check_upload_file(request):
    current_user = request.user
    uploaded_files = ExcelFile.objects.filter(user=current_user)

    file_info = []
    for file in uploaded_files:
        file_info.append({
            'file_name': file.file.name,
            'uploaded_at': file.uploaded_at,
            # Add additional file information here if needed
        })

    return JsonResponse(file_info, safe=False)
'''

def react_template(request):
    return render(request, 'mainapp/react.html')

def home_view(request):
    return render(request, 'mainapp/react.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid credentials'})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})
'''

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid credentials'})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})
def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('mainapp/react.html')  # Replace 'home' with the URL name of your HomePage view

        error_message = 'Invalid credentials'
    else:
        error_message = 'Invalid request method'

    return JsonResponse({'success': False, 'error': error_message})
'''