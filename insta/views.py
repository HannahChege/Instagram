# from django.shortcuts import render
# from django.http  import HttpResponse
import datetime as dt
from .models import Image
from django.contrib.auth.decorators import login_required

# # Create your views here.
@login_required(login_url='/accounts/login/')
def instagram(request):
    image = Image.display_images
    return render(request,'instagram.html',{"image":image})

# def image(request,image_id):
#     try:
#         image = Image.objects.get(id = image_id)
#     except DoesNotExist:
#         raise Http404()
#     return render(request,"all-insta/image.html", {"image":image})