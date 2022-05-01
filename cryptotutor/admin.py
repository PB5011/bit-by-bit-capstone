from django.contrib import admin
from .models import *

#BbB defined models
admin.site.register(CodeSubmission)
admin.site.register(Question)

#Client defined models
# admin.site.register(inheritedQuestion)
# admin.site.register(student)
# admin.site.register(inheritedUser)
# admin.site.register(keywords)
admin.site.register(Responses)
# admin.site.register(Notifications)
admin.site.register(Requests)