from .models import course
from .serializers import CourseSerializer, SearchSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
# Create your views here.

class course_view(APIView):

	def get(self, request, format = None):
		courses = course.objects.all()
		course_serializer = CourseSerializer(courses, many = True)
		return Response(course_serializer.data)

class search(APIView):

	def get(self, request, val, format = None):
		val = list(val.split(" "))
		"""q_search = (Q(subject__icontains = val[0]) |Q(grade__icontains = val[0]) | Q(name__icontains = val[0]))
		if len(val) > 1:
			for i in range(1,len(val)):
				q_search.connector = Q.OR
				q_search = q_search.add((Q(subject__icontains = val[i]) |Q(grade__icontains = val[i]) | Q(name__icontains = val[i])), q_search.connector)"""
		q_search = (Q(name__icontains = val[0]))
		if len(val) > 1:
			for i in range(1,len(val)):
				q_search.connector = Q.AND
				q_search = q_search.add((Q(name__icontains = val[i])), q_search.connector)
		print(q_search)
		s = course.objects.filter(q_search)
		if len(s)>5:
			s = s[:5]
		course_serializer = SearchSerializer(s, many = True)
		return Response(course_serializer.data)	

