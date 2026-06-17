from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Student
from .forms import StudentForm
def search_student(request):
    query = request.GET.get('q', '')

    students = Student.objects.filter(
        Q(name__icontains=query) |
        Q(admission_no__icontains=query) |
        Q(aadhaar__icontains=query)
    ) if query else []

    return render(
        request,
        'students/search.html',
        {
            'students': students,
            'query': query
        }
    )
def class_students(request, cls):

    query = request.GET.get('q', '')

    students = Student.objects.filter(
        student_class=cls
    )

    if query:
        students = students.filter(
            Q(name__icontains=query) |
            Q(admission_no__icontains=query) |
            Q(aadhaar__icontains=query)
        )

    return render(
        request,
        'students/class_students.html',
        {
            'students': students,
            'cls': cls,
            'query': query
        }
    )
def home(request):
    classes = [
        'Nursery',
        'LKG',
        'UKG',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10'
    ]
from django.shortcuts import render
from django.db.models import Q
from .models import Student

def search_student(request):
    query = request.GET.get('q', '')

    students = Student.objects.filter(
        Q(name__icontains=query) |
        Q(admission_no__icontains=query) |
        Q(aadhaar__icontains=query)
    ) if query else []

    return render(
        request,
        'students/search.html',
        {
            'students': students,
            'query': query
        }
    )
def class_students(request, cls):

    query = request.GET.get('q', '')

    students = Student.objects.filter(
        student_class=cls
    )

    if query:
        students = students.filter(
            Q(name__icontains=query) |
            Q(admission_no__icontains=query) |
            Q(aadhaar__icontains=query)
        )

    return render(
        request,
        'students/class_students.html',
        {
            'students': students,
            'cls': cls,
            'query': query
        }
    )
def home(request):
    classes = [
        'Nursery',
        'LKG',
        'UKG',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10'
    ]

    return render(
        request,
        'students/home.html',
        {
            'classes': classes
        }
    )
    return render(
        request,
        'students/home.html',
        {
            'classes': classes
        }
    )
def add_student(request):

    if request.method == 'POST':
        form = StudentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = StudentForm()

    return render(
        request,
        'students/student_form.html',
        {'form': form}
    )


def edit_student(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    if request.method == 'POST':

        form = StudentForm(
            request.POST,
            request.FILES,
            instance=student
        )

        if form.is_valid():
            form.save()
            return redirect('/')

    else:

        form = StudentForm(
            instance=student
        )

    return render(
        request,
        'students/student_form.html',
        {'form': form}
    )


def delete_student(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    student.delete()

    return redirect('/')