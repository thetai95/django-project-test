# import from Django
from django.shortcuts import render
from django.views import View
# import from this project
from .models import Department


class ListItem(View):
    def get(self, request):
        departments = Department.objects.all().order_by('-id')
        context = {
            "departments": departments
        }
        return render(request, "polls/index.html", context)
