from django.shortcuts import render
from main.serializers import PersonSerializer
from rest_framework import generics
from main.models import Person


class APIPersonList(generics.ListCreateAPIView):
	queryset = Person.objects.all()
	serializer_class = PersonSerializer

	def get_success_headers(self, data):
		print(data)
		try:
			return {'Location': f"/api/v1/persons/{data['id']}"}
		except (TypeError, KeyError):
			return {}


class APIPersonDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Person.objects.all()
	serializer_class = PersonSerializer
