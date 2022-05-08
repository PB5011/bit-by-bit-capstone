"""Registers models with the Django administration interface."""

from django.contrib import admin
from .models import *

admin.site.register(CodeSubmission)
admin.site.register(Question)
admin.site.register(Responses)

# admin.site.register(inheritedQuestion)
# admin.site.register(student)
# admin.site.register(inheritedUser)
# admin.site.register(keywords)
# admin.site.register(Notifications)
# admin.site.register(Requests)