from django.urls import path
from .views import *
urlpatterns=[
    path('', PostListView.as_view(), name='home'),
    path('search/', search.as_view(), name='search'),
    path('create/new/',PostCreateView.as_view(),name='add_news'),
    #path('<int:pk>/edit/', ArticalEditView.as_view(), name='artical_edit'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_datail'),
    path('<int:pk>/categories/', CategoryListView.as_view(), name='category_list'),
    path('like/<int:pk>/', like, name='like_post'),
    #path('<int:pk>/delete/', ArticalDeleteView.as_view(), name='artical_detele'),

]