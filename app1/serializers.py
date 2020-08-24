from .models import school, course, subscription_plan, subscription_course
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = course
		fields = "__all__"


class SearchSerializer(serializers.ModelSerializer):
	class Meta:
		model = course
		fields = ['name','id']
