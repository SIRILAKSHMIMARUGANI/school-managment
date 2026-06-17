from django.urls import path
from . import views

urlpatterns = [
    path(
    'login/',
    views.admin_login,
    name='login'
),

path(
    'logout/',
    views.admin_logout,
    name='logout'
),

    path('', views.home, name='home'),

    path(
        'search/',
        views.search_student,
        name='search'
    ),

    path(
        'class/<str:cls>/',
        views.class_students,
        name='class_students'
    ),

    path(
        'add-student/',
        views.add_student,
        name='add_student'
    ),

    path(
        'edit-student/<int:id>/',
        views.edit_student,
        name='edit_student'
    ),

    path(
        'delete-student/<int:id>/',
        views.delete_student,
        name='delete_student'
    ),
]