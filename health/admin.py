from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Status)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Type)
admin.site.register(Disease)
admin.site.register(Feedback)
admin.site.register(Searched_symptom2)
admin.site.register(Searched_Patient)
