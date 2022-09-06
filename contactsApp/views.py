from .serializer import ContactsSerializer
from rest_framework import status
from .models import Contacts
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

class ContactsList(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        career_incubator = Contacts.objects.all()
        serializer = ContactsSerializer(career_incubator, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ContactsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactsDetail(APIView):
    authentication_classes = []
    permission_classes = []
    
    def get_object(self, pk):
        try:
            return Contacts.objects.get(pk=pk)
        except Contacts.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ContactsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        career_incubator = self.get_object(pk)
        serializer = ContactsSerializer(career_incubator)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        career_incubator = self.get_object(pk)
        career_incubator.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)