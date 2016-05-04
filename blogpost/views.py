from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.
#for arranging the published posts
posts = Post.objects.all()
def post_list(request):
	return render(request,'blogpost/post_list.html',{'posts':posts})
