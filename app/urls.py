from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.Names,name='home' ),
    path('chart/',views.chart,name='chart'),
    path('login/',views.login_view,name='login'),
    path('files_list/',views.file_list,name='files_list'),
    path('files_form/',views.fileform,name='files_form'),
    path('forms/<int:id>/',views.fileform,name='edit_file'),
    path('form/delete/<int:id>/',views.fdelete,name='file_delete'),
    path('logout/',views.user_logout,name='logout'),
    path('S_form/',views.Student_form,name='S_form'),
    path('S_delete/<int:id>',views.Sdelete,name='S_delete'),
    path('S_edit/<int:id>',views.Student_form,name='S_edit'),
    path('S_list/',views.S_list,name='S_list'),
    path('F_form/',views.Faculty_form,name='F_form'),
    path('F_delete/<int:id>',views.Faculty_delete,name='F_delete'),
    path('F_edit/<int:id>',views.Faculty_form,name='F_edit'),
    path('F_list/',views.F_list,name='F_list'), 
    path('register/',views.register,name='register'),
    path('studenthome/',views.studenthome,name='studenthome'), 
    path('FacultyHome/',views.temp,name='temp'),
    path('reports/',views.report,name='report'),
    path('pdf/',views.pdf,name='pdf'),
    path('pdf1/',views.pdf1,name='pdf1'),
    path('pdf2/',views.pdf2,name='pdf2'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)