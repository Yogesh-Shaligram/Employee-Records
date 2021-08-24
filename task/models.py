from django.db import models


class Person(models.Model):
    PersonID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    MiddleName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Initials = models.CharField(max_length=50)
    Title = models.CharField(max_length=50)
    Gender = models.CharField(max_length=50)
    BirthDate = models.DateField(null=True)


class Function(models.Model):
    FunctionCode = models.AutoField(primary_key=True)
    FunctionName = models.CharField(max_length=50)
    MinSalary = models.IntegerField(null=True)
    MaxSalary = models.IntegerField(null=True)
    DefaultBillingRate = models.FloatField(null=True)

#One Employee ID one Person ID((One)EmployeeID---(One)PersonID)
#One Function Many Employee ((One)FunctionCode----(Many)EmployeeFunction)


class Employee(models.Model):
    ID = models.AutoField(primary_key=True)
    EmployeeID = models.ForeignKey(Person, null=True, on_delete=models.CASCADE)
    EmployeeBillingRate = models.IntegerField(null=True)
    EmployeeWorkPhone = models.IntegerField(null=True)
    EmployeeFunction = models.ForeignKey(Function, null=True, on_delete=models.CASCADE)


class Team(models.Model):
    TeamCode = models.AutoField(primary_key=True)
    TeamName = models.CharField(max_length=50)
    TeamLeader = models.ForeignKey(Person, null=True, on_delete=models.CASCADE)

#One Team one Team Code
#One Team many Team members ((One)TeamCode---(Many)EmployeeID)
#One Team One Team Leader((One)TeamCode---(One)TeamLeader)


class TeamMember(models.Model):
    id = models.AutoField(primary_key=True)
    TeamCode = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    EmployeeID = models.ForeignKey(Person, null=True, on_delete=models.CASCADE)


class Project(models.Model):
    ProjectCode = models.AutoField(primary_key=True)
    TeamCode = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    ProjectName = models.CharField(max_length=50)
    ProjectDescription = models.CharField(max_length=50)
    ProjectLeader = models.ForeignKey(Person, null=True, on_delete=models.CASCADE)


#One Poject one Project leader((One)PeojectCode---(One)ProjectLeader)
#One Project mant task((One)ProjectCode---(Many))

class Task(models.Model):
    TaskName = models.CharField(max_length=50, primary_key=True)
    ProjectCode = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
    TaskDescription = models.CharField(max_length=50)
    TaskCost = models.IntegerField()
    TaskDueDate = models.DateField()
    TaskCreateDate = models.DateField()


class ProjectTeamMember(models.Model):
    TeamCode = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    ProjectCode = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
    EmployeeID = models.ForeignKey(Person, null=True, on_delete=models.CASCADE)


class MemberTask(models.Model):
    TeamCode = models.ForeignKey(Team, null=True, related_name='task_TeamCode', on_delete=models.CASCADE)
    ProjectCode = models.ForeignKey(Project, null=True, related_name='task_ProjCode', on_delete=models.CASCADE)
    TaskName = models.ForeignKey(Task, null=True, unique=True, on_delete=models.CASCADE)
    EmployeeID = models.ForeignKey(Person, null=True, related_name='task_EmployeeID', on_delete=models.CASCADE)
