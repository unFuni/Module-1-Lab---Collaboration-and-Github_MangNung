#Write a Python app that will accept student names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll. Your app will
#ask for and accept a student's last name.'
#quit processing student records if the last name entered is 'ZZZ'.
#ask for and accept a student's first name
#ask for and accept the student's GPA as a float
#test if the student's GPA is 3.5 or greater and, if so, print a message saying that the student has made the Dean's List.
#test if the student's GPA is 3.25 or greater and, if so, print a message saying that the studnet has made the Honor Roll.
#Test your app using at least five students.

# Mang Nung
# M02_Case_Study.py
# This code takes student names and GPAs and tests their qualifications for special rolls depending on their GPA.

while True:

   # Last name

   last_name = input("Enter the student's last name (Enter 'ZZZ' to quit): ").upper()

   if last_name == 'ZZZ':

       print("Quitting student records processing.")

       break

   # First name

   first_name = input("Enter the student's first name: ")

   # GPA as a float

   try:

       gpa = float(input("Enter the student's GPA: "))

   except ValueError:

       print("Invalid GPA. Please enter a valid numeric value.")

       continue

   # Qualification for Dean's List

   if gpa >= 3.5:

       print(f"{first_name} {last_name} has made the Dean's List!")

   # Qualification for Honor Roll

   elif gpa >= 3.25:

       print(f"{first_name} {last_name} has made the Honor Roll!")

   else:

       print(f"{first_name} {last_name} does not qualify for Dean's List or Honor Roll.")



