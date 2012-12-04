from django.views import generic

from {{app_name}}.models import {{model_name}}
#from main.forms import {{model_name}}Form

class {{model_name}}DetailView(generic.DetailView):
    model = {{model_name}}

class {{model_name}}ListView(generic.ListView):
    model = {{model_name}}

class {{model_name}}CreateView(generic.CreateView):
    model = {{model_name}}

class {{model_name}}UpdateView(generic.UpdateView):
    model = {{model_name}}
