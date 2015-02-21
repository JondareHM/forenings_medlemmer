from django.contrib import admin
from members.models import Person, Department, Volunteer, Member, Activity, ActivityInvite, WaitingList, ActivityParticipant,Family
# Register your models here.


class MemberInline(admin.TabularInline):
    model = Member
    extra = 0
class DepartmentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['name']})
    ]
    list_display = ('name','no_members')
    inlines = [MemberInline]
admin.site.register(Department,DepartmentAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name','department', 'member_since','is_active')
    list_filter = ['department']
admin.site.register(Member, MemberAdmin)

class ActivityParticipantInline(admin.TabularInline):
    model = ActivityParticipant
    extra = 1

class ActivityInviteInline(admin.TabularInline):
    model = ActivityInvite
    extra = 1

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start', 'end', 'is_historic')
    inlines = [ActivityParticipantInline, ActivityInviteInline]
admin.site.register(Activity, ActivityAdmin)

class WaitingListInline(admin.TabularInline):
    model = WaitingList
    extra = 0

class PersonInline(admin.TabularInline):
    model = Person
    extra = 0

class FamilyAdmin(admin.ModelAdmin):
    list_display = ('email','unique')
    inlines = [PersonInline]
admin.site.register(Family, FamilyAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'street', 'placename','zipcity', 'email','family_url','unique')
    inlines = [MemberInline,WaitingListInline]
    search_fields = ('name', 'zipcity')
    def family_url(self, item):
        return '<a href="../family/%d">%s</a>' % (item.family.id, item.family.email)
    family_url.allow_tags = True

admin.site.register(Person,PersonAdmin)

class WaitingListAdmin(admin.ModelAdmin):
    list_display = ('person','department','added')
    list_filter = ['department']
admin.site.register(WaitingList,WaitingListAdmin)