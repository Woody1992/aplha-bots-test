from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import ReferralUser
from .serializers import UserSerializer, FormResultsSerializer


class UserView(APIView):
    def get(self, request, pk):
        user = ReferralUser.objects.get(referral_code=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)


class FormPostView(APIView):
    def post(self, request, format=None):
        serializer = FormResultsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



