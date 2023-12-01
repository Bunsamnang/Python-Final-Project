# Python program to create a simple GUI
# Simple Quiz using Tkinter
#import everything from tkinter
from tkinter import *

# and import messagebox as mb from tkinter
from tkinter import messagebox as mb

#import json to use json file for data
import json
import time
import random



#class to define the components of the GUI
class mathQuiz:
	# This is the first method which is called when a
	# new object of the class is initialized. This method
	# sets the question count to 0. and initialize all the
	# other methoods to display the content and make all the
	# functionalities available
	def __init__(self):
		
		# set question number to 0
		self.q_no=0

		# Set the time limit for each question (in seconds)
		self.time_limit = 45

		# Set the start time to the current time
		self.start_time = time.time()
		
		# Create label for the timer
		self.timer_label = Label(root, text="", font=('ariel', 12), bg='red')
		
		# Display title
		self.display_title()

		# Have a new randomized order of questions every time they
		# quit and start the quiz again
		self.shuffle_questions_and_options()

		# assigns ques to the display_question function to update later.
		self.display_question()
		
		
		# option_selected holds an integer value which is used for
		# selected option in a question.
		self.option_selected=IntVar()
		
		# displaying radio button for the current question and used to
		# display options for the current question
		self.options=self.radio_buttons()
		
		# display options for the current question
		self.display_options()
		
		# displays the button for next, quit, view answers
		self.buttons()
		
		# no of questions
		self.data_size=len(math_question)
		
		# keep a counter of correct answers
		self.correct=0

		# Schedule the update_timer method to start updating the timer
		root.after(1000, self.update_timer)


	# This method is used to Display Title
	def display_title(self):
		
		# The title to be shown
		title = Label(root, text="MATH QUIZ",
		width=75, bg="grey30",fg="white", font=("ariel", 20, "bold"))
		root.configure(bg = 'lightgrey')
		# place of the title
		title.place(x=0, y=2)

	
	# This method shuffles the questions order randomly every time users take the quiz
	def shuffle_questions_and_options(self):
		indices = random.sample(range(len(math_question)), len(math_question))

		math_question[:] = [math_question[i] for i in indices]
		math_answer_options[:] = [math_answer_options[i] for i in indices]
		math_answers[:] = [math_answers[i] for i in indices]



	# This method shows the current Question on the screen
	def display_question(self):
		
		question_no_label = Label(root, text = f'Question {self.q_no + 1}:', width = 40, bg = 'lightgrey', 
		font = ('ariel', 16, 'bold'), anchor= 'w')
		question_no_label.place(x = 70, y = 50)

		# setting the Question properties
		q_no = Label(root, text=math_question[self.q_no], width=100, bg = 'lightgrey',
		font=( 'ariel' , 16 , 'bold' ), anchor= 'w' )
		
		#placing the option on the screen
		q_no.place(x=70, y=100)


	# This method sets a timer for each question
	def update_timer(self):
		
		# Calculate the elapsed time
		elapsed_time = int(time.time() - self.start_time)

		# Calculate the remaining time
		self.remaining_time = max(0, self.time_limit - elapsed_time)

		# Update the timer label
		self.timer_label.config(text=f"Time Remaining: {self.remaining_time} seconds", font = ('ariel', 15, 'bold'), bg = 'lightgrey', fg= 'firebrick1')
		self.timer_label.place(x = 800, y = 50)

		# Check if time is up
		if self.remaining_time == 0:
			mb.showinfo('Time Up', 'You have run out of time for this question!')
			self.next_btn()  # Move to the next question
		

		
		# Continue updating the timer every second
		root.after(1000, self.update_timer)




	# This method shows the radio buttons to select the Question
	# on the screen at the specified position. It also returns a
	# list of radio button which are later used to add the options to
	# them.
	def radio_buttons(self):
		
		# initialize the list with an empty list of options
		q_list = []
		
		# position of the first option
		y_pos = 150
		
		# adding the options to the list
		while len(q_list) < 4:
			
			# setting the radio button properties
			radio_btns = Radiobutton(root,text=" ",variable=self.option_selected,
			value = len(q_list)+1,font = ("ariel",14), bg = 'lightgrey')
			
			# adding the button to the list
			q_list.append(radio_btns)
			
			# placing the button
			radio_btns.place(x = 100, y = y_pos)
			
			# incrementing the y-axis position by 40
			y_pos += 40
		
		# return the radio buttons
		return q_list
	

	# This method deselect the radio button on the screen
	# Then it is used to display the options available for the current
	# question which we obtain through the question number and Updates
	# each of the options for the current question of the radio button.
	def display_options(self):
		val=0
		
		# deselecting the options
		self.option_selected.set(0)
		
		# looping over the options to be displayed for the
		# text of the radio buttons.
		for option in math_answer_options[self.q_no]:
			self.options[val]['text']=option
			val+=1



	# This method checks the Answer after we click on Next.
	def check_answer(self, q_no):
		
		# checks for if the selected option is correct
		if self.option_selected.get() == math_answers[q_no]:
			# if the option is correct it return true
			return True


	
	# This method checks if users select their answer or not
	def check_option_selected(self):
		return not self.option_selected.get()




	# This method is used to check the answer of the
	# current question by calling the check_answer and question no.
	# if the question is correct it increases the count by 1
	# and then increase the question number by 1. If it is last
	# question then it calls display result to show the message box.
	# otherwise shows next question.
	def next_btn(self):

		# Check if the answer is correct or not and that the users did select their answers
		if self.check_answer(self.q_no) and not self.check_option_selected():
			mb.showinfo('', 'Your answer is correct')
			# if the answer is correct it increments the correct by 1
			self.correct += 1
		if not self.check_answer(self.q_no) and not self.check_option_selected():
			mb.showinfo('', 'Your answer is incorrect')



		# Check if users select their answer or not and the time is up or not after clicking the next button
		# if not, they will get an error pop up on the screen
		# if yes, they will move to the next question
		if self.check_option_selected() and self.remaining_time != 0:
			mb.showerror('Option not selected', 'Please select your answer!')

		# Check if the time is up and also if the user did not select their answer
		# if true, showinfor, and move to the next question
		if self.check_option_selected() and self.remaining_time == 0:
			mb.showinfo('', 'You did not select you answer!')
			self.q_no += 1 
			self.start_time = time.time()

		# If user did select their answer, they will be graded and moved to next question
		if not self.check_option_selected():
			self.q_no += 1
			self.start_time = time.time()
		
	

		# checks if the q_no size is equal to the data size
		if self.q_no == self.data_size:
			
			# if it is correct then it displays the score
			self.display_result()
			
			# destroys the GUI
			
		else:
			# shows the next question
			self.display_question()
			self.display_options()
	
	




	# This method shows the two buttons on the screen.
	# The first one is the next_button which moves to next question
	# It has properties like what text it shows the functionality,
	# size, color, and property of text displayed on button. Then it
	# mentions where to place the button on the screen. The second
	# button is the exit button which is used to close the GUI without
	# completing the quiz.
	def buttons(self):
		
		# The first button is the Next button to move to the
		# next Question
		next_btn = Button(root, text="Next Question",command=self.next_btn,
		width=15,bg="firebrick2",fg="white",font=("ariel",16,"bold"))
		
		# placing the button on the screen
		next_btn.place(x=480,y=380)
		
		# This is the second button which is used to Quit the GUI
		quit_btn = Button(root, text="Quit", command=root.destroy,
		width=5,bg="firebrick1", fg="white",font=("ariel",16," bold"))
		
		# placing the Quit button on the screen
		quit_btn.place(x=1100,y=50)

		view_correct_answer_btn = Button(root, text = 'View correct answers', width = 18, bg = 'firebrick', fg = 'white', font=("ariel",16," bold"), command = self.view_correct_btn)
		view_correct_answer_btn.place(x = 740, y = 380)


	# This method is used to display the result
	# It counts the number of correct and wrong answers
	# and then display them at the end as a message Box
	def display_result(self):
		
		# calculates the wrong count
		wrong_count = self.data_size - self.correct
		correct = f"Correct: {self.correct}"
		wrong = f"Wrong: {wrong_count}"
		
		# calcultaes the percentage of correct answers
		score = int(self.correct / self.data_size * 100)
		result = f"Score: {score}%"
		
		# Shows a message box to display the result
		mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")


	
	# Check if users try to view answers when they did not complete their quiz yet
	def view_correct_btn(self):
		if self.q_no != self.data_size:
			mb.showinfo('Access denied', 'Please complete your quiz first!')
		elif self.correct == self.data_size:
			mb.showinfo('', 'You have it all correct!')
		else:
			new_Window = Toplevel(root)
			new_Window.title('View Correct Answers')
			new_Window.geometry('1500x900')
			new_Window.configure(bg = 'lightgrey')

			question_frame = LabelFrame(new_Window, text = 'Questions', width = 300, height = 300, bg = 'lightgrey')
			question_frame.grid(column = 0, row = 0)

			question_label = Label(question_frame, text = "1. What is 8(-5) - (-8)?\n2. Given a = 5 and b = 3, what is the value of (3a + 2b) / 3\n3. A farmer has 100 chickens. If every chicken lays 1 egg per day, how many eggs does the farmer get in 1 week?\n4. Given (X + 5) x 5 = 70 what is the value of X?\n5. What is the area of a circle with a diameter of 20 inches if pi= 3.1415?\n6. What is the square root of 144?\n7. Given: 33, 55, 77, 99, ? What is the next number here?\n8. Given: A is 1, O is 15, H is 8, U is ?\n9. What is the sum of the angles in a triangle?\n10. What is the approximate value of mathematical constant e\n11. What is the number needed to fill in the question mark? Circle, Triangle, Diamond, Circle, ...?, Diamond Circle\n12. What is a prime number?\n13. Which of these number is/are even number(s)?\n14. What is the number needed to fill in the question mark? 100, 97.4, 94.8, ...? , 89.6, 87\n15. What is the number needed to fill in the question mark? (36)(1216)(48), (24)(824)(72), (42)(...?)(51)\n16. What is the next number in the sequence: 2, 4, 8, 16, 32, ...?\n17. A farmer has 150 cows. He sells 2/5 of his cows. How many cows does he have left?\n18. What is the next number in the sequence: 2, 6, 12, 20, 30, ...?\n19. What is the area of a rectangle with length 8 cm and width 5 cm?\n20. What is the value of 2^4 x 3^2?",
						  font=('ariel', 10, 'bold'), anchor='w', justify='left', bg = 'lightgrey')
			question_label.grid(column = 0, row = 0, sticky = 'w', padx = 10, pady = 5)

			answer_frame = LabelFrame(new_Window, text = "Answers", width = 300, height = 300, bg = 'lightgrey')
			answer_frame.grid(column=1, row = 0)


			answer_label = Label(answer_frame, text ="1. -32\n2. 7: \n (3(5) + 2(3)) / 3 = (15 + 6) / 3 = 21 / 3 = 7\n3. 700 eggs: \n Chicken in total = 100, each lays 1 egg per day, and 1 week is 7 days so 7 times 100 = 700\n4. 9\n5. 314.15 Inches: \n Area of a circle = radius^2 x pi = diameter^2 / 4 x pi\n6. 12\n7. 121: \n 3 x 11, 5 x 11, 7 x 11, 9 x 11, 11 x 11\n8. 21: \n The index number of letter U is 21\n9. 180 degrees\n10. 2.72\n11. Triangle: \n It is a cycle: Circle, Triangle, Diamond, Circle, [Triangle], Diamond, Circle\n12. Can only be divided by 1 and itself\n13. 22 and 14: \n Even numbers are numbers that can be divided by number 2\n14. 92.2: \n The sequence of numbers is subtracted by 2.6 all the way to the end\n15. 1417: \n 42 / 3 = 14, 51 / 3 = 17, put the answer together, we get 1417, the other two are also done like this.\n16. 64: \n The sequence of the numbers are multiplied by 2 or that the the sequence numbers start from 2^1\n and then add 1 to the exponent \n 2 = 1 x 2, 4 = 2 x 2, 8 = 4 x 2, 16 = 8 x 2, 32 = 16 x 2, 64 = 32 x 2\n17. 90 cows: \n Total = 150, 2/5 of his cow = 150 x 2 / 5 = 60, sell means subtraction: 150 - 60 = 90\n18. 42: \n The number shown in the bracket below is increased by 2 sequence after sequence. \n 2, 6 = 2 + [4], 12 = 6 + [6], 20 = 12 + [8], 30 = 20 + [10], 42 = 30 + [12]\n19. 40 square cm: \n Area of a rectangle is Length x Width, so 8 cm times 5 cm is 40 square cm.\n20. 144: \n 2^4 = 2 x 2 x 2 x 2 = 16, 3^2 = 3 x 3 = 9, so 16 x 9 = 144.",
						font=('ariel', 10, 'bold'), anchor='w', justify='left', bg = 'lightgrey')
			answer_label.grid(column =1, row = 0, sticky ='w', padx = 10, pady = 5)

			
			quit = Button(new_Window, text = 'Quit', command = root.destroy, padx = 15, pady =6, bg = 'firebrick1', fg = 'white', font = ('ariel', 16, 'bold'))
			quit.grid(column = 0, row = 1, pady = 5,)





#class to define the components of the GUI
class generalQuiz:
	# This is the first method which is called when a
	# new object of the class is initialized. This method
	# sets the question count to 0. and initialize all the
	# other methoods to display the content and make all the
	# functionalities available
	def __init__(self):
		
		# set question number to 0
		self.q_no=0
		
		# Set the time limit for each question (in seconds)
		self.time_limit = 30

		# Set the start time to the current time
		self.start_time = time.time()
		
		# Create label for the timer
		self.timer_label = Label(root, text="", font=('ariel', 12), bg='red')

		# Display title
		self.display_title()

		# Have a new randomized order of questions every time they
		# quit and start the quiz again
		self.shuffle_questions_and_options()

		# assigns ques to the display_question function to update later.
		self.display_question()
		
		# option_selected holds an integer value which is used for
		# selected option in a question.
		self.option_selected=IntVar()
		
		# displaying radio button for the current question and used to
		# display options for the current question
		self.options=self.radio_buttons()
		
		# display options for the current question
		self.display_options()
		
		# displays the button for next and exit.
		self.buttons()
		
		# no of questions
		self.data_size=len(general_question)
		
		# keep a counter of correct answers
		self.correct=0

		
		# Schedule the update_timer method to start updating the timer
		root.after(1000, self.update_timer)
		

	# This method is used to Display Title
	def display_title(self):
		
		# The title to be shown
		title = Label(root, text="GENERAL QUIZ",
		width=75, bg="grey30",fg="white", font=("ariel", 20, "bold"))
		root.configure(bg = 'lightgrey')
		# place of the title
		title.place(x=0, y=2)

	
	# This method shuffles the questions order randomly every time users take the quiz
	def shuffle_questions_and_options(self):
		indices = random.sample(range(len(general_question)), len(general_question))

		general_question[:] = [general_question[i] for i in indices]
		general_answer_options[:] = [general_answer_options[i] for i in indices]
		general_answers[:] = [general_answers[i] for i in indices]


	# This method shows the current Question on the screen
	def display_question(self):
		
		question_no_label = Label(root, text = f'Question {self.q_no + 1}:', width = 40, bg = 'lightgrey', 
		font = ('ariel', 16, 'bold'), anchor= 'w')
		question_no_label.place(x = 70, y = 50)
		
		# setting the Question properties
		q_no = Label(root, text=general_question[self.q_no], width=100, bg = 'lightgrey',
		font=( 'ariel' , 16 , 'bold' ), anchor= 'w' )
		
		#placing the option on the screen
		q_no.place(x=70, y=100)



	# This method sets a timer for each question
	def update_timer(self):
		
		# Calculate the elapsed time
		elapsed_time = int(time.time() - self.start_time)

		# Calculate the remaining time
		self.remaining_time = max(0, self.time_limit - elapsed_time)

		# Update the timer label
		self.timer_label.config(text=f"Time Remaining: {self.remaining_time} seconds", font = ('ariel', 15, 'bold'), bg = 'lightgrey', fg= 'firebrick1')
		self.timer_label.place(x = 800, y = 50)

		# Check if time is up
		if self.remaining_time == 0:
			mb.showinfo('Time Up', 'You have run out of time for this question!')
			self.next_btn()  # Move to the next question
		

		self.timer_label.update()
		# Continue updating the timer every second
		root.after(1000, self.update_timer)

	

	# This method shows the radio buttons to select the Question
	# on the screen at the specified position. It also returns a
	# list of radio button which are later used to add the options to
	# them.
	def radio_buttons(self):
		
		# initialize the list with an empty list of options
		q_list = []
		
		# position of the first option
		y_pos = 150
		
		# adding the options to the list
		while len(q_list) < 4: 
			
			# setting the radio button properties
			radio_btn = Radiobutton(root,text=" ",variable=self.option_selected,
			value = len(q_list)+1,font = ("ariel",14), bg = 'lightgrey')
			
			# adding the button to the list
			q_list.append(radio_btn)
			
			# placing the button
			radio_btn.place(x = 100, y = y_pos)
			
			# incrementing the y-axis position by 40
			y_pos += 40
		
		# return the radio buttons
		return q_list
	

	# This method deselect the radio button on the screen
	# Then it is used to display the options available for the current
	# question which we obtain through the question number and Updates
	# each of the options for the current question of the radio button.
	def display_options(self):
		val=0
		
		# deselecting the options
		self.option_selected.set(0)
		
		# looping over the options to be displayed for the
		# text of the radio buttons.
		for option in general_answer_options[self.q_no]:
			self.options[val]['text']=option
			val+=1



	# This method checks the Answer after we click on Next.
	def check_answer(self, q_no):
		# checks for if the selected option is correct
		if self.option_selected.get() == general_answers[q_no]:
		# if the option is correct it return true
			return True
		
	

	# This method checks if users select their answer or not
	def check_option_selected(self):
		return not self.option_selected.get()

			



	# This method is used to check the answer of the
	# current question by calling the check_answer and question no.
	# if the question is correct it increases the count by 1
	# and then increase the question number by 1. If it is last
	# question then it calls display result to show the message box.
	# otherwise shows next question.
	def next_btn(self):
		
		# Check if the answer is correct or not and that the users did select their answers
		if self.check_answer(self.q_no) and not self.check_option_selected():
			mb.showinfo('', 'Your answer is correct')
			# if the answer is correct it increments the correct by 1
			self.correct += 1
		if not self.check_answer(self.q_no) and not self.check_option_selected():
			mb.showinfo('', 'Your answer is incorrect')



		# Check if users select their answer or not and the time is up or not after clicking the next button
		# if not, they will get an error pop up on the screen
		# if yes, they will move to the next question
		if self.check_option_selected() and self.remaining_time != 0:
			mb.showerror('Option not selected', 'Please select your answer!')

		# Check if the time is up and also if the user did not select their answer
		# if true, showinfor, and move to the next question
		if self.check_option_selected() and self.remaining_time == 0:
			mb.showinfo('', 'You did not select you answer!')
			self.q_no += 1 
			self.start_time = time.time()

		# If user did select their answer, they will be graded and moved to next question
		if not self.check_option_selected():
			self.q_no += 1
			self.start_time = time.time()
		
	

		# checks if the q_no size is equal to the data size
		if self.q_no == self.data_size:
			
			# if it is correct then it displays the score
			self.display_result()
			
			# destroys the GUI
			
		else:
			# shows the next question
			self.display_question()
			self.display_options()
	
	


	# This method shows the two buttons on the screen.
	# The first one is the next_button which moves to next question
	# It has properties like what text it shows the functionality,
	# size, color, and property of text displayed on button. Then it
	# mentions where to place the button on the screen. The second
	# button is the exit button which is used to close the GUI without
	# completing the quiz.
	def buttons(self):
		
		# The first button is the Next button to move to the
		# next Question
		next_btn = Button(root, text="Next Question",command=self.next_btn,
		width=15,bg="firebrick2",fg="white",font=("ariel",16,"bold"))
		
		# placing the button on the screen
		next_btn.place(x=480,y=380)
		
		# This is the second button which is used to Quit the GUI
		quit_btn = Button(root, text="Quit", command=root.destroy,
		width=5,bg="firebrick1", fg="white",font=("ariel",16," bold"))
		
		# placing the Quit button on the screen
		quit_btn.place(x=1100,y=50)


		view_correct_answer_btn = Button(root, text = 'View correct answers', width = 18, bg = 'firebrick', fg = 'white', font=("ariel",16," bold"), command = self.view_correct_general_btn)
		view_correct_answer_btn.place(x = 740, y = 380)


	# This method is used to display the result
	# It counts the number of correct and wrong answers
	# and then display them at the end as a message Box
	def display_result(self):
		
		# calculates the wrong count
		wrong_count = self.data_size - self.correct
		correct = f"Correct: {self.correct}"
		wrong = f"Wrong: {wrong_count}"
		
		# calcultaes the percentage of correct answers
		score = int(self.correct / self.data_size * 100)
		result = f"Score: {score}%"
		
		# Shows a message box to display the result
		mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

	
	# Check if users try to view answers when they did not complete their quiz yet
	def view_correct_general_btn(self):
		if self.q_no != self.data_size:
			mb.showinfo('Access denied', 'Please complete your quiz first!')
		elif self.correct == self.data_size:
			mb.showinfo('', 'You have it all correct!')
		else:
			new_Window = Toplevel(root)
			new_Window.title('View Correct Answers')
			new_Window.geometry('1100x500')
			new_Window.configure(bg = 'lightgrey')

			question_frame = LabelFrame(new_Window, text = 'Questions', width = 400, height = 300, padx = 10, bg = 'lightgrey')
			question_frame.grid(column = 0, row = 0, padx = 20, pady = 20)

			question_label = Label(question_frame, text = "1. Which country has the most population?\n2. Which country has the largest area?\n3. How many planets are in the solar system?\n4. Which planet is the closest to the Sun?\n5. How many continents are there in the world?\n6. Which country that had the sumurai?\n7. Which of these colors is not featured in the logo for Google?\n8. What is the chemical formula of water?\n9. What is the most abundant element in the Earth?\n10. What is the largest ocean in the world?\n11. What is the most widely spoken language in the world?\n12. Which is the world's largest rainforest?\n13. What is the tallest mountain in the world?\n14. What is the average time of a new child/childrens to born?\n15. What is the largest organ in human body?\n16. What is the largest mammal on Earth?\n17. Which planet is known as the 'Red Planet'?\n18. Who painted the Mona Lisa?\n19. Which month that contains normally 28 days, and 29 days every four years?\n20. Who wrote the famous tragedy 'Romeo and Juliet'?",
						font=('ariel', 12, 'bold'), anchor = 'w', justify='left', bg = 'lightgrey')
			question_label.grid(column = 0, row = 0, sticky = 'w', padx = 10, pady = 5)

			answer_frame = LabelFrame(new_Window, text = 'Answers', width=400, height = 300, padx = 10, bg = 'lightgrey')
			answer_frame.grid(column = 1, row = 0, padx = 20, pady = 20)

			answer_label = Label(answer_frame, text = '1. China\n2. Russia\n3. 8\n4. Venus\n5. 7\n6. Japan\n7.Pink\n8. H2O\n9. Nitrogen\n10. Pacific Ocean\n11. Mandarin Chinese\n12. Amazon rainforest\n13. Mount Everest\n14. 9 months and 10 days\n15. Skin\n16. Blue Whale\n17. Mars\n18. Leonardo da Vinci\n19. February\n20. William Shakespeare',
						font=('ariel', 12, 'bold'), anchor='w', justify='left', bg = 'lightgrey')
			answer_label.grid(column =1, row = 0, sticky ='w', padx = 10, pady = 5)

			quit = Button(new_Window, text = 'Quit', command = root.destroy, padx = 15, pady =6, bg = 'firebrick1', fg = 'white', font = ('ariel', 16, 'bold'))
			quit.grid(column = 0, row = 1, pady = 5,)


#class to define the components of the GUI
class historyQuiz:
	# This is the first method which is called when a
	# new object of the class is initialized. This method
	# sets the question count to 0. and initialize all the
	# other methoods to display the content and make all the
	# functionalities available
	def __init__(self):
		
		# set question number to 0
		self.q_no=0
		
		# Set the time limit for each question (in seconds)
		self.time_limit = 30

		# Set the start time to the current time
		self.start_time = time.time()
		
		# Create label for the timer
		self.timer_label = Label(root, text="", font=('ariel', 12), bg='red')

		# Display title
		self.display_title()

		# Have a new randomized order of questions every time they
		# quit and start the quiz again
		self.shuffle_questions_and_options()

		# assigns ques to the display_question function to update later.
		self.display_question()
		
		# option_selected holds an integer value which is used for
		# selected option in a question.
		self.option_selected=IntVar()
		
		# displaying radio button for the current question and used to
		# display options for the current question
		self.options=self.radio_buttons()
		
		# display options for the current question
		self.display_options()
		
		# displays the button for next and exit.
		self.buttons()
		
		# no of questions
		self.data_size=len(history_question)
		
		# keep a counter of correct answers
		self.correct=0

		
		# Schedule the update_timer method to start updating the timer
		root.after(1000, self.update_timer)
		

	# This method is used to Display Title
	def display_title(self):
		
		# The title to be shown
		title = Label(root, text="HISTORY QUIZ",
		width=75, bg="grey30",fg="white", font=("ariel", 20, "bold"))
		root.configure(bg = 'lightgrey')
		# place of the title
		title.place(x=0, y=2)

	# This method shuffles the questions order randomly every time users take the quiz
	def shuffle_questions_and_options(self):
		indices = random.sample(range(len(history_question)), len(history_question))

		history_question[:] = [history_question[i] for i in indices]
		history_answer_options[:] = [history_answer_options[i] for i in indices]
		history_answers[:] = [history_answers[i] for i in indices]


	# This method shows the current Question on the screen
	def display_question(self):
		
		question_no_label = Label(root, text = f'Question {self.q_no + 1}:', width = 40, bg = 'lightgrey', 
		font = ('ariel', 16, 'bold'), anchor= 'w')
		question_no_label.place(x = 70, y = 50)
		
		# setting the Question properties
		q_no = Label(root, text=history_question[self.q_no], width=100, bg = 'lightgrey',
		font=( 'ariel' , 16 , 'bold' ), anchor= 'w' )
		
		#placing the option on the screen
		q_no.place(x=70, y=100)



	# This method sets a timer for each question
	def update_timer(self):
		
		# Calculate the elapsed time
		elapsed_time = int(time.time() - self.start_time)

		# Calculate the remaining time
		self.remaining_time = max(0, self.time_limit - elapsed_time)

		# Update the timer label
		self.timer_label.config(text=f"Time Remaining: {self.remaining_time} seconds", font = ('ariel', 15, 'bold'), bg = 'lightgrey', fg= 'firebrick1')
		self.timer_label.place(x = 800, y = 50)

		# Check if time is up
		if self.remaining_time == 0:
			mb.showinfo('Time Up', 'You have run out of time for this question!')
			self.next_btn()  # Move to the next question
		

		self.timer_label.update()
		# Continue updating the timer every second
		root.after(1000, self.update_timer)

	

	# This method shows the radio buttons to select the Question
	# on the screen at the specified position. It also returns a
	# list of radio button which are later used to add the options to
	# them.
	def radio_buttons(self):
		
		# initialize the list with an empty list of options
		q_list = []
		
		# position of the first option
		y_pos = 150
		
		# adding the options to the list
		while len(q_list) < 4: 
			
			# setting the radio button properties
			radio_btn = Radiobutton(root,text=" ",variable=self.option_selected,
			value = len(q_list)+1,font = ("ariel",14), bg = 'lightgrey')
			
			# adding the button to the list
			q_list.append(radio_btn)
			
			# placing the button
			radio_btn.place(x = 100, y = y_pos)
			
			# incrementing the y-axis position by 40
			y_pos += 40
		
		# return the radio buttons
		return q_list
	

	# This method deselect the radio button on the screen
	# Then it is used to display the options available for the current
	# question which we obtain through the question number and Updates
	# each of the options for the current question of the radio button.
	def display_options(self):
		val=0
		
		# deselecting the options
		self.option_selected.set(0)
		
		# looping over the options to be displayed for the
		# text of the radio buttons.
		for option in history_answer_options[self.q_no]:
			self.options[val]['text']=option
			val+=1



	# This method checks the Answer after we click on Next.
	def check_answer(self, q_no):
		
		# checks for if the selected option is correct
		if self.option_selected.get() == history_answers[q_no]:
		# if the option is correct it return true
			return True
		
	

	# This method checks if users select their answer or not
	def check_option_selected(self):
		return not self.option_selected.get()

			



	# This method is used to check the answer of the
	# current question by calling the check_answer and question no.
	# if the question is correct it increases the count by 1
	# and then increase the question number by 1. If it is last
	# question then it calls display result to show the message box.
	# otherwise shows next question.
	def next_btn(self):
		
		# Check if the answer is correct or not and that the users did select their answers
		if self.check_answer(self.q_no) and not self.check_option_selected():
			mb.showinfo('', 'Your answer is correct')
			# if the answer is correct it increments the correct by 1
			self.correct += 1
		if not self.check_answer(self.q_no) and not self.check_option_selected():
			mb.showinfo('', 'Your answer is incorrect')



		# Check if users select their answer or not and the time is up or not after clicking the next button
		# if not, they will get an error pop up on the screen
		# if yes, they will move to the next question
		if self.check_option_selected() and self.remaining_time != 0:
			mb.showerror('Option not selected', 'Please select your answer!')

		# Check if the time is up and also if the user did not select their answer
		# if true, showinfor, and move to the next question
		if self.check_option_selected() and self.remaining_time == 0:
			mb.showinfo('', 'You did not select you answer!')
			self.q_no += 1 
			self.start_time = time.time()

		# If user did select their answer, they will be graded and moved to next question
		if not self.check_option_selected():
			self.q_no += 1
			self.start_time = time.time()
		
	

		# checks if the q_no size is equal to the data size
		if self.q_no == self.data_size:
			
			# if it is correct then it displays the score
			self.display_result()
			
			# destroys the GUI
			
		else:
			# shows the next question
			self.display_question()
			self.display_options()
	



	# This method shows the two buttons on the screen.
	# The first one is the next_button which moves to next question
	# It has properties like what text it shows the functionality,
	# size, color, and property of text displayed on button. Then it
	# mentions where to place the button on the screen. The second
	# button is the exit button which is used to close the GUI without
	# completing the quiz.
	def buttons(self):
		
		# The first button is the Next button to move to the
		# next Question
		next_btn = Button(root, text="Next Question",command=self.next_btn,
		width=15,bg="firebrick2",fg="white",font=("ariel",16,"bold"))
		
		# placing the button on the screen
		next_btn.place(x=480,y=380)
		
		# This is the second button which is used to Quit the GUI
		quit_btn = Button(root, text="Quit", command=root.destroy,
		width=5,bg="firebrick1", fg="white",font=("ariel",16," bold"))
		
		# placing the Quit button on the screen
		quit_btn.place(x=1100,y=50)


		view_correct_answer_btn = Button(root, text = 'View correct answers', width = 18, bg = 'firebrick', fg = 'white', font=("ariel",16," bold"), command = self.view_correct_general_btn)
		view_correct_answer_btn.place(x = 740, y = 380)


	# This method is used to display the result
	# It counts the number of correct and wrong answers
	# and then display them at the end as a message Box
	def display_result(self):
		
		# calculates the wrong count
		wrong_count = self.data_size - self.correct
		correct = f"Correct: {self.correct}"
		wrong = f"Wrong: {wrong_count}"
		
		# calcultaes the percentage of correct answers
		score = int(self.correct / self.data_size * 100)
		result = f"Score: {score}%"
		
		# Shows a message box to display the result
		mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

	# Check if users try to view answers when they did not complete their quiz yet
	def view_correct_general_btn(self):
		if self.q_no != self.data_size:
			mb.showinfo('Access denied', 'Please complete your quiz first!')
		elif self.correct == self.data_size:
			mb.showinfo('', 'You have it all correct!')
		else:
			new_Window = Toplevel(root)
			new_Window.title('View Correct Answers')
			new_Window.geometry('1400x500')
			new_Window.configure(bg = 'lightgrey')

			question_frame = LabelFrame(new_Window, text = 'Questions', width = 400, height = 300, padx = 10, bg = 'lightgrey')
			question_frame.grid(column = 0, row = 0, padx = 20, pady = 20)

			question_label = Label(question_frame, text = "1. When was the world war I started and ended?\n2. When was the world war II started and ended?\n3. Who was the leader of the Khmer Rouge during the Cambodian Genocide?\n4. The ancient temple complex Angkor Wat is located in which Cambodian city?\n5. Which period of Cambodia that is considered to have the most influence?\n6. What is the independence day of Cambodia?\n7. How many years has Cambodia been colonized by France?\n8. What is strongest reason why Cambodia periods collapsed?\n9. Which event marked the beginning of the World War I?\n10. Which ancient civilization built the pyramids of Giza?\n11. Which year did the Titanic sink?\n12. Which ancient temple complex is a symbol of Cambodia and appears on the national flag?\n13. What significant event in Cambodian history occurred on April 17, 1975?\n14. Who was the first president of the United States?\n15. Who was the leader of the Soviet Union during World War II?\n16. In which year did the Berlin Wall fall, leading to the reunification of Germany?\n17. When did Cambodia join ASEAN?\n18. How many countries are there in ASEAN?\n19. Which Khmer king is known for converting the empire to Mahayana Buddhism and building the Bayon temple?\n20. Who was the founder of the Khmer Empire and the city of Angkor?",
						  font =('ariel', 12, 'bold'), anchor = 'w', justify='left', bg = 'lightgrey')
			question_label.grid(column = 0, row = 0, sticky = 'w', padx = 10, pady = 5)

			answer_frame = LabelFrame(new_Window, text = 'Answers', width=400, height = 300, padx = 10, bg = 'lightgrey')
			answer_frame.grid(column = 1, row = 0, padx = 20, pady = 20)

			answer_label = Label(answer_frame, text = '1. 1914-1918\n2. 1939-1945\n3. Pol Pot\n4. Siem Reap\n5. Angkor period\n6. 9 November 1953\n7. 90 years\n8. Civil war\n9. Assassination of Archduke Franz Ferdinand\n10. Ancient Egypt\n11. 1912\n12. Angkor Wat\n13. Fall of Phnom Penh to the Khmer Rouge\n14. George Washington\n15. Joseph Stalin\n16. 1989\n17. 30 April 1999\n18. 10\n19. Jayavarman VII\n20. Jayavarman II',
						font =('ariel', 12, 'bold'), anchor = 'w', justify='left', bg = 'lightgrey')
			answer_label.grid(column =1, row = 0, sticky ='w', padx = 10, pady = 5)

			quit = Button(new_Window, text = 'Quit', command = root.destroy, padx = 15, pady =6, bg = 'firebrick1', fg = 'white', font = ('ariel', 16, 'bold'))
			quit.grid(column = 0, row = 1, pady = 5,)


# Create a GUI Window
root = Tk()

# set the size of the GUI Window
root.geometry("1250x500")

# set the title of the Window
root.title("Quiz")

# get the data from the json file
with open('data.json') as f:
	data = json.load(f)

# set the question, options, and answer for math quiz
math_question = (data['math_questions'])
math_answer_options = (data['math_answer_options'])
math_answers = (data[ 'math_answers'])


# set the question, options, and answer for general quiz
general_question = (data['general_questions'])
general_answer_options = (data['general_answer_options'])
general_answers = (data['general_answers'])



history_question = (data['history_questions'])
history_answer_options = (data['history_asnwer_options'])
history_answers = (data['history_answers'])




# Create home page
frame1 = Frame()
def homepage():
	frame1.configure(bg = 'lightgrey')
	greeting_label = Label(frame1, text = 'What type of quiz would you like to give it a try?', font = ('Ariel', 12,'bold'), bg = 'lightgrey')
	greeting_label.pack()
	math_btn = Button(frame1, text = 'Math Quiz', bg = 'lightgrey', command = math_selected, padx = 10, pady =5, font = ('Ariel', 11,'bold'), cursor= 'tcross')
	general_btn = Button(frame1, text = 'General Quiz', bg = 'lightgrey', command = general_selected,  padx = 10, pady =5, font = ('Ariel', 11,'bold'), cursor= 'tcross')
	history_btn = Button(frame1, text = 'History Quiz', bg = 'lightgrey', command = history_selected,  padx = 10, pady =5, font = ('Ariel', 11,'bold'), cursor= 'tcross')
	introduction_label1 = Label(frame1, text =  '*Note* Each quiz contains 20 questions and has a timer each question.', font = ('Ariel', 13,'bold'), bg = 'lightgrey', fg = 'firebrick3')
	introduction_label2 = Label(frame1, text = "The math quiz has a time of 45 seconds, and the other two have 30 seconds. Click the button to start the quiz.", font = ('Ariel', 13,'bold'), bg = 'lightgrey', fg = 'firebrick3')
	math_btn.pack(pady= 5)
	general_btn.pack(pady= 5)
	history_btn.pack(pady= 5)
	introduction_label1.pack()
	introduction_label2.pack()


#If user want to do math quiz
#Create an object for the class mathQuiz
def math_selected():
	frame1.pack_forget()
	math = mathQuiz()


#If user want to do general quiz
#Create an object for the class generalQuiz
def general_selected():
	frame1.pack_forget()
	general = generalQuiz()


#If user want to do general quiz
#Create an object for the class historyQuiz
def history_selected():
	frame1.pack_forget()
	history = historyQuiz()

	


#display the content inside the frame
frame1.pack(expand = True, fill= 'both')

# Display the homepage first
homepage()
# Start the GUI
root.mainloop()

# END OF THE PROGRAM