from django.shortcuts import render

# Create your views here.
from groups.models import Group

from students.utils import format_records
from django.http import HttpResponse


def get_groups(request):
    groups = Group.objects.all()
    records = format_records(groups)
    return HttpResponse(records)