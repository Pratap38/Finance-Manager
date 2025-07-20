from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Transaction(models.Model):
    Transaction_types=(
        ('income', 'Income'),
        ('expense', 'Expense'),
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.TextField(max_length=100)
    amount=models.FloatField()
    transaction_type=models.CharField(max_length=100,choices=Transaction_types)
    date=models.DateField()
    category=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}-{self.user.username}"
    
class Goal(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    target_amount=models.FloatField()
    current_amount=models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}-{self.user.username}"
