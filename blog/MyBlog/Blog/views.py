from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog(request):
	texts = Blog.objects.all()
	return render(request, 'Blog/blogs.html', {'texts': texts})
# Create your views here.

def detail(request, blog_id):
	blog = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'Blog/detail.html', {'blog':blog})