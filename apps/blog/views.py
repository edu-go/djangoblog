from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Homepage
def home(request):
    return render(request, 'home.html', {})

# Create your views here.
def posts(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'posts.html', {'posts' : posts})

    ## COMO SE TRADUCE LO DE ARRIBA EN SQL?
    ## SELECT * FROM Post WHERE publish_date <= DATETIME.NOW() ORDER BY publish_date