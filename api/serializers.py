from rest_framework import serializers
from medicine.models import medicine

class medicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = medicine
        fields = '__all__'