#python program to find total and percentage of five subjects
English=float(input("please enter english marks:"))
Math=float(input("please enter math score:"))
Computer=float(input("please enter computer marks:"))
Science=float(input("please enter  science marks:"))
Chemistry=float(input("please enter chemistry marks:"))
total = English+Math+Computer+Science+Chemistry
average=total/5
percentage =(total/500)*100
print("Total Marks =%.2f" %total)
print("Average Marks =%.2f" %average)
print("Marks Percentage =%.2f" %percentage)
