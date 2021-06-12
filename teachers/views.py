from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from students.utils import format_records

from teachers.models import Teacher

from webargs import fields
from webargs.djangoparser import use_args


# Create your views here.

@use_args({
    "first_name": fields.Str(
        required=False
    ),
    "last_name": fields.Str(
        required=False
    )},
    location="query"
)
def get_teachers(request, args):
    teachers = Teacher.objects.all()

    for param_name, param_value in args.items():
        teachers = teachers.filter(**{param_name: param_value})

    records = format_records(teachers)

    return HttpResponse(records)