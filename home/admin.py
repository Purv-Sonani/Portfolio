from django.contrib import admin
from .models import Profile, ContactInfo, Project, About, Education, Skill

class SingletonAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False  # Prevent deletion to ensure singleton behavior

@admin.register(Profile)
class ProfileAdmin(SingletonAdmin):
    list_display = ['name', 'role']

@admin.register(About)
class AboutAdmin(SingletonAdmin):
    list_display = ['moto', 'location']

@admin.register(ContactInfo)
class ContactInfoAdmin(SingletonAdmin):
    list_display = ['email', 'github_url', 'linkedin_url']

# admin.site.register(Profile)
# admin.site.register(ContactInfo)
admin.site.register(Project)
# admin.site.register(About)
admin.site.register(Education)
admin.site.register(Skill)

