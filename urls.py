from django.conf.urls.defaults import patterns, url, include

from {{app_name}} import views

urlpatterns = patterns("",

    url(
        regex=r"^create/$",
        view=views.{{model_name}}CreateView.as_view(),
        name="{{model_name|lower}}_create",
    ),
    url(
        regex=r"^update/(?P<pk>\d+)/$",
        view=views.{{model_name}}UpdateView.as_view(),
        name="{{model_name|lower}}_update",
    ),
    url(
        regex=r"^(?P<pk>\d+)/$",
        view=views.{{model_name}}DetailView.as_view(),
        name="{{model_name|lower}}_detail",
    ),
    url(
        regex=r"^$",
        view=views.{{model_name}}ListView.as_view(),
        name="{{model_name|lower}}_list",
    ),
)
