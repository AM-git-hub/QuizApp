import random
import time
import keyboard
import sys
file1=open("qp.txt","r")

txt=file1.readlines()
ques=0
corr=0
wrng=0
incorrect = []
wrng_ans = []
q_no = []
score = 0
print("You are about to start your quiz.\nYou will be shown the Question followed by 4 options, please type a/b/c/d\naccording to your choice and press enter to attempt the question\n")
print("The Marking scheme for this quiz is +3 for correct answer and -1 for wrong answer\n\n")
while(True):
	s=input("Press 'S' and enter to start the Quiz: ")
	if(s=="s"):
		start=time.time()
		for i in range(0,len(txt)):
			txt[i] = txt[i].rstrip() #to remove the "\n" from all list elements

		for i in range(0,len(txt)):
			if(txt[i]=="QUESTION:"):
				ques+=1
		for i in range(0,ques):
			q_no.append(i)
			
		for i in range(0,ques):
			i=random.choice(q_no)
			for j in range(i*10,(i*10)+10):
				if(j!=2+(i*10) and j!=3+(i*10) and j!=9+(i*10)):
					print(txt[j])
			ans=input("Enter your choice: ")
			if(ans==txt[(i*10)+3]):
				#print("\nCorrect Answer!\n")
				corr+=1
				score+=3
			elif(ans!=txt[(i*10)+3]):
				#print("\nIncorrect Answer!\n")
				wrng+=1
				score-=1
				incorrect.append(i)
				wrng_ans.append(ans)
			q_no.remove(i)
		end=time.time()
		t_taken = round(end-start,2)
		print("\n**************************************************")
		input("The Quiz is complete. Press enter to show the results:")
		print("\nTime taken to attempt the quiz: ",t_taken,"seconds")
		print("Total number of correct answers: ",corr)
		print("Total number of incorrect answers: ",wrng)
		print("Final Score: ",score)
		if(wrng>0):
			print("\n=====================================================")
			print("\nThe following questions were attempted incorrectly:")
			print("\n=====================================================")

		k=0
		for j in incorrect:
			print("\nQuestion: ",txt[(j*10)+1])
			print("\nCorrect Option: ",txt[(j*10)+3])
			print("\nYour Selected Option: ",wrng_ans[k])
			k+=1
			print("\n**************************************************\n")
		break
	else:
		print("\nIncorrect key pressed!")

def save():
	f= open("result.txt","w+")
	#for i in range(10):
		#f.write("This is line %d\r\n" % (i+1))
	f.write("Correct Answers: %d" % corr)
	f.write("\nIncorrect Answers: %d" % wrng)
	f.write("\nTotal Score: %d" % score)
	f.write("\nTotal Time taken: %.2f seconds" % t_taken)
	f.close()
print("\nPress 'P' to print the results or Escape to exit the program")
while True:
    try:
        if keyboard.is_pressed('p'):
            print("\nThe results have been saved in a file called 'result.txt'")
            save()
            input("Press ENTER to exit: ")
            break
        if keyboard.is_pressed('Esc'):
            print("\nyou pressed Esc, so exiting...")
            sys.exit(0)
    except:
        break	
	
