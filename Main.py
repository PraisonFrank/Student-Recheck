import operator 


StudDets = {"JAMES":80,"ROHITH":87, "ISHITHA":67}

print("The student dictonary is",StudDets)

print("The number of students are",len(StudDets))

#to fnd class average

sum=0

for k in StudDets: 

  sum = sum + StudDets[k] 

class_average = sum/len(StudDets)

print("The class average is =",class_average)

#to fnd no. of students above class average

count=0

for k in StudDets: 

  if StudDets[k] > class_average: 

    count = count + 1

print("The number of students above class average is", count)

#to fnd the topper of the class

out = sorted(StudDets.items(), key = operator.itemgetter(1), reverse = 1)

topper = out[0][0]

print("The Topper of the class is",topper)

 

#to implement recheck

recheck_name = input("Who has applied for recheck?")

new_mark = int(input("What is the new mark?")) 

StudDets[recheck_name] = new_mark

print("The dictonary afer rechecks is",StudDets)

