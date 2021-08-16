from django.db import connections
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.http import JsonResponse

from rest_framework.views import APIView
from .models import *
from task.serializers import *
from django.db import connections
from django.core import serializers

from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import *

from rest_framework.parsers import JSONParser
from django.db.migrations import serializer

from rest_framework.response import Response
import logging


class Common(object):

    @staticmethod
    def get_request_data(request):
        try:
            return request.data
        except Exception as e:
            logging.error("There is no request: %s" % e)
            return JsonResponse({'error': 'Request is not there'}, status=status.HTTP_401_UNAUTHORIZED)


common_methods = Common()


########################################################################################################################
# ALL GET METHODS--
@csrf_exempt
@api_view(['GET'])
def personGET(request):
    try:
        person = Person.objects.all()
        serializers = PersonSerializers(person, many=True)
        return JsonResponse(serializers.data, safe=False)
    except Exception as e:
        return JsonResponse(
            {"Success": False, "Message": "Data not fetch", "Payload": []})


@csrf_exempt
@api_view(['GET'])
def functionGET(request):
    try:
        function = Function.objects.all()
        serlizer = FunctionSerializers(function, many=True)
        return JsonResponse(serlizer.data, safe=False)
    except Exception as e:
        return JsonResponse(
            {"Success": False, "Message": e, "Payload": []})


    except Exception as e:
        return Response(
            {"Success": False, "Message": "Data not fetch", "Payload": []})


@csrf_exempt
@api_view(['GET'])
def employeeGET(request):
    try:
        employee = Employee.objects.all()
        serializers = EmployeeSerializers(employee, many=True)
        return Response(serializers.data)
    except Exception as e:
        return JsonResponse(
            {"Success": False, "Message": e, "Payload": []})


@csrf_exempt
@api_view(['GET'])
def teamGET(request):
    try:
        team = Team.objects.all()
        serializers = TeamSerializers(team, many=True)
        return Response(serializers.data)
    except Exception as e:
        return JsonResponse(
            {"Success": False, "Message": e, "Payload": []})


@csrf_exempt
@api_view(['GET'])
def teamMemberGET(request):
    try:
        team = Team.objects.all()
        serializers = TeamMemberSerializers(team, many=True)
        return Response(serializers.data)
    except Exception as e:
        return JsonResponse(
            {"Success": False, "Message": e, "Payload": []})


@csrf_exempt
@api_view(['GET'])
def projectGET(request):
    try:
        team = Project.objects.all()
        serializers = ProjectSerializers(team, many=True)
        return Response(serializers.data)
    except Exception as e:
        return JsonResponse(
            {"Success": False, "Message": e, "Payload": []})


@csrf_exempt
@api_view(['GET'])
def taskGET(request):
    try:
        team = Task.objects.all()
        serializers = TaskSerializers(team, many=True)
        return Response(serializers.data)
    except Exception as e:
        return JsonResponse(
            {"Success": False, "Message": e, "Payload": []})


@csrf_exempt
@api_view(['GET'])
def projectteammemberGET(request):
    try:
        team = ProjectTeamMember.objects.all()
        serializers = ProjectTeamMemberSerializers(team, many=True)
        return Response(serializers.data)
    except Exception as e:
        return JsonResponse(
            {"Success": False, "Message": e, "Payload": []})


@csrf_exempt
@api_view(['GET'])
def membertaskGET(request):
    try:
        team = MemberTask.objects.all()
        serializers = MemberTaskSerializers(team, many=True)
        return Response(serializers.data)
    except Exception as e:
        return JsonResponse(
            {"Success": False, "Message": e, "Payload": []})


########################################################################################################################
# TASK APIs--
# First API-Add Employee with dependent employee Details

@api_view(['POST'])
def firsttask(request):
    try:
        data = common_methods.get_request_data(request)
        conn = connections['default']
        cursor1 = conn.cursor()
        cursor2 = conn.cursor()
        cursor3 = conn.cursor()
        cursor4 = conn.cursor()
        cursor5 = conn.cursor()

        FirstName = request.data['FirstName']
        MiddleName = request.data['MiddleName']
        LastName = request.data['LastName']
        Title = request.data['Title']
        Gender = request.data['Gender']
        Initials = request.data['Initials']
        BirthDate = request.data['BirthDate']

        FunctionName = request.data['FunctionName']
        MinSalary = request.data['MinSalary']
        MaxSalary = request.data['MaxSalary']
        DefaultBillingRate = request.data['DefaultBillingRate']

        EmployeeBillingRate = request.data['EmployeeBillingRate']
        EmployeeWorkPhone = request.data['EmployeeWorkPhone']
        EmployeeFunction = request.data['EmployeeFunction']

        # TeamName = request.data['TeamName']

        person = "INSERT INTO task_person(FirstName,MiddleName,LastName,Title,Gender,Initials,BirthDate) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        personval = (FirstName, MiddleName, LastName, Title, Gender, Initials, BirthDate)
        cursor1.execute(person, personval)
        print("Check=========", cursor1.lastrowid)
        PersonID = cursor1.lastrowid

        function = "INSERT INTO task_function(FunctionName,MinSalary,MaxSalary,DefaultBillingRate) VALUES (%s,%s,%s,%s)"
        functionval = (FunctionName, MinSalary, MaxSalary, DefaultBillingRate)
        cursor2.execute(function, functionval)
        # print("Check=========", cursor2.lastrowid)
        # FunctionCode = cursor2.lastrowid

        employee = "INSERT INTO task_employee(EmployeeID_id, EmployeeBillingRate,EmployeeWorkPhone,EmployeeFunction_id) VALUES (%s,%s,%s,%s)"
        employeeval = (PersonID, EmployeeBillingRate, EmployeeWorkPhone, EmployeeFunction)

        cursor3.execute(employee, employeeval)

        cursor1.close()
        cursor2.close()
        cursor3.close()
        return JsonResponse(
            {"Success": True, "Message": "Data  added Successful",
             "Payload": [PersonID, EmployeeBillingRate, EmployeeWorkPhone, EmployeeFunction]})

    except Exception as e:
        return Response(
            {"Success": False, "Message": e, "Payload": []})


########################################################################################################################
# Second API- Add Team and Team Member
@api_view(['POST'])
def secondtask(request):
    try:
        data = common_methods.get_request_data(request)
        conn = connections['default']
        cursorteam = conn.cursor()
        cursorteammember = conn.cursor()

        TeamName = data['TeamName']
        TeamLeader = data['TeamLeader']

        TeamCode = data['TeamCode']
        EmployeeID = data['EmployeeID']

        teamname = Team.TeamName
        team = "INSERT INTO task_team(TeamName, TeamLeader_id) VALUES (%s,%s)"
        if (teamname.__eq__(TeamName)):
            pass
        else:
            teamval = (TeamName, TeamLeader)
            cursorteam.execute(team, teamval)

        teammember = "INSERT INTO task_TeamMember( EmployeeID_id,TeamCode_id) VALUES (%s,%s)"
        teammemberval = (EmployeeID, TeamCode)
        cursorteammember.execute(teammember, teammemberval)

        cursorteam.close()
        cursorteammember.close()

        return Response(
            {"Success": True, "Message": "Data  added Successful",
             "Payload": [TeamName, TeamLeader, TeamCode, EmployeeID]})


    except Exception as e:
        return Response(
            {"Success": False, "Message": e, "Payload": []})


########################################################################################################################
# Third API- Add Project and Task under the project

@api_view(['POST'])
def thirdtask(request):
    try:
        data = common_methods.get_request_data(request)
        conn = connections['default']
        cursorproject = conn.cursor()
        cursortask = conn.cursor()

        TeamCode = data['TeamCode']
        ProjectName = data['ProjectName']
        ProjectDescription = data['ProjectDescription']
        ProjectLeader = data['ProjectLeader']

        TaskName = data['TaskName']
        ProjectCode = data['ProjectCode']
        TaskDescription = data['TaskDescription']
        TaskCost = data['TaskCost']
        TaskDueDate = data['TaskDueDate']
        TaskCreateDate = data['TaskCreateDate']

        PName = Project.ProjectName

        project = "INSERT INTO task_Project(ProjectName, ProjectDescription, ProjectLeader_id, TeamCode_id) VALUES (%s,%s,%s,%s)"
        if (PName.__eq__(ProjectName)):
            pass
        else:
            projectval = (ProjectName, ProjectDescription, ProjectLeader, TeamCode)
            cursorproject.execute(project, projectval)

        task = "INSERT INTO task_Task(TaskName, TaskDescription, TaskCost, TaskDueDate, TaskCreateDate, ProjectCode_id) VALUES(%s,%s,%s,%s,%s,%s)"
        taskval = (TaskName, TaskDescription, TaskCost, TaskDueDate, TaskCreateDate, ProjectCode)
        cursortask.execute(task, taskval)

        cursorproject.close()
        cursortask.close()
        return Response(
            {"Success": True, "Message": "Data  added Successful",
             "Payload": []})

    except Exception as e:
        return Response(
            {"Success": False, "Message": e, "Payload": []})


########################################################################################################################
# Fourth API- Add Project Team and Update the members to the task under the project

@api_view(['POST'])
def fourthtask(request):
    try:
        data = common_methods.get_request_data(request)
        conn = connections['default']
        cursorproject = conn.cursor()
        # cursortmembertask = conn.cursor()

        TeamCode = data['TeamCode']
        ProjectCode = data['ProjectCode']
        EmployeeID = data['EmployeeID']

        TaskName = data['TaskName']

        project = "INSERT INTO task_ProjectTeamMember(EmployeeID_id,ProjectCode_id,TeamCode_id) VALUES(%s,%s,%s)"
        projectval = (EmployeeID, ProjectCode, TeamCode)
        cursorproject.execute(project, projectval)

        member = "INSERT INTO task_MemberTask(EmployeeID_id, ProjectCode_id, TaskName_id, TeamCode_id) VALUES(%s,%s,%s,%s)"
        memberval = (EmployeeID, ProjectCode, TaskName, TeamCode)
        cursorproject.execute(member, memberval)

        cursorproject.close()
        # cursortmembertask.close()
        return Response(
            {"Success": True, "Message": "Data  added Successful",
             "Payload": []})

    except Exception as e:
        print(e)
        return Response(
            {"Success": False, "Message": e, "Payload": []})


########################################################################################################################
# Fifth API- Modify team member if any team members are a part of the project then we should not allow removing
#            or changing the teams.
@api_view(['POST'])
def fifthtask(request):
    try:
        data = common_methods.get_request_data(request)
        EmployeeID = data['EmployeeID']
        TeamCode = data['TeamCode']

        conn = connections['default']
        cursor1 = conn.cursor()
        employee = cursor1.execute('SELECT ProjectCode_id FROM task_projectteammember WHERE EmployeeID_id=%s', [EmployeeID])
        # cursor1.fetchall(employee)
        print(employee)

        # employee = ProjectTeamMember.objects.raw('SELECT ProjectCode_id FROM task_projectteammember WHERE EmployeeID_id=%s', [EmployeeID])
        # print(employee)










        # if employee.__eq__(0):
        #     changeTeam = TeamMember.objects.raw('UPDATE TeamMember SET TeamCode_id=%s WHERE EmployeeID_id=%s',[TeamCode, EmployeeID])
        #     return Response(
        #         {"Success": True, "Message": "Employee team has changed", "Payload": [TeamCode, EmployeeID]})
        # else:
        #     return Response({"Success": False, "Message": "Employee has assigned a project", "Payload": []})
        #
        # # return Response(
        # #     {"Success": True, "Message": "Success", "Payload": [employee]})
        # cursor.close()
    except Exception as e:
        return Response(
            {"Success": False, "Message": e, "Payload": []})


########################################################################################################################
# Sixth API- Modify Team Members for the task- Team members should be a part of the team
#            that are assigned to the project

@api_view(['POST'])
def sixthtask(request):
    try:
        data = common_methods.get_request_data(request)
        conn = connections['default']
        cursor1 = conn.cursor()
        # cursortmembertask = conn.cursor()

        EmployeeID = data['EmployeeID']

        cursor1.close()
        # cursortmembertask.close()
    except Exception as e:
        return Response(
            {"Success": False, "Message": e, "Payload": []})
