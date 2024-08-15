from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    def getUsername(self, obj):
        return obj.user.username
    
    def getFirstName(self, obj):
        return obj.user.first_name
    
    def getLastName(self, obj):
        return obj.user.last_name

    def getEmail(self, obj):
        return obj.user.email

    username = serializers.SerializerMethodField("getUsername")
    firstName = serializers.SerializerMethodField("getFirstName")
    lastName = serializers.SerializerMethodField("getLastName")
    email = serializers.SerializerMethodField("getEmail")
    
    class Meta:
        model = Profile
        fields = ['username', 'firstName', 'lastName', 'initials', 'email', 'unique', 'address', 'idnum', 'cell', 'homenum', 'designation', 'image']
