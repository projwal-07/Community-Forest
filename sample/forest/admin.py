from django.contrib import admin
from .models import Feedback_User
from .models import Tole_Samiti,Tole_Samiti_Member,Chetriya_Samiti,Chetriya_Samiti_Member,Lekha_Samiti_Member,Karya_Samiti_Member,Salakar_Samiti_Member

admin.site.register(Feedback_User)
admin.site.register(Tole_Samiti)
admin.site.register(Tole_Samiti_Member)
admin.site.register(Chetriya_Samiti_Member)
admin.site.register(Chetriya_Samiti)
@admin.register(Salakar_Samiti_Member)
class SalakarSamitiMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'image')  # Fields to display in the list view
    search_fields = ('name', 'position')          # Fields to search by
    list_filter = ('position',)                   # Filter by position
admin.site.register(Lekha_Samiti_Member)
admin.site.register(Karya_Samiti_Member)

