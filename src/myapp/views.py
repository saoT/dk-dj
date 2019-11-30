from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Post

class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'

# INITIAL EXMPLE
#from .tasks import show_hello_world
#from .models import DemoModel

# class ShowHelloWorld(TemplateView):
#     template_name = 'hello_world.html'

#     def get(self, *args, **kwargs):
#         show_hello_world.apply()
#         return super().get(*args, **kwargs)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['demo_content'] = DemoModel.objects.all()
#         return context