from .models import Post
from django import forms

class PostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields= '__all__'
		#('author','title','text','created date','published date')