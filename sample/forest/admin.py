from django.contrib import admin
from .models import Feedback_User
from .models import Tole_Samiti,Tole_Samiti_Member,Chetriya_Samiti,Chetriya_Samiti_Member

admin.site.register(Feedback_User)
admin.site.register(Tole_Samiti)
admin.site.register(Tole_Samiti_Member)
admin.site.register(Chetriya_Samiti_Member)
admin.site.register(Chetriya_Samiti)