from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt
from .models import Image,Profile
from django.contrib.auth.decorators import login_required

# # Create your views here.
@login_required(login_url='/accounts/login/')
def instagram(request):
    images = Image.object.all()
    return render(request,'instagram.html',{"images":image})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-insta/image.html", {"image":image})