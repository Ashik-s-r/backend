from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.forms import UserCreationForm

from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.authtoken.models import Token

@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
    form = UserCreationForm(data=request.data)
    if form.is_valid():
        user = form.save()
        return Response("account created successfully", status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=HTTP_200_OK)



from medicine.forms import medicineForm
from rest_framework.permissions import IsAuthenticated
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_product(request):
    form = medicineForm(request.POST)
    if form.is_valid():
        product = form.save()
        return Response({'id': product.id}, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from medicine.models import medicine
from .serializers import medicineSerializer
from rest_framework.permissions import AllowAny

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def list_products(request):
    products = medicine.objects.all()
    serializer = medicineSerializer(products, many=True)
    return Response(serializer.data)

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from medicine.forms import medicineForm
from medicine.models import medicine
from .serializers import medicineSerializer

@api_view(['PUT'])
@permission_classes((AllowAny,))
def update_product(request, pk):
    product = get_object_or_404(medicine, pk=pk)
    form = medicineForm(request.data, instance=product)
    if form.is_valid():
        form.save()
        serializer = medicineSerializer(product)
        return Response(serializer.data)
    else:
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from medicine.models import medicine
from rest_framework.permissions import AllowAny

@api_view(['DELETE'])
@permission_classes((AllowAny,))
def delete_product(request, pk):
    try:
        product = medicine.objects.get(pk=pk)
    except medicine.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    product.delete()
    return Response("deleted successfully")


@api_view(['GET'])
@permission_classes((AllowAny,))
def search_data(request, query):
    medicin1 = medicine.objects.filter(MedicineName__iexact=query)
    serializer = medicineSerializer(medicin1, many=True)
    
    if medicin1.exists():
        return Response(serializer.data)
    else:
        return Response({'message': 'Medicine not found'}, status=404)

@api_view(['GET'])
def my_model_search(request):
    search_query = request.query_params.get('search', '')
    queryset = medicine.objects.filter(name__icontains=search_query)
    serializer = medicineSerializer(queryset, many=True)
    return Response(serializer.data)

