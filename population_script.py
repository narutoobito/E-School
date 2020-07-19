import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','eschool_backend.settings')

import django
django.setup()

from app1.models import course

if __name__ == "__main__":
	grades = [4,5,6,7,8,9,10]
	subjects = ['Maths','Computer','Chemistry','Physics']
	for i in range(len(grades)):
		for j in range(len(subjects)):
			name = "Understanding " + subjects[j] + " for class " + str(grades[i])
			price = 450
			teacher = "YIF"
			duration = "20h"
			subject = j + 1
			grade = i + 1
			course.objects.create(name = name,
									price = price,
									teacher = teacher,
									duration = duration,
									subject = subject,
									grade = grade)	
	