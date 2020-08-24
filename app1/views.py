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
			for i in range(1, len(val)):
				q_search.connector = Q.AND
				q_search = q_search.add((Q(name__icontains = val[i])), q_search.connector)
		print(q_search)
		s = course.objects.filter(q_search)
		if len(s)>5:
			s = s[:5]
		course_serializer = SearchSerializer(s, many = True)
		return Response(course_serializer.data)	

class Filter(APIView):

	def post(self, request, format=None):
		print(request.data)
		container = {}
		special_filter = {"science": Q(name__icontains="physics") | Q(name__icontains="chemistry"), "primary": Q(grade__lte="5"), "secondary": Q(grade__gte="6")
		}
		main_search = Q()
		data_fields = course.getFields(self)

		filter_type={
			"name": "icontains",
			"price": "lte",
			"duration": "lte",
			"teacher": "icontains",
			"subject": "icontains",
			"grade": "icontains"
		}

		try:
			request.data['special']
		except KeyError:
			request.data['special'] = None

		if request.data['special']:
			main_search = special_filter[request.data["special"]]

		else:
			for field in data_fields:
				try:
					container[field] = request.data[field]
					if type(container[field]) == int:
						val = [container[field]]
					elif type(container[field])==str:
						val = list(container[field].split(" "))
				except KeyError:
					container[field] = None
					val = None

				field_filter = field + '__' + filter_type[field]


				if val:
					q_search = Q()
					for elements in val:

						q_search.add(Q(**{field_filter: elements}), Q.OR)
						#print(q_search)
						#q_search.add(Q(grade="2"), Q.AND)
				else:
					q_search = None
				if q_search:
					main_search.add(q_search, Q.AND)


		#print(main_search)

		courses = course.objects.filter(main_search)
		course_serializer = CourseSerializer(courses, many = True)

		#print(main_search)

		return Response(course_serializer.data)

