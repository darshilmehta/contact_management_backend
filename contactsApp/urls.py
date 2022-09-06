from django.urls import path
from .views import ContactsList, ContactsDetail

urlpatterns = [
    path('create/', ContactsList.as_view(), name='create-registeration'), # POST
    path('all/', ContactsList.as_view(), name='all-registerations-list'), # GET
    path('update/<int:pk>/', ContactsDetail.as_view(), name='update-registeration'), # PUT
    path('delete/<int:pk>/', ContactsDetail.as_view(), name='delete-registeration'), # DELETE
    path('get/<int:pk>/', ContactsDetail.as_view(), name='get-registeration'), # GET (single object)
]