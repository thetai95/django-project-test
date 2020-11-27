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
