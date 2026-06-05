#Email slicer
email=input("Enter your Email:-> ")
#want to slice in two part (1) In username (2)Domain name
index=email.index("@")
username=email[:index]
domain=email[index:]
print(f"Username: {username}")
print(f"Domain name: {domain}\n")