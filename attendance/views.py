from django.shortcuts import render
from django.http import JsonResponse
from .models import Student, Attendance
from django.utils import timezone
import pywhatkit as kit
import datetime

def scanner_page(request):
    return render(request, 'attendance/scanner.html')

def check_attendance(request):
    student_id = request.GET.get('id')
    try:
        student = Student.objects.get(id=student_id)
        # 1. تسجيل الحضور في الداتا بيز
        attendance, created = Attendance.objects.get_or_create(
            student=student, 
            date=timezone.now().date(),
            defaults={'is_present': True}
        )
        
        if created:
            # 2. إرسال رسالة الواتساب
            phone_number = student.parent_phone
            # تأكد إن الرقم بيبدأ بـ +2 (كود مصر)
            if not phone_number.startswith('+'):
                phone_number = f"+2{phone_number}"
            
            message = f"تحية طيبة، نود إخباركم أن الطالب {student.name} قد وصل للمركز في تمام الساعة {datetime.datetime.now().strftime('%H:%M')}"
            
            # إرسال الرسالة (ستفتح المتصفح وترسل تلقائياً)
            kit.sendwhatmsg_instantly(phone_number, message, wait_time=15, tab_close=True)
            
            return JsonResponse({'status': 'success', 'name': student.name, 'msg': 'تم تسجيل الحضور وإرسال رسالة'})
        else:
            return JsonResponse({'status': 'info', 'message': 'الطالب مسجل حضور بالفعل اليوم'})
            
    except Student.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'طالب غير مسجل!'})