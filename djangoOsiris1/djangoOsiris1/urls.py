from django.contrib import admin
from django.urls import path
from crudapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', views.IndexView.as_view(), name='index'),
    path('contacts/<int:pk>/', views.ContactDetailView.as_view(), name='detail'),

    path('contacts/edit/<int:pk>/', views.edit, name='edit'),
    path('contacts/create/', views.create, name='create'),
    path('contacts/delete/<int:pk>/', views.delete, name='delete'),
]


# CREATE, READ, UPDATE,        DELETE
# POST,    GET, (PUT, PATCH),  DELETE 
# 
# GET -> /contacts/1/                   -> [DetailView]
# GET -> /contacts/                     -> [ListView]
# POST -> /contacts/                    -> [CreateView]
# (PUT, PATCH) -> /contacts/1/          -> [UpdateView]
# DELETE -> /contacts/1/                -> [DeleteView]
#                                               +
#                                        [GenericApiView]
