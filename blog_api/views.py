from django.shortcuts import render
from blog.models import  Post
from rest_framework import generics , filters , status 
from rest_framework.response import Response
from rest_framework.permissions import BasePermission , SAFE_METHODS, IsAdminUser , DjangoModelPermissions , IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import PostSerializer


class PostUserWritePermission(BasePermission):
    message = " Editing posts is restricted to the author only "

    def has_object_permission(self , request , view , obj): # obj  ust equal to the user
        
        if request.method == SAFE_METHODS:  #if the method is either 'GET' 'POST' , 'HEAD'
            return True

        return obj.author == request.user


class PostList(generics.ListCreateAPIView):
    # permission_classes = [ IsAuthenticated  ]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        # return Post.objects.all()
        return Post.objects.filter(author = user)
    

# RetrieveAPIView is use to get a single instance using the kwargs parameters either as integer or string from the url
# ListAPIView return all the post where slug value == to the kwargs parameter
# class PostDetail(generics.ListAPIView ):
#     # queryset = Post.postobjects.all()
#     serializer_class = PostSerializer
#     def get_queryset(self):
#         slug = self.kwargs['pk']
#         print(slug)
        
#         return Post.objects.filter(slug=slug)




# returning every post for any user(allow any)
# class PostList1(generics.ListAPIView):
#     permission_classes = [AllowAny]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()



# returning every post for only Authenticated users(IsAuthenticated)
# class PostList2(generics.ListAPIView):
#     permission_classes = [ IsAuthenticated ]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()



# RetrieveAPIView is use to get a single instance using the kwargs parameters either as integer or string from the url
# class PostDetail (generics.RetrieveAPIView): 
#     # permission_classes = [ PostUserWritePermission ]
#     serializer_class = PostSerializer

#     def get_queryset(self):
#         slug = self.kwargs['pk']
#         print(slug)
#         return Post.objects.filter(id = slug)



#RetrieveAPIView is use to get a single instance using the querystring params
# class PostDetail (generics.RetrieveAPIView): 

#     serializer_class = PostSerializer
    
#     def get_queryset(self):
#         slug = self.request.query_params.get('slug' , None)
#         return Post.objects.filter(slug=slug)




#ListAPIView is use to get all instance using the querystring params and it only works with ListAPIView
class PostDetail (generics.ListAPIView): 
    serializer_class = PostSerializer
    def get_queryset(self):
        slug = self.request.query_params.get('slug' , None) #here, it will get the value of each query string at the url from query string parameters
        print(slug)
        return Post.objects.filter(slug=slug)





#RetrieveAPIView is use to get a single instance using the querystring params if user as the author only
class PostSearch (generics.ListAPIView): 
    # permission_class = [ PostUserWritePermission ]
    serializer_class = PostSerializer
    def get_queryset(self):
        slug = self.request.query_params.get('slug' , None)
        return Post.objects.filter(slug=slug)



# making advance search here ; like this strictly exactly =>  ?search=...
#   '^': 'istartswith',
#         '=': 'iexact',
#         '@': 'search',
#         '$': 'iregex',
class PostListDetailFilter(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [filters.SearchFilter]  #utilizing the search filter
    search_fields = ['^slug']    # specifying the database fields to make the search





# Poost Admin

# creating a post
# class CreatePost(generics.CreateAPIView):
#     persmission_classes = [IsAuthenticated]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class CreatePost(APIView):
    # permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser , FormParser,)  #parser classes that will all Files to be parsed and get upload through forms

    
    def post(self , request , format=None):
        print(request.data)
        print(format)
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid(): #serializer level validation
            serializer.save()
            return Response(serializer.data , status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)






# viewing the post detail
class AdminDetailPost(generics.RetrieveAPIView):
    persmission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer



# editing a post
class EditPost(generics.UpdateAPIView):
    persmission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class DeletePost(generics.DestroyAPIView):
    persmission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer




