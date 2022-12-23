from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404,redirect
from blog.models import Post,Category,Like,PostImage
from .models import Profile,Friend,Work,Education
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import F
from django.db.models import Count
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from notifications.signals import notify
from django.views.generic import UpdateView
from .forms import WorkForm,WorkandEducationForm
from django.contrib.auth.views import PasswordChangeView

class UserRegisterView(generic.CreateView):
	form_class = UserCreationForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')



def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        newProfile = Profile.objects.create(user=user)
        login(request, user)
        return redirect('home')
    return render(request, 'registration/register.html', {'form': form})


def ProfileView(request,username):
	user = User.objects.get(username=username)
	user_posts = Post.objects.filter(author=user)
	return render(request,'registration/profile.html',{'user_posts':user_posts,'designer':user})

def AllDesignersView(request):
	user_posts = User.objects.annotate(total_posts = Count('post'),total_likes = Count('post__liked'))
	user_by_post = user_posts.order_by('-total_posts')
	user_by_like = user_posts.order_by('-total_likes')
	number_of_designers = len(user_posts)
	print(user_posts)
	context = {
	'user_posts':user_posts,
	'user_by_post':user_by_post,
	'user_by_like':user_by_like,
	'number_of_designers':number_of_designers,
	}
	return render(request,'designers_page.html',context)

def AboutDesignerView(request,username):
	user = User.objects.get(username=username)
	user_posts = Post.objects.filter(author=user)
	number_of_posts = len(user_posts)
	return render(request,'about_designer.html',{'user_posts':user_posts,'designer':user,'number_of_posts':number_of_posts})

def add_friend(request):

	if request.is_ajax and request.method == 'POST':
		print("this is post request")
		reciever_id = request.POST.get('reciever_id')
		reciever_obj = User.objects.get(id=reciever_id)
		sender = request.user

		if sender in reciever_obj.profile.friend_request.all():
			reciever_obj.profile.friend_request.remove(sender)
		else:
			reciever_obj.profile.friend_request.add(sender)

		friend, created = Friend.objects.get_or_create(sender=sender, reciever=reciever_obj)

		if not created:
			friend.requested = not friend.requested
			friend.save()
		else:
			friend.requested = True
			friend.save()

			reciever_obj.save()
			notify.send(sender, recipient=reciever_obj, verb='подписался на вас',level="warning")
	return redirect('home')


class UpdateProfile(UpdateView):
	model = Profile
	template_name = 'edit_user.html'
	fields = ['city','firstname','lastname','website','mobile','bio','profile_pic']


# class UpdateWork(UpdateView):
# 	model = Work
# 	template_name = 'edit_work.html'
# 	form_class = WorkForm


def addWork(request):
	if request.method == "POST":
		form = WorkandEducationForm(request.POST or None)
		print(request.POST)
		if form.is_valid():
			print("Form valid")
			user = request.user
			work_date = form.cleaned_data['work_date']
			work_place = form.cleaned_data['work_place']
			education_place = form.cleaned_data['education_place']
			work_obj = Work.objects.create(designer=user,work_date=work_date,work_place=work_place)
			education_obj = Education.objects.create(designer=user,education_place=education_place)
		else:
			print("Form invalid")
	else:
		form = WorkandEducationForm()
	return HttpResponseRedirect(reverse('home'))



def addWorkView(request):
	return render(request,'edit_work.html')

def changePrivacy(request):
	return render(request,'privacy.html')


class PasswordsChangeView(PasswordChangeView):
	form_class = PasswordChangeForm
	success_url = reverse_lazy('password_success')


def passwordSuccess(request):
	return render(request,'password_success.html')
