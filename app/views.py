from django.http import HttpResponse
from .tasks import test_func
from send_mail_app.tasks import send_mail_func


# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("Hiii")



def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Email Sent")

