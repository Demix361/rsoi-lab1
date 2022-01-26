from django.urls import path
from .views import APIPersonList, APIPersonDetail


urlpatterns = [
	path('api/v1/persons', APIPersonList.as_view(), name='person-list'),
	path('api/v1/persons/<int:pk>', APIPersonDetail.as_view(), name='person-detail')
]
