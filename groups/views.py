from django.shortcuts import render
from .models import Group
# Create your views here.


def group_list(request):
    group_list = Group.objects.all()
    return render(request, "groups/groups.html", {
        "groups": group_list,
    })
