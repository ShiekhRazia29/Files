batch1_students=["Shivani","Sonam","GeetaAngali","Supriya","Avantika","Rahila"]
student_file=open("navgurukul_student.html","w")
student_file.write("<html>\n")
student_file.write("<head>\n")
student_file.write("<tiltle>\n")
student_file.write("</title>\n")
student_file.write("</head>\n")
student_file.write("<body>\n")
student_file.write("<ul>\n")
for student in batch1_students:
    student_file.write("<li>" + student + "</li>")
student_file.write("<ul>\n")
student_file.write("</body>\n")
student_file.write("</html>\n")
student_file.close()


