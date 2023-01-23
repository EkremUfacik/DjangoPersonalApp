from rest_framework import serializers
from .models import Personnel, Department
from django.utils.timezone import now

class PersonnelSerializer(serializers.ModelSerializer):
    
    department = serializers.StringRelatedField(read_only = True)
    department_id = serializers.IntegerField(write_only = True)
    days_since_joined = serializers.SerializerMethodField()
    
    class Meta:
        model = Personnel
        fields = (
            "id",
            "days_since_joined",
            "firstname",
            "lastname",
            "is_staffed",
            "title",
            "gender",
            "salary",
            "start_date",
            "department_id",
            "department",
        )
    
    def get_days_since_joined(self, obj):
        return (now() - obj.date_joined).days
        
class DepartmentSerializer(serializers.ModelSerializer):
    personnel = serializers.StringRelatedField(many=True)
    personal_count = serializers.SerializerMethodField()
    class Meta:
        model = Department
        fields = (
            "id",
            "name",
            "personnel",
        )
        
    def get_personal_count(self, obj):
        return obj.personnel.count()