from django.shortcuts import render
from django.http import HttpResponseRedirect
from.models import Post
from.forms import PostForm
from django.shortcuts import redirect

def post_list (request):
        return render(request, 'firstapp/post_list.html')
    
def index(request):
    text=Post.objects.all()
    return render(request, 'firstapp/index.html', {"text": text})
    
def new(request):
    if request.method=="POST":
        form=NameForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
            return redirect('index_list')
    else:
        form=PostForm()
    return render(request,'firstapp/new.html',{'form':form})    