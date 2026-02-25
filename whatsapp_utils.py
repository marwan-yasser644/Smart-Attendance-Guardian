from twilio.rest import Client
from django.conf import settings

def send_whatsapp_notification(phone, student_name, time, lang):
    client = Client(settings.TWILIO_SID, settings.TWILIO_TOKEN)
    
    messages = {
        'ar': f"تحية طيبة، تم تسجيل حضور الطالب ({student_name}) بنجاح اليوم الساعة {time}. ✅",
        'en': f"Hello, Attendance recorded for ({student_name}) today at {time}. ✅"
    }
    
    body = messages.get(lang, messages['ar'])
    
    try:
        message = client.messages.create(
            from_=settings.TWILIO_WHATSAPP_NUMBER,
            body=body,
            to=f'whatsapp:{phone}'
        )
        return message.sid
    except Exception as e:
        print(f"Twilio Error: {e}")
        return None