
from django.contrib import admin
from django.urls import path , include
from rest_framework.schemas import get_schema_view  # module function to get our api schemas
from rest_framework.documentation import include_docs_urls 


from django.conf import settings
from django.conf.urls import static


urlpatterns = [
    path('admin/', admin.site.urls),

    # Oauth2
    #  path('auth/', include('drf_social_oauth2.urls', namespace='drf')),

    path('' , include('blog.urls' , namespace="blog") ),
    path('api/' , include('blog_api.urls' , namespace="blog_api") ),
    path('api-auth/' , include('rest_framework.urls' , namespace="rest_framework") ),
    path('docs/' , include_docs_urls(title='BlogAPI')),   

# generating a schema endpoints for blogapi app
    path('schema' , get_schema_view(
        title="BlogApi",
        description="API for BlogAPI",
        version = "1.0.0"
    ) , name = 'openapi-schema'),
]



# if settings.DEBUG:
#     urlpatterns +=  static(settings.STATIC_URL , document_root=settings.STATIC_ROOT )
#     urlpatterns +=  static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT )
