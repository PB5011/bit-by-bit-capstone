from django.contrib import admin
from .models import inheritedQuestion, student, inheritedUser, answers, keywords, responses, Notifications, Requests

# Register your models here.
admin.site.register(inheritedQuestion)
admin.site.register(student)
admin.site.register(inheritedUser)
admin.site.register(answers)
admin.site.register(keywords)
admin.site.register(responses)
admin.site.register(Notifications)
admin.site.register(Requests)