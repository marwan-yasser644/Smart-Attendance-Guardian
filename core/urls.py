from django.contrib import admin
from django.urls import path
from attendance.views import scanner_page, check_attendance

urlpatterns = [
    path('admin/', admin.site.urls), # ده مسار لوحة الإدارة اللي إنت كنت فيها
    path('', scanner_page, name='scanner'), # ده بيخلي الصفحة الاحترافية هي أول حاجة تفتح
    path('check/', check_attendance, name='check_attendance'), # ده المسار اللي بيبعت الداتا والواتساب
]