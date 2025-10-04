from django.contrib import admin
from .models import Profile, ContactInfo, Project, About, Education, Skill, TechStack, Experience, ContactSubmission
from .forms import ExperienceForm


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
    list_display = ['email', 'github_url', 'linkedin_url', 'phone_number']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('tech_stacks',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    form = ExperienceForm
    list_display = ('company', 'role', 'duration')

# admin.site.register(Profile)
# admin.site.register(ContactInfo)
# admin.site.register(Project)
admin.site.register(TechStack)
# admin.site.register(About)
admin.site.register(Education)
admin.site.register(Skill)

class ContactSubmissionAdmin(admin.ModelAdmin):
    """
    Admin options for the ContactSubmission model.
    """
    # This makes the list view more useful than the default "ContactSubmission object (1)"
    list_display = ('name', 'email', 'submitted_at')

    # This function removes the "Add" button
    def has_add_permission(self, request):
        return False

    # (Recommended) This function removes the ability to edit a submission
    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(ContactSubmission, ContactSubmissionAdmin)

