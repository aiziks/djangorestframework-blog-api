from django.urls import path
from .views import (PostList , PostDetail , PostSearch, PostListDetailFilter,
        CreatePost, AdminDetailPost , EditPost , DeletePost 

)



app_name = "blog_api"

urlpatterns = [
    path('' ,  PostList.as_view() , name="listcreate"),
    # path('post/<int:pk>/' ,  PostDetail.as_view() , name="detailcreate"),
    path('post/' ,  PostDetail.as_view() , name="detailcreate"),
    path('search/' ,  PostSearch.as_view() , name="postsearch"),

    path('search/custom/' ,  PostListDetailFilter.as_view() , name="postsearchcustom"),
    
    # Admin Post
    
    path('post/create/' ,  CreatePost.as_view() , name="postcreate"),
    path('post/detail/<int:pk>' ,  AdminDetailPost.as_view() , name="postedit"),
    path('post/edit/<int:pk>' ,  EditPost.as_view() , name="postedit"),
    path('post/delete/<int:pk>' ,  DeletePost.as_view() , name="postedit"),

]