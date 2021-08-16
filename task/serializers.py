from .models import *
from rest_framework import serializers


class PersonSerializers(serializers.Serializer):
    PersonID = serializers.IntegerField()
    LastName = serializers.CharField(max_length=50)
    MiddleName = serializers.CharField(max_length=50)
    FirstName = serializers.CharField(max_length=50)
    Initials = serializers.CharField(max_length=50)
    Title = serializers.CharField(max_length=50)
    Gender = serializers.CharField(max_length=50)
    BirthDate = serializers.IntegerField()

    def create(self, validated_data):
        return Person.objects.create(**validated_data)


class FunctionSerializers(serializers.Serializer):
    FunctionCode = serializers.IntegerField()
    FunctionName = serializers.CharField(max_length=50)
    MinSalary = serializers.IntegerField()
    MaxSalary = serializers.IntegerField()
    DefaultBillingRate = serializers.FloatField()

    def create(self, validated_data):
        return Function.objects.create(**validated_data)


class EmployeeSerializers(serializers.Serializer):
    ID = models.IntegerField()
    EmployeeID = models.IntegerField()
    EmployeeBillingRate = models.IntegerField()
    EmployeeWorkPhone = models.IntegerField()
    EmployeeFunction = models.IntegerField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

class TeamSerializers(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

    def create(self, validated_data):
        return Team.objects.create(**validated_data)


class TeamMemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'

    def create(self, validated_data):
        return TeamMember.objects.create(**validated_data)


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

    def create(self, validated_data):
        return Project.objects.create(**validated_data)


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        return Task.objects.create(**validated_data)


class ProjectTeamMemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProjectTeamMember
        fields = '__all__'

    def create(self, validated_data):
        return ProjectTeamMember.objects.create(**validated_data)

class MemberTaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = MemberTask
        fields = '__all__'

    def create(self, validated_data):
        return MemberTask.objects.create(**validated_data)


