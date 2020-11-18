# using context_processors to pass environment variables for Django template
from django.conf import settings


def export_vars(request):
    data = {
        'MY_NAME': settings.MY_NAME
    }
    return data
