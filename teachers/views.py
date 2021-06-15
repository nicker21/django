from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect

from students.utils import format_records

from teachers.models import Teacher

from webargs import fields
from webargs.djangoparser import use_args
from teachers.forms import TeacherCreateForm


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

@csrf_exempt
def create_teacher(request):
    if request.method == 'GET':

        form = TeacherCreateForm()

    elif request.method == 'POST':

        form = TeacherCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')

    html_form = f"""
    <form method="post">
      {form.as_p()}
      <input type="submit" value="Submit">
    </form>
    """

    response = html_form

    return HttpResponse(response)