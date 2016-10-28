from rest_framework import serializers
from .models import Main_Details,Personal_Details,Academic_Details,Semester_1,Semester_2,Library

class Main_DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main_Details
        fields = ('id','Barcode','Name','Roll_No')

class Personal_DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal_Details
        fields = ('id','Barcode' , 'Name', 'Mothers_Name', 'Fathers_Name' , 'Address' , 'Contact_No', 'Email')

class Academic_DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academic_Details
        fields = ('id','Barcode', 'Branch', 'Year', 'Sem' ,'Average_CGPA')

class Semester_1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Semester_1
        fields = ('id','Barcode', 'Maths_1', 'Physics_1', 'Basic_Electrical', 'Prog_Fundamentals', 'Engg_Drawing', 'Environment')

class Semester_2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Semester_2
        fields = ('id','Barcode', 'Maths_2', 'Physics_2', 'Chemistry', 'Basic_Mechanical', 'Workshop_Practice', 'English')

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ('id','Barcode', 'Books_Isued', 'Fine_Due')
