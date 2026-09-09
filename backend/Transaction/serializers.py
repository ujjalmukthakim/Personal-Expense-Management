from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields='__all__'
    
    def validate_amount(self,value):
        if value<=0:
            raise serializers.ValidationError("The amount should be more than 0 ")
        return value
    
    def validate_title(self,value):
        if not value:
            return value
        value=value.strip()
        if len(value)<=3:
            raise serializers.ValidationError("There should be at least one letter . . .")
        return value
        