from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Main_Details,Personal_Details,Academic_Details,Semester_1,Semester_2,Library
from .serializer import Main_DetailsSerializer,Personal_DetailsSerializer,Academic_DetailsSerializer,Semester_1Serializer,Semester_2Serializer,LibrarySerializer


class personal_detail(APIView):

     def get_object(self, Barcode):
        try:
            return Personal_Details.objects.get(Barcode=Barcode)
        except Personal_Details.DoesNotExist:
            raise Http404

     def get(self, request, Barcode, format=None):
        snippet = self.get_object(Barcode)
        serializer = Personal_DetailsSerializer(snippet)
        return Response(serializer.data)

class academic_detail(APIView):

    def get_object(self, Barcode):
       try:
           return Academic_Details.objects.get(Barcode=Barcode)
       except Academic_Details.DoesNotExist:
           raise Http404

    def get(self, request, Barcode, format=None):
       snippet = self.get_object(Barcode=Barcode)
       serializer = Academic_DetailsSerializer(snippet)
       return Response(serializer.data)

class main_detail(APIView):

    def get_object(self, Barcode):
       try:
           return Main_Details.objects.get(Barcode=Barcode)
       except Main_Details.DoesNotExist:
           raise Http404

    def get(self, request, Barcode, format=None):
       snippet = self.get_object(Barcode)
       serializer = Main_DetailsSerializer(snippet)
       return Response(serializer.data)

class semester_1_detail(APIView):

    def get_object(self, Barcode):
       try:
           return Semester_1.objects.get(Barcode=Barcode)
       except Semester_1.DoesNotExist:
           raise Http404

    def get(self, request, Barcode, format=None):
       snippet = self.get_object(Barcode)
       serializer = Semester_1Serializer(snippet)
       return Response(serializer.data)

class semester_2_detail(APIView):

    def get_object(self, Barcode):
       try:
           return Semester_2.objects.get(Barcode=Barcode)
       except Semester_2.DoesNotExist:
           raise Http404

    def get(self, request, Barcode, format=None):
       snippet = self.get_object(Barcode)
       serializer = Semester_2Serializer(snippet)
       return Response(serializer.data)

class library_detail(APIView):

    def get_object(self, Barcode):
       try:
           return Library.objects.get(Barcode=Barcode)
       except Library.DoesNotExist:
           raise Http404

    def get(self, request, Barcode, format=None):
       snippet = self.get_object(Barcode)
       serializer = LibrarySerializer(snippet)
       return Response(serializer.data)
