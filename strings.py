'''year_of_birth = input("In what year were you born? : ")
print("You were born in " + str(year_of_birth))'''

#Num = int(input("Enter a number : "))
#print(Num * 3)
#input() always returns text (a string).
#int() converts that text into an integer


#Num = (input("Enter a number : ")
#print(Num * 3)

'''current_year = int(input("Enter the currentyear : "))
olympic_year = 1896
years_passed = current_year - olympic_year
#print("The number of years passed since the first Olympic Games is : ", years_passed)
print("it has been", str(years_passed), "years since the first Olympic Games")'''

'''str = "my name is sravan"
print(len(str))'''

#calculate the end time of an event.
#Tips: Convert all input times into minutes to calculate the end time in minutes. Then, convert the end time into hours and minutes with the help of the modulo % operator.
#Split the operations into small parts with the help of the variables start_time, end_time, end_mins, end_hour.
'''hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
duration = int(input("Event duration (minutes): "))

start_time = hour * 60 + mins
end_time = start_time + duration
end_mins = end_time % 60
end_hour = end_time // 60

print(str(end_hour) + ":" + str(end_mins))'''