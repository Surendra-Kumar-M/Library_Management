from django.contrib import admin
from .models import Book,Member,Transaction,Staff
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'publication_year', 'available_copies', 'rating')
    search_fields = ('title', 'author')
    list_filter = ('genre', 'publication_year')
    ordering = ('title',)

class MemberAdmin(admin.ModelAdmin):
    list_display = ('member_name', 'mail', 'phone', 'membership_type', 'membership_start_date')
    search_fields = ('member_name', 'mail')
    list_filter = ('membership_type',)
    ordering = ('member_name',)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'member', 'book','book__title', 'issue_date', 'return_date', 'status', 'fine_amount')
    list_filter = ('status',)
    search_fields = ('member__member_name', 'book__title')  
    ordering = ('-issue_date',)


class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_name', 'mail', 'role', 'phone')
    search_fields = ('staff_name', 'mail')
    list_filter = ('role',)
    ordering = ('staff_name',)

admin.site.register(Book,BookAdmin)
admin.site.register(Member,MemberAdmin)
admin.site.register(Transaction,TransactionAdmin)
admin.site.register(Staff,StaffAdmin)