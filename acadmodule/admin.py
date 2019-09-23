from django.contrib import admin
from .models import BtechCurriculum,Course,BatchSemester,CurriculumCourse,CurriculumInstructor
# Register your models here.

admin.site.register(BtechCurriculum)
admin.site.register(BatchSemester)
admin.site.register(Course)
admin.site.register(CurriculumCourse)
admin.site.register(CurriculumInstructor)
