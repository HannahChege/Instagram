from django.http  import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm,NewImageForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
import datetime as dt
from .models import Image
from django.contrib.auth.decorators import login_required

# # Create your views here.
@login_required(login_url='/accounts/login/')
def instagram(request):
    images = Image.get_all_images()
    # profiles = Profile.objects.all()
    profileimage=  User.objects.all()
    return render(request,'instagram.html',{"images":image})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'registration/registration_form.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')



def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('instagram')

    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form": form})

@login_required(login_url='/accounts/login/')
def upload_image(request):
        profile = Profile.objects.all()
        form = ImageForm()
        for profile in profile:
            if profile.user.id == request.user.id:
                if request.method == 'POST':
                    form = ImageForm(request.POST, request.FILES)
                    if form.is_valid():
                        upload =form.save(commit=False)
                        upload.profile = request.user
                        upload.profile_det = profile
                        upload.save()
                        return redirect('profile', username=request.user)
                else:
                    form = ImageForm()

        return render(request, 'upload.html',{'form':form})    
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-insta/image.html", {"image":image})