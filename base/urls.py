from django.contrib import admin
from django.urls import path, include
from api.models import CourseResource, CategoryResource
from tastypie.api import Api

api = Api(api_name='v1')
course_resource = CourseResource()
category_resource = CategoryResource()
api.register(course_resource)
api.register(category_resource)

# api/courses/1
# api/categories

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('api/', include(api.urls))
]
