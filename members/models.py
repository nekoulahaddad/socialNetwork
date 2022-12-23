from django.db import models
from django.contrib.auth.models import User
from blog.models import Post
from django.urls import reverse

class Profile(models.Model):
	user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
	firstname = models.CharField(max_length=250,blank=True,default="")
	lastname = models.CharField(max_length=250,blank=True,default="")
	mobile = models.CharField(max_length=250,blank=True,default="")
	website = models.CharField(max_length=250,blank=True,default="")
	bio = models.TextField(null=True,blank=True,default="")
	profile_pic = models.ImageField(upload_to='img/user/', null = True, default='img/user/default.jpg')
	views = models.CharField(max_length=250,default=0)
	user_type = models.CharField(max_length=250,default='designer')
	city = models.CharField(max_length=250,default="Россия")
	friend_request = models.ManyToManyField(User, blank=True, related_name='friend_request')
	# @property
	# def avatar_image_url(self):
	# 	if self.profile_pic:
	# 		return self.profile_pic.url
	# 	else:
	# 		return "https://upload.wikimedia.org/wikipedia/commons/a/a0/Arh-avatar.jpg"
	def get_absolute_url(self):
		return reverse('edit_profile',args=[self.user.id])

	def __str__(self):
		return str(self.user)



class Friend(models.Model):
	sender = models.ForeignKey(User,related_name='sender', on_delete=models.CASCADE)
	reciever = models.ForeignKey(User,related_name='reciever', on_delete=models.CASCADE)
	read = models.BooleanField(default=False)
	approved = models.BooleanField(default=False)
	requested = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	
	def __str__(self):
		return str(self.sender) + ' | ' + str(self.reciever)


class Work(models.Model):
	designer = models.ForeignKey(User, on_delete=models.CASCADE)
	work_date = models.CharField(max_length=250,blank=True,default="")
	work_place = models.CharField(max_length=250,blank=True,default="")
	def __str__(self):
		return str(self.designer) + ' | ' + self.work_place


class Education(models.Model):
	designer = models.ForeignKey(User, on_delete=models.CASCADE)
	education_date = models.CharField(max_length=250,blank=True,default="")
	education_place = models.CharField(max_length=250,blank=True,default="")
	def __str__(self):
		return str(self.designer) + ' | ' + self.education_place