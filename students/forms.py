from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student

        fields = [
            'admission_no',
            'name',
            'aadhaar',
            'father_name',
            'mother_name',
            'mobile',
            'student_class',
            'photo',
            'fa1',
            'fa2',
            'sa1',
            'fa3',
            'fa4',
            'sa2'
        ]