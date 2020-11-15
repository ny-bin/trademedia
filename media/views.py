from django.shortcuts import render, get_object_or_404
from loginauth.models import User
from .models import Content
from .forms import PostForm
from django.views.generic import ListView, CreateView
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from datetime import datetime
# from django.views.generic.edit import Forms
from django.urls import reverse
from django.conf.urls.static import static


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@login_required
def profile(request):
    # user = get_object_or_404(User, pk=user_id)
    return HttpResponse(request.user.username)


class ContentsList(ListView):
    template_name = 'media/contents.html'


class PostView(CreateView):
    template_name = 'media/post.html'
    model = Content
    # Content.user_id =
    fields = ("title", "content", "picture")
    success_url = "/media/profile"

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        print(form)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.published_date = datetime.now()
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)
