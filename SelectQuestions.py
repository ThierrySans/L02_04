# MCQ - multiple choice
# FIB - fill in blanks
# The assignment creates one for each student

try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk
    
import random
import io
import csv

from randomalgo import *

class SelectQuestions(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.label = tk.Label(self, text="WELCOME!!\nPlease choose questions \
to appear on an assignment (without spaces)\n", font=("Helvetica", 32))
        self.label.pack()

        self.display_button = tk.Button(self, text="Display Questions", \
                                        command=self.display)
        self.display_button.pack()

        self.submit_button = tk.Button(self, text="Submit", \
                                       command=self.create_window)

        self.entry = tk.Entry(self)
        
        self.assignmentEntry = None
        
        self.assignmentWindow = None
        
        # This will be the list of actual questions chosen
        self.chosenQuestions = []
        
        #self.questionEntries = []
        
        self.assignmentAnswerEntry = None

    def display(self):
        # Read all the questions in questions.csv and display them on the
        # screen
        with open("questions.csv", "r") as csvFile:
            reader = csv.reader(csvFile, delimiter="\n")
            for row in reader:
                splitRow = row[0].split(',')
                self.singleQuestion = tk.Label(self, text=splitRow[0] + ":" + \
                                               splitRow[3],\
                                               font=("Helvetica", 28))
                self.singleQuestion.pack()
                
            self.submit_button.pack()
    
            self.entry.pack()
            
            self.display_button.config(state = 'disabled')

    def create_window(self):
        # FIX: WHEN QUESTIONS SPAN MORE THAN THE SCREEN, UNABLE TO SCROLL DOWN
        # Create a new window for the assignment
        self.assignmentWindow = tk.Toplevel(self)
        root.withdraw()
        self.assignmentWindow.wm_title("ASSIGNMENT")
        
        # Get the user input
        chosenQuestionNums = self.entry.get()
        questionNumChosen = chosenQuestionNums.split(',')
        
        # Get the chosen questions and append to the list self.chosenQuestions
        with open("questions.csv", "r") as csvFile:
            for lineList in csv.reader(csvFile):
                self.chosenQuestions.append(lineList)
        
        # Make an assignment and store it inside Assignment.csv (using the
        # function in randomalgo.py)
        makeAssignment(self.chosenQuestions)
        
        # Read from Assignment.csv and display the questions to the window
        with open('Assignment.csv', 'r') as assignmentFile:
            for question in csv.reader(assignmentFile):
                questionEntry = tk.Label(self.assignmentWindow, text=question[2],\
                         font=("Helvetica", 28))
                questionEntry.pack()
                
                #self.questionEntries.append(questionEntry)
                
                #tk.Entry(assignmentWindow).pack()
                
        tk.Button(self.assignmentWindow, text="Hand in", font=("Helvetica", 28),\
                  command=self.validate).pack()
        
        self.assignmentAnswersEntry = tk.Entry(self.assignmentWindow, \
                                              font=("Helvetica", 28))
        self.assignmentAnswersEntry.pack()

    def validate(self):
        # I AM ASSUMING THAT STUDENTS WILL ANSWER EVERY QUESTION
        assignmentAnswers = self.assignmentAnswersEntry.get()
        #assignmentAnswersList = assignmentAnswers.split(',')
        assignmentAnswersList = [x.strip() for x in \
                                 assignmentAnswers.split(',')]
        
        with open('Assignment.csv', 'r') as assignmentFile:
            for question in csv.reader(assignmentFile):
                if question[3] in assignmentAnswersList:
                    tk.Label(self.assignmentWindow, text="Correct").pack()
                else:
                    tk.Label(self.assignmentWindow, text="Wrong").pack()
        # For every student answer in assignmentAnswersList, compare them with
        # the answers

root = tk.Tk()
root.geometry('%sx%s' % (2000, 2000))
main = SelectQuestions(root)
main.pack(side="top", fill="both", expand=True)
root.mainloop()

'''
self.question = tk.Label(assignmentWindow, text=\
                         self.questionNumPair.get(key),\
                         font=("Helvetica", 28))
self.question.pack()
'''

'''
if row[0].strip() in questionNumChosen:
    self.chosenQuestions.append(row[0])
'''
'''
for row in reader:
    for num in questionNumChosen:
        if num.strip() in row[0]:
            self.chosenQuestions.append(row[0])
'''
        #reader = csv.reader(csvFile, delimiter="\n")

    # For every element in self.chosenQuestions, split it by comma
    #for csvInfo in self.chosenQuestions:
        #csvInfo.replace('"', '')
        
        #indivList = csvInfo.split(',')
        
        # Add the element at index 5 with the one at index 4
        #indivList[4] = indivList[4] + ', ' + indivList[5]
        
        # Delete the 5th element
        #del indivList[5]
        
        #self.passList.append(indivList)