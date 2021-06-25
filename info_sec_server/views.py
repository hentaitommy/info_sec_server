from django.shortcuts import render
from django.http import HttpResponse
from oauth2_provider.views.generic import ProtectedResourceView
# Create your views here.

def index(request):
    return render(request, 'index/index.html')

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        print(request.user)
        return HttpResponse('Hello, OAuth2!')