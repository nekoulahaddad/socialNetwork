from django import forms
from .models import Post,PostImage,Comment


# choices = Cat.objects.all().values_list('russian','russian')
# choice_list = []

# for item in choices:
# 	choice_list.append(item)

# print(choice_list)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		# fields = ['title','category','author','description']
		fields = ['title','description','category']

		# widgets = {
		# 'title':forms.TextInput(attrs={'class':'form-control','placeholder':'type a title'}),
		# 'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
		# 'author':forms.TextInput(attrs={'class':'form-control','id':'author','value':'','type':'hidden'}),
		# 'description':forms.Textarea(attrs={'class':'form-control'})
		# }

class PostFullForm(PostForm): #extending form
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta(PostForm.Meta):
        fields = PostForm.Meta.fields + ['images',]


class CommentForm(forms.ModelForm):
	comment = forms.CharField(label="",widget=forms.Textarea(attrs={
		'id':'commenttext',
		'class': 'textarea commenttext',
		'rows': '4',
	}))
	class Meta:
		model = Comment
		fields = ('comment',)
