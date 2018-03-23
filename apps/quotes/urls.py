from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="dashboard"),

    url(r'^create$', views.create, name="create_quote"),

#REGEX IS LISTENING TO THE URL(THAT THE LINK FROM HTML). => VIEWS.PY => SHOW_USER METHOD
    url(r'^showuser/(?P<userid>[0-9]+)$', views.show_user, name="show"),


 #REGEX IS LISTENING FOR THE URL.THIS WILL BE ROUTING THE ADD FAV FORM. =>VIEWS=>ADD_FAVORITE METHOD.
    url(r'^addfave/(?P<quote_id>[0-9]+)$', views.add_favorite, name="add_favorite"),

     #<a href="/quotes/addfave/{{quote.id}}">Favorite</a


 #REGEX IS LISTENING FOR THE URL.THIS WILL BE ROUTING THE DELETE FAV FORM. =>VIEWS=>ADD_FAVORITE METHOD.
    url(r'^remfave/(?P<quote_id>[0-9]+)$', views.delete_favorite, name="delete_favorite"),
]
