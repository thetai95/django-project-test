DOC:
(1) đọc lại các bài viết từ đầu, tiếng việt trk (2 bài), 
https://viblo.asia/p/gioi-thieu-celery-maGK7mvBlj2
https://viblo.asia/p/tim-hieu-ve-celery-1VgZv4dr5Aw


(2) sau đó đọc document của Celery (2 bài: 1 bài của Python, 1 bài của Django)
https://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html
https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html


(3) sau đó xem youtube để làm lại, hình như 3 video gì đó
https://www.youtube.com/watch?v=THxCy-6EnQM
https://www.youtube.com/watch?v=BbPswIqn2VI
https://www.youtube.com/watch?v=b-6mEAr1m-A

----------
project using celery demo:
1 - install redis on windows, test redis=redis-cli, run redis=redis-server

2 - run celery: celery -A tasks worker -l info -P eventlet (làm đúng như command, run cả "-P eventlet")

3 - define some task (ex: task add, ...)

4 - call task celery with terminal
>> from tasks import add
>> result = add.delay(2, 3)     # call my task 
>> result.status    # get status of task
>> result.get()     # get result when status = Success, else status=pending


----------
-----------

cái cuối cùng là làm đc 1 demo về Celery, như các ví dụ của nó vậy

----
chú ý xem Redis các thứ hoạt động ntn...
các trạng thái nó cập nhật trong DB ntn, log ra ntn...

--------------------
Để call một task, bạn có thể sử dụng method delay(): add.delay(4, 4)
--------------------
Celery quản lý trạng thái của tasks và có thể lưu chúng trong các hệ thống gọi là result backend. Vòng đời mặc định của task trong Celery gồm:

PENDING: task đợi được thực thi.

STARTED: task đã khởi chạy

SUCCESS: task đã chạy thành công

FAILURE: task gặp lỗi sau khi khởi chạy

RETRY: task đang được chạy lại

REVOKED: task được thu hồi lại
--------------------
Gọi task: Celery cung cấp các API để gọi task sau khi đã định nghĩa chúng ở trên.
3 method chính:
apply_async: gửi task message.
delay: gửi task message
calling: task message sẽ không được gửi đi tới worker mà task sẽ được thực thi luôn bởi process hiện tại.