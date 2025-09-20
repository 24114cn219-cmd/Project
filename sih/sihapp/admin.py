from django.contrib import admin
from .models import Great, Candidate, Internship

admin.site.register(Candidate)
admin.site.register(Internship)

@admin.register(Great)
class GreatAdmin(admin.ModelAdmin):
    # show role, and depending on role show name/email
    list_display = ("role", "display_name", "email")

    def display_name(self, obj):
        if obj.role == "company":
            return obj.company_name or "Unknown Company"
        return obj.full_name or "Unknown Student"
    
    display_name.short_description = "Name"
