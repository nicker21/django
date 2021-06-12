from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from students.models import Student
from students.utils import format_records

from webargs import fields
from webargs.djangoparser import use_args


def hello(request):
    return HttpResponse('Hello')


@use_args({
    "first_name": fields.Str(
        required=False
    ),
    "last_name": fields.Str(
        required=False
    ),
    "birthdate": fields.Date(
        required=False
    )},
    location="query"
)

def get_students(request):
    students = Student.objects.all()
    records = format_records(students)


    return HttpResponse(records)