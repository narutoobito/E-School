from django.contrib import admin
from .models import school, course, subscription_plan, subscription_course
# Register your models here.


admin.site.register(school)
admin.site.register(course)
admin.site.register(subscription_plan)
admin.site.register(subscription_course)

