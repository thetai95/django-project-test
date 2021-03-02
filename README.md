Các chức năng có trong Project:
- Connect Django - Postgres
- Django web: các file html, static
- template base không có view return, vậy làm sao để template base nhận đc các biến
(https://stackoverflow.com/questions/43207563/how-can-i-access-environment-variables-directly-in-a-django-template)


- Fix các lỗi, comment liên quan đến HTML/CSS trong (Đánh giá bào test full-stack) -- chưa làm
- API CRUD (làm lại cho chuẩn CRUD api), các chức năng web CRUD -- chưa làm 
- Các config về static trong file settings -- chưa làm -- TODO
- API: paginator, select_related, prefetch_related(project-test-3) - chưa làm
- import / export database -- chưa làm
- Celery -- chưa làm
- Fix các lỗi KHÁC trong (Đánh giá bào test full-stack) -- chưa làm

- ĐỌc mấy cái API CRUD trong project của cty, CRUD mà mình hay làm kiểu ntn -- Tìm hiểu

- Tích hợp thêm cái call Procedure vào đây k nhỉ (search product - boxme)
- Decorator là gì ?

-----------
## Python locally Invoke aws lambda_function ARN
- có 1 lambda_function đã được deploy lên aws type "arn"
- locally: using client.boto3 invoke function đó.
- config account AWS in locally

----------
## send email with Celery
- install redis, celery, django-celery-results, eventlet(with windows)
- add file celery.py in setting folder, add setting for celery, for send mail
(doc celery: https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html)
- run celery: celery -A mysite worker -l info --pool=solo (--pool using with windows)
- runserver

----------
## Model Form CRUD
- create thì validate ntn
- (1) đọc cái CRUD trên web: https://rayed.com/posts/2018/05/django-crud-create-retrieve-update-delete/
- (2) đọc cái góp ý Perob: https://docs.google.com/document/d/1wXinfTfvyRIABfh1i9pzoL7Bx3OrgE1iw8VcJxwX6mM/edit
- (3) tutorial mà a Việt bảo: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website
----------
## null=True, blank=True
- address = models.CharField(max_length=100, blank=True): nếu set như này thì:
- mặc định null=False => field này bắt buộc có giá trị, nếu admin site k nhập gì => insert ''
- ngoài admin site không bắt buộc nhập, nếu k nhập gì thì insert giá trị ''
----------
## django on_delete=models.CASCADE
- on_delete=CASCADE trong OneToOneField và trong ForeignKey
(https://stackoverflow.com/questions/12754024/onetoonefield-and-deleting)

## Fetch API
https://openplanning.net/12395/javascript-fetch-api

## url, path, re_path thì đều để khai báo đường dẫn tới view
+ url khai báo đường dẫn có thể sử dụng đc Regex trong đó để validate cho đường dẫn

+ path() thì dễ dàng sử dụng hơn với url. ví dụ:
path('users/<int:id>') chỉ cần khai báo kiểu dữ liệu và tên biến là được, còn url thì không dùng đc

+ re_path thì có các chức năng nâng cao hơn như có thể dùng Regex để validate cho urlcó thể thay thế cho việc dùng url