from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
# Create your views here.


@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        users= User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_by_nick(request, nick):
    try:
        user= User.objects.get(pk=nick)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    # Deletando User
    if request.method == 'DELETE':
        try:
            print(request.data)
            user_to_delete = User.objects.get(pk=nick)
            user_to_delete.delete()
            return Response( status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST', 'PUT', ])
def user_manager(request):
    # Pegar user especifico
    if request.method == 'GET':
        try:
            if request.GET['user']:
                user_nickname = request.GET['user']
                try:
                    user= User.objects.get(pk=user_nickname)
                except: 
                    return Response(status=status.HTTP_404_NOT_FOUND)
                
                serializer = UserSerializer(user)
                return Response(serializer.data)  
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    # Criar user
    if request.method == 'POST':
        
        new_user = request.data
        serializer = UserSerializer(data=new_user)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        

    # Editando user
    if request.method == 'PUT':
        nickname = request.data['User_nickname']
        try:
            update_user = User.objects.get(pk=nickname)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(update_user,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
    
    