import sqlite3

email_input = input("What is the email? ")
def email_slice (email_input):
  first_name_slice = email_input.split("@", 1)
  first_name = first_name_slice[0]
  company_list = first_name_slice[1]
  company_splice = company_list.split(".", 1)
  company = company_splice[0]
  print("\n")
  print ("First Name: " + first_name)
  print("Company: " + company)

email_slice(email_input)
