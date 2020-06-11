from django.shortcuts import render,redirect
from .forms import MessageForm
from .models import Post


# Create your views here.

def index(request):

    posts=Post.objects.all().order_by('-id')

    form=MessageForm()


    if request.method == 'POST':
        form=MessageForm(request.POST)


        if form.is_valid():
            form.save()

            return redirect('/')


    context={
        'title':"Home Page",
        'form':form,
        'posts':posts
    }

    return render(request,'blog/index.html',context)

