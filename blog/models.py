from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date



class Post(models.Model):
	title = models.CharField(max_length=250)
	pending = models.BooleanField(default=True)
	category = models.CharField(max_length=250,default='design')
	russian_category = models.CharField(max_length=255,default='design')
	author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	description = models.TextField(blank=True)
	post_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	views = models.IntegerField(default=0)
	liked = models.ManyToManyField(User, blank=True, related_name='likes')
	post_main_pic = models.ImageField(upload_to='img/main/', null = True)
	def __str__(self):
		return self.title + ' | ' + str(self.author) + ' | ' + str(self.pending) #i put string cuz author is not a string

	def num_likes(self):
		return self.liked.all().count()
	

	def get_absolute_url(self):
		# return reverse('design-detail',args=(str(self.id)))
		return reverse('home')

class PostImage(models.Model):
	post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
	title = models.CharField(max_length=250)
	views = models.CharField(max_length=250,default=0)
	mainimage = models.ImageField(upload_to='img/', null = True)
	def __str__(self):
		return self.title + ' | ' + self.views #i put string cuz author is not a string



LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    
    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"
	

class Category(models.Model):
	name = models.CharField(max_length=250)
	russian_name = models.CharField(max_length=250)
	category_pic = models.ImageField(upload_to='img/category/', null = True)
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		# return reverse('design-detail',args=(str(self.id)))
		return reverse('home')	


class Comment(models.Model):
	post = models.ForeignKey(Post,related_name='comments' ,on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment_user')
	comment = models.TextField(default='')
	add_time = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.post.title + ' | ' + str(self.user)