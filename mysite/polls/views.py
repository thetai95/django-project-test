# import from Django
from django.shortcuts import render
from django.views import View
# import from this project
from .models import Department, City


class ListItem(View):
    def get(self, request):
        departments = Department.objects.all().order_by('-id')
        context = {
            "departments": departments
        }
        return render(request, "polls/index.html", context)


class InvokeLambdaFunction(View):
    def get(self, request):
        # import lib
        import boto3
        import json

        # init client
        client = boto3.client('lambda')

        # function_name deploy AWS
        function_name = "arn:aws:lambda:ap-northeast-1:295277646086:function:thetai-test-aws-HelloWorldFunction-G55U9J4QWGQY"

        # NOTE: config account AWS in locally

        # event: any value
        payload = {
            "key": 12345
        }

        # client invoke to lambda_function
        response = client.invoke(
            FunctionName=function_name,
            InvocationType='RequestResponse',
            LogType='Tail',
            Payload=json.dumps(payload),
            # Qualifier=$LATEST
        )

        print("response = ", response)
        print("status_code = ", response['StatusCode'])
        print("data_payload = ", json.loads(response['Payload'].read()))

        return render(request, "polls/invoke_lambda_function.html")


from .tasks import go_to_sleep, send_email_with_celery
from datetime import datetime
from django.conf import settings


class TestCelery(View):
    def get(self, request):
        go_to_sleep.delay(5)
        return render(request, "polls/test_celery.html")


def send_email(request):
    dict_info = {
        "subject": "Test Celery in time {}.".format(datetime.now()),
        "message": "Celery Send Email Success! {}".format(datetime.now()),
        "from_email": settings.EMAIL_HOST_USER,
        "recipient_list": [
            'thetai.hvktqs@gmail.com',
            'tai.tran@fujitechjsc.com',
        ]
    }
    send_email_with_celery.delay(**dict_info)

    return render(request, 'polls/send_email.html')


def create_city(request):
    data_city = {
        "name": "ND",
        "created": "2020-11-05 10:57:33",
    }
    City.objects.create(**data_city)

    return render(request, 'polls/create_city.html')
