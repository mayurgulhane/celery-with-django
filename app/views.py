from django.http import HttpResponse
from .tasks import test_func


# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("Hiii")
