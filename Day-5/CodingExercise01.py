#Average Height without using len() or sum() function
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

sum = 0
length = 0 


for i in student_heights:
  sum += int(i)
  length += 1
print(sum)
print(length)

print("Average Height: ",round(sum/length))