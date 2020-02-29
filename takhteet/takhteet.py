import test
import myiter
import time


print("*********************** WELCOME ***************************")
print("USER GUIDELINES")
print("\n1. The user has to feed-in the following details:\n\ta)Number of students.\n\tb) Total number of days\n\t and then for each student,\n\tc) Student's name.\n\td) Student's current surat/page number and ayat/line number.\n\te) Number of safahs/lines per day assigned to the student.")
print("\n2. Takhteet can be made safah wise or line wise with the least entity of safah being 0.25.")  
print("\n3. All the takhteets of students will be generated in the excel file\n 'takhteet.xlsx' while the program is being\n executed.\n The excel file should be closed while the program is being executed,\n and both the program and the excel file saved in the same directory.")
print("\n4. User can either select the tabular layout or grid layout of takhteet.")
wait = input("\nPRESS ENTER TO CONTINUE.")

print ("\n" * 4)

studs=int(input("Enter number of students "))
year=int(input("Enter hijri year "))
yr=myiter.to_arab(year)
mon=int(input("Enter hijri month no. "))
mont=myiter.month[mon-1]
tno=int(input("Enter total no.of working days of this month "))
form=int(input("Enter 1 for tabular or 2 for grid display of takhteet form in excel "))
print("\n")
z=1
while(studs>0):
    j=0
    print("\n")
    print("For student ",z,":")
    
    name=input("Enter student name ")
    flag=int(input("Enter \n1. for line wise takhteet \n2. for page wise \n"))
    if(flag==2):
        n=float(input("Enter number of pages per day in multiples of 0.25 "))
        sur=int(input("Enter current surat no.  "))
        x=int(input("Enter current ayat number "))
        v=test.line_search2(x,sur,n,tno)
        myiter.to_excel1(v,tno,form,name,n,mont,yr)
    elif(flag==1):
        n=int(input("Enter number of lines per day "))
        sur=int(input("Enter current page no.(1-604)  "))
        x=int(input("Enter current line number(1-15) "))
        v=test.line_search1(x,sur,n,tno)
        myiter.to_excel2(v,tno,form,name,n,mont,yr)
    print("\nTakhteet added in excel sheet")

    studs-=1
    z=z+1
print(" معهد الزهراء-الشارقة")
print("\n")
print(" 'السهولة في التخطيط' ")
print("\n")
print("\n\t Mohammed Kothaliya")
time.sleep(5)
