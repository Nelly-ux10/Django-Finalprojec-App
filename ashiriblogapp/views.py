from django.shortcuts import render, get_object_or_404,  HttpResponse, redirect
from .models import blogs
from .forms import loginForm, Signup, BlogRegistrationForm, BlogUpdateForm
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

# Create your views here.
def about(request):
		context = {}
		return render(request, 'ashiriblogapp/about.html', context)


def article_list(request):
		article_list = blogs.objects.all().order_by('published')

		paginator = Paginator(article_list, 5)
		page = request.GET.get('page')

		try:
				articles = paginator.page(page)

		except PageNotAnInteger:
				articles = paginator.page(1)
		except EmptyPage:
				articles = paginator.page(paginator.num_pages)

		return render(request, 'ashiriblogapp/articles.html', {'article_list':articles, 'page':page})

def article_detail(request, slug):
		detail = get_object_or_404(blogs, slug=slug)
		return render(request, 'ashiriblogapp/details.html', {'detail':detail})

def user_login(request):
		if request.method == "POST":
				form = loginForm(request.POST)

				if form.is_valid():
						cd = form.cleaned_data
						user = authenticate(request, username = cd['username'], password = cd['password'])


						if user is not None:
								login(request, user)
								return HttpResponse("you are authenticated")

						else:
								return HttpResponse("invalid Login")

		else:
				form = loginForm()

		return render(request,'ashiriblogapp/login.html', {'form':form})

def register(request):
		if request.method == "POST":
				user_form = Signup(request.POST)

				if user_form.is_valid():

						new_user = user_form.save(commit=False)

						new_user.set_password(user_form.cleaned_data['password2'])
						new_user.save()

						return render(request, 'ashiriblogapp/signup_done.html', {'user_form':user_form})

		else:
				user_form = Signup()
		return render(request,'ashiriblogapp/signup.html', {'user_form':user_form})



#@login_required
def add_article(request):
		if request.method == "POST":
			article_form = BlogRegistrationForm(request.POST)

			if article_form.is_valid():
					article = article_form.save(commit=False)
					article.author = request.user
					article.save()

					return redirect('article_list')

		else:
				article_form = BlogRegistrationForm()
		return render(request, 'ashiriblogapp/add_new.html', {'article_form':article_form})


def update_article(request, slug):
		article = get_object_or_404(blogs, slug=slug)

		form = BlogUpdateForm(request.POST or None, instance=article)

		if form.is_valid():
				form.save()
				return redirect('article_list')

		return render(request, 'ashiriblogapp/update.html', {'form':form})



def delete_article(request, slug):
		article = get_object_or_404(blogs, slug=slug)
		article.delete()
		return redirect('article_list')

