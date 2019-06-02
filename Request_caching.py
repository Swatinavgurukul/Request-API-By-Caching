import requests
import json
import os
import pprint
saral_url="http://saral.navgurukul.org/api/courses"
def request(url):
        response= requests.get(url)
        with open("coursesData.json","w") as file:
                file.write(response.content)
        return response.json()
# pprint.pprint(request(saral_url))
def read_file(f_read):
        with open("coursesData.json","r") as file:
                data_read=file.read()
                # print data_read
                data_load=json.loads(data_read)
                # print data_load
        return(data_load)
# read_file()
# pprint.pprint(read_file())
coursesIdList=[]
def saral_courses(data_load):

        for index in range(len(data_load['availableCourses'])):
                courses=data_load['availableCourses'][index]
                courses_name=courses['name']
                coursesId=courses['id']
                coursesIdList.append(coursesId)
                print index+1,"-",courses_name," * ID of courses-",coursesId
        return coursesIdList
# saral_courses()

if os.path.exists("coursesData.json"):
        data_load=read_file("coursesData.json")
        saral_courses(data_load)
        print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
else:
        request(saral_url)
        data_load=read_file("coursesData.json")
        saral_courses(data_load)
        print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

userInput=input("select courses - ")
def selectCourse():
        selecteCourseId=coursesIdList[userInput-1]
        return selecteCourseId
print selectCourse()
print "*****************************************************************"
# request(saral_url)


saral_url1= saral_url+"/"+ str(selectCourse()) +"/exercises"
print(saral_url1)


def requestExercises(url1):
        response= requests.get(url1)
        with open("exercises_"+str(selectCourse())+".json","w") as exercisesFile:
                exercisesFile.write(response.content)
        return response.json()
# requestExercises(saral_url1)
# pprint.pprint(requestExercises(saral_url1))


def read_file(f_read):
        with open("exercises_"+str(selectCourse())+".json","r") as exercisesFile:
                data_read=exercisesFile.read()
                data_load1=json.loads(data_read)
        return(data_load1)

# all_exercises=None
childExercise = []
exercisesSlugList=[]
def saral_exercises(data_lode1):
    if data_lode1 != []:
        # print data_lode1
        available_exercises=data_lode1['data']
        for index in range(len(available_exercises)):
                exercises=available_exercises[index]
                # print exercises
                all_exercises=exercises['parentExerciseId']
                # print all_exercises
                childExerciseList = exercises["childExercises"]
                childExercise.append(childExerciseList)
                if all_exercises !=[]:
                    exercises_name=exercises['name']
                    exercisesSlug=exercises['slug']
                    exercisesSlugList.append(exercisesSlug)
                print index+1,"-",exercises_name
        return childExercise
    # saral_exercises()
    else:
        print "In this Course not Exercise"

print "********************************************************"



if os.path.exists("exercises_"+str(selectCourse())+".json"):
        data_lode1=read_file("exercises_"+str(selectCourse())+".json")
        saral_exercises(data_lode1)
        print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
else:

        requestExercises(saral_url1)
        data_lode1=read_file("exercises_"+str(selectCourse())+".json")
        saral_exercises(data_lode1)
        print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

print "*************************************************************"


# userInput1=input("select Exercise - ")
# def selecteExercise():
#         selecteExerciseId=exercisesSlugList[userInput1-1]
#         return selecteExerciseId
# print selecteExercise()

userInput1=input("select Exercise - ")
def selecteExercise():
        selecteExerciseId=exercisesSlugList[userInput1-1]
        return selecteExerciseId
# print selecteExercise()
saral_url2=saral_url+"/"+str(selectCourse())+"/exercise/getBySlug?slug="+str(selecteExercise())
print saral_url2


def requestContent(url2):  
        response= requests.get(url2)
        with open("exContent_"+str(userInput1)+".json","w") as file:
                file.write(response.content)      
        return response.json()
# requestContent(saral_url2)
# pprint.pprint(request(saral_url2))

def read_content_file(f_read):
        with open("exContent_"+str(userInput1)+".json","r") as file:
                data_read=file.read()
                # print data_read
                data_lode3=json.loads(data_read)
                # print data_lode3
        return(data_lode3)

def exercise_content(data_lode3):
        contentEx=data_lode3["content"]
        print contentEx
# print exercise_content()

if os.path.exists("exContent_"+str(userInput1)+".json"):
        data_lode3=read_content_file("exContent_"+str(userInput1)+".json")
        exercise_content(data_lode3)
        print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
else:
        requestContent(saral_url2)
        data_lode3=read_content_file("exContent_"+str(userInput1)+".json")
        exercise_content(data_lode3)
        print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"


print "**********************************************"

childSlugList = []
def childExerciseFun():
    for index in range(len(childExercise[userInput1])):
        childExIndex = childExercise[userInput1][index]
        childName = childExIndex["name"]
        childSlug = childExIndex["slug"]
        childSlugList.append(childSlug)
        print index +1 , "-", childName
    return childSlugList
childExerciseFun()

print "*********************************************************"

if childSlugList != []:

        selectChildEx = int(raw_input("Selsec the ChildEx :-"))
        if selectChildEx > 0 and selectChildEx < len(childSlugList):
                childExSlug = childSlugList[selectChildEx-1]

                childSlugUrl="http://saral.navgurukul.org/api/courses/"+str(userInput1-1)+"/exercise/getBySlug?slug="+childExSlug


                def requestChildCon(childurl):  
                        response= requests.get(childurl)
                        with open("childContent_"+str(selectChildEx)+".json","w") as file:
                                file.write(response.content)      
                        return response.json()
                # requestChildCon(childSlugUrl)

                def read_file(f_read):
                        with open("childContent_"+str(selectChildEx)+".json","r") as file:
                                data_read=file.read()
                                data_load4=json.loads(data_read)
                        return(data_load4)


                def contentChild(data_load4):
                        content = data_load4["content"]
                        print content
                        # contentChild()


                if os.path.exists("childContent_"+str(selectChildEx)+".json"):
                        data_load4=read_file("childContent_"+str(selectChildEx)+".json")
                        contentChild(data_load4)
                        print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
                else:
                        requestChildCon(childSlugUrl)
                        data_load4=read_file("childContent_"+str(selectChildEx)+".json")
                        contentChild(data_load4)
                        print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
        else: 
                print "This child exercise not in this exercise."
else:
        print "In this exercise not child exercise."
print "***********************************************************"

