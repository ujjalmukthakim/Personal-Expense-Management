from django.db import models

# Create your models here.

class Transaction(models.Model):
    TYPE_CHOICES=(
        ('income','Income')
        ('expense','Expense')
    )

    title=models.CharField(max_length=50)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    type=models.CharField(max_length=10,choices=TYPE_CHOICES)
    note=models.TextField(blank=True)
    created_at=models.TimeField(auto_now_add=True)

    class Meta:
        ordering=['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.amount}"
    
    