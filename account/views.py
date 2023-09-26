from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterSerializer
# Create your views here.

class Register(APIView):
    def post(self, request):
        try:
            data = request.data 
            serializer = RegisterSerializer(data=data)
            
            if not serializer.is_valid():
                return Response({
                    'data':serializer.errors,
                    'messages': 'Something went wring'
                },status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response({
                'data':{},
                'message':'Your account created successfuly'
            },status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({
                    'data':{},
                    'messages': 'Something went wring'
                },status=status.HTTP_400_BAD_REQUEST)
        
