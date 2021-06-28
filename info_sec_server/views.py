from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from oauth2_provider.views.generic import ProtectedResourceView
# Create your views here.

def index(request):
    return render(request, 'index/index.html')

@login_required()
def secret_page(request, *args, **kwargs):
    return HttpResponse('正在使用身份：' + str(request.user) + '访问此API')