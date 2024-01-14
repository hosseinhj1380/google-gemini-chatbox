from django.contrib import admin
from django.urls import path ,include
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('rest/chat',views.RestApiChat.as_view()),
    path('stream/chat',views.StreamChat.as_view()),
    # path('',views.home,name="home")


]
