from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from health.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home,name="home"),
    path('patient_home', User_Home,name="patient_home"),
    path('doctor_home', Doctor_Home,name="doctor_home"),
    path('admin_home', Admin_Home,name="admin_home"),
    path('about', About,name="about"),
    path('contact', Contact,name="contact"),
    path('help', Help,name="help"),
    path('gallery', Gallery,name="gallery"),
    path('login', Login_User,name="login"),
    path('login_admin', Login_admin,name="login_admin"),
    path('signup', Signup_User,name="signup"),
    path('logout', Logout,name="logout"),
    path('add_doctor', Add_Doctor,name="add_doctor"),
    path('add_disease', Add_Disease,name="add_disease"),
    path('view_doctor', View_Doctor,name="view_doctor"),
    path('view_disease', View_Disease,name="view_disease"),
    path('view_patient', View_Patient,name="view_patient"),
    path('view_feedback', View_Feedback,name="view_feedback"),
    path('edit_profile', Edit_My_deatail,name="edit_profile"),
    path('profile_doctor', View_My_Detail,name="profile_doctor"),
    path('notification', View_My_Notification,name="notification"),
    path('search_doctor', Search_Doctor,name="search_doctor"),
    path('sent_feedback', sent_feedback,name="sent_feedback"),
    path('change_password', Change_Password,name="change_password"),
    path('view_notify', View_Notification,name="view_notify"),
    path('predict_disease<str:pid>', Predict_disease,name="predict_disease"),
    path('edit_doctor<int:pid>', Edit_Doctor,name="edit_doctor"),
    path('edit_disease<int:pid>', Edit_Disease,name="edit_disease"),
    path('delete_doctor<int:pid>', delete_doctor,name="delete_doctor"),
    path('delete_disease<int:pid>', delete_disease,name="delete_disease"),
    path('delete_patient<int:pid>', delete_patient,name="delete_patient"),
    path('delete_feedback<int:pid>', delete_feedback,name="delete_feedback"),
    path('assign_status<int:pid>', Assign_Status,name="assign_status"),
    path('delete_notification<int:pid>', delete_notification,name="delete_notification"),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
