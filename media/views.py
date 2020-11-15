from django.shortcuts import render, get_object_or_404
from loginauth.models import User
from .models import Content
# from .forms import PostForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
# from django.views.generic.edit import Forms
from django.urls import reverse
from django.conf.urls.static import static


@login_required
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def profile(request):
    # user = get_object_or_404(User, pk=user_id)
    return HttpResponse(request.user.username)

class ContentsListByUser(ListView):
    template_name = 'media/usercontents.html'
    model = Content
    paginate_by = 10  # if pagination is desired

    def get_queryset(self):
        return Content.objects.filter(author_id = self.request.user)

 

class ContentDetail(DetailView):
    template_name = 'media/detail.html'
    model = Content

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'username': User.objects.get(id = self.request.user.id).username
        })
        # context["username"] = "username"
        return context 

class PostView(CreateView):
    template_name = 'media/post.html'
    model = Content
    fields = ("title", "content", "picture")
    success_url = "/media/profile"

    def form_valid(self, form):
        form.instance.published_date = datetime.now()
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)
