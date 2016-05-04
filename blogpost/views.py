from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.
#for arranging the published posts
posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
def post_list(request):
	return render(request,'blogpost/post_list.html',{'posts':posts})
