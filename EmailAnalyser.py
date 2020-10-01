import time
print("Hello!")
time.sleep(1)
print("Im Itachi Uchiha!")
time.sleep(1)
print("Thanks For Using My Email Analyser!")
time.sleep(1)


print("Enter Email To Analyse!")
email=input()
l=email.find("@")
id= email[:l:]
dom =email[l+1::]
print("Analysing Email")
time.sleep(1)
print(f"The Username Is {id}")
time.sleep(1)
print(f"The Domain Of Email Hosting Service Is {dom}")









	
	



	
