from django.conf.urls import url,include
from django.contrib import admin
from acadmodule import views

urlpatterns = [
    url(r'^add_course/', views.add_course,name="add_courses"),
    url(r'^add_btech_curriculum/', views.add_btech_curriculum,name="add_btech_curriculums"),
    url(r'^add_batch_semester/', views.add_batch_semester,name="add_batch_semester"),
    url(r'^add_curriculum_course/', views.add_curriculum_course,name="add_curriculum_courses"),
    url(r'^view_curriculum/', views.view_curriculum,name="view_curriculums"),
    url(r'^test/',views.testajax,name="test"),
    url(r'^select/',views.selectProgramme,name="select"),
    url(r'^selectsem/',views.select_semester,name="selectsem"),
    url(r'^Academics/',views.programme,name="pro"),
]
