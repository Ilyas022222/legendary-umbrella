input_file = open('student_marks.txt', 'r')
student_data = {}
for line in input_file:
   name, mark, weight = line.strip()
   mark = float(mark)
   weight = float(weight)
   if name in student_data:
       student_data[name].append((mark, weight))
   else:
       student_data[name] = [(mark, weight)]
input_file.close()
student_averages = {}
for student in student_data:
   assessments = student_data[student]
   total_weighted_marks = 0
   total_weight = 0
   for mark, weight in assessments:
       total_weighted_marks += (mark * weight) / 100
       total_weight += weight
   if total_weight == 100:
       student_averages[student] = total_weighted_marks
output_file = open('student_averages.txt', 'w')
for student in student_averages:
   average = student_averages[student]
   output_file.write(f"{student}, {average:.1f}\n")
output_file.close()
print("Process completed. Check 'student_averages.txt' for the results.")
