from django.shortcuts import render
from appOne.models import Users
# Create your views here.

def index(request):
    return render(request, 'appOne/index.html')


def users(request):

    user_list = Users.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'appOne/users.html', context = user_dict)

def stuff(request):
    return render(request, 'appOne/stuff.html')
