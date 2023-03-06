#Breanna Eafon
#Problem 1
def print_name(name):
  print("The name is",name)
print_name("bre")

#Problem 2
def ninety(a,b,c):
  # a+b+c+d/4=90
  # a+b+c+d=360
  d=360-a-b-c
  return d
print(ninety(12,25,43))

#Problem 3
def miles_per_hour(miles,hours,minutes,seconds):
  time_minute=minutes/60
  time_seconds= seconds/3600
  total=hours+time_minute+time_seconds
  total_hours=miles/total
  return total_hours

print(miles_per_hour(20,2,21,16))

#problem 4
def greeting(name):
  if name=="chris":
    print("Hello Chris")
  else:
    print("Goodbye",name)
greeting("Amy")

#problem 5
def convert_temperature(temp,units):
  if units=="celsius":
    f=(9/5)*temp+32
    return f
  else:
    c=(temp-32)*5/9
    return c

convert_temperature(85,"F")

#Problem 6
def calculate_grade(score):
  if score>=90:
    return "A"
  elif 80 <= score <90:
    return "B"
  elif 70 <= score <=80:
    return "C"
  elif 60 <= score <= 70:
    return "D"
  else:
    return "F"

calculate_grade(78)
