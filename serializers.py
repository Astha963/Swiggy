from rest_framework import serializers
from users.models import (Student,)

class CreatedBySerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('__all__')