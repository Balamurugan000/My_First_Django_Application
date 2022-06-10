from django.http import HttpResponse
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from datetime import timedelta
import timedelta
#from django.core.cache.backends.base import DEFAULT_TIMEOUT

import timedelta


@cache_page(20000)
def home(request):

    return render(request,"student.html")


    #msg = "<h1>WELCOME TO DJANGO,hai python</h1>"

    #return HttpResponse(msg)

