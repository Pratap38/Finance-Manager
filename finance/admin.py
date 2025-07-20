from django.contrib import admin
from .models import Transaction, Goal

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'amount', 'transaction_type', 'date', 'created_at')
    list_filter = ('transaction_type', 'date', 'user')

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'current_amount', 'target_amount', 'deadline', 'created_at')
    list_filter = ('deadline', 'user')
