from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from .models import Post,Category,Like,Comment,PostImage
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PostForm,PostFullForm,CommentForm
from django.db.models import F
from notifications.signals import notify


class HomeView(ListView):
	model = Post
	template_name = "home.html"
	ordering = ['-post_date']
	def get_context_data(self,*args,**kwargs):
		cat_menu = Category.objects.all()
		context = super(HomeView,self).get_context_data(*args,**kwargs)
		context["cat_menu"] = cat_menu
		return context

class designView(DetailView):
	model = Post
	template_name = "design_detail.html"
	form = CommentForm
	def get_context_data(self,*args,**kwargs):
		comments = Comment.objects.filter(post=self.kwargs['pk'])
		post_images = PostImage.objects.filter(post=self.kwargs['pk'])
		post, _ = Post.objects.get_or_create(id=self.kwargs['pk'])
		post.views = F("views") + 1
		post.save(update_fields=["views"])
		recomended_posts = Post.objects.filter(category=post.category)[:4]
		context = super(designView,self).get_context_data(*args,**kwargs)
		context["post_images"] = post_images
		context["form"] = self.form
		context["comments"] = comments
		context["recomended_posts"] = recomended_posts
		return context
	def post(self, request, *args, **kwargs):
		form = CommentForm(request.POST)
		if form.is_valid():
			post = self.get_object()
			form.instance.user = request.user
			form.instance.post = post
			form.save()
			recipient = post.author
			if request.user.id != recipient.id:
				notify.send(request.user, recipient=recipient, verb='прокомментировал вашу',target=post,description="публикацию",level="info")
			return redirect(reverse("design-detail", kwargs={
				'pk': post.pk
			}))


class AddPostView(ListView):
	model = Category
	template_name = "add_post.html"



class UpdatePostView(UpdateView):
	model = Post
	template_name = 'update_post.html'
	form_class = PostForm


class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')


def CategoryView(request,cats):
	cat_menu = Category.objects.all()
	cat = cats.replace('-',' ')
	category_posts = Post.objects.filter(category=cats.replace('-',' '))
	return render(request,'categories.html',{'cats':cat,'category_posts':category_posts,'cat_menu':cat_menu})



def like_unlike_post(request):
    user = request.user
    print(user)
    if  request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        # profile = Profile.objects.get(user=user)
        recipient = post_obj.author
        profile = request.user
        print(recipient)

        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)

        like, created = Like.objects.get_or_create(user=profile, post_id=post_id)

        if not created:
            if like.value=='Like':
                like.value='Unlike'
                like.save()
            else:
                like.value='Like'
                like.save()
        else:
            like.value='Like'

            post_obj.save()
            like.save()
            if user.id != recipient.id:
                notify.send(user, recipient=recipient, verb='поставил лайк на твою',target=post_obj,description="публикацию",level="success")
            
    return redirect('home')





def addNoteView(request):
	if request.method == "POST":
		form = PostFullForm(request.POST or None, request.FILES or None)
		print(request.POST)
		files = request.FILES.getlist('images')
		print(files)
		print(files[0])
		if form.is_valid():
			user = request.user
			title = form.cleaned_data['title']
			description = form.cleaned_data['description']
			category = form.cleaned_data['category']
			note_obj = Post.objects.create(author=user,title=title,description=description,category=category,post_main_pic=files[0]) #create will create as well as save too in db.
			for f in files:
				PostImage.objects.create(post=note_obj,mainimage=f)
		else:
			print("Form invalid")
	else:
		form = PostFullForm()
	return HttpResponseRedirect(reverse('home'))





def mark_all_as_read(request):
	if request.is_ajax and request.method == "GET":
		request.user.notifications.mark_all_as_read()
	return redirect('home')

# def mark_friend_request_as_read(request):
# 	if request.is_ajax and request.method == "GET":
# 		request.user.reciever.update(read=True)
# 	return redirect('home')

