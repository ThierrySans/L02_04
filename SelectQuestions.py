# MCQ - multiple choice
# FIB - fill in blanks
# Creates one assignment for each student

try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk

class SelectQuestions(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.label = tk.Label(self, text="WELCOME!!\nPlease choose questions \
to appear on an assignment\n", font=("Helvetica", 32))
        self.label.pack()

        self.display_button = tk.Button(self, text="Display Questions", \
                                        command=self.display)
        self.display_button.pack()

        self.submit_button = tk.Button(self, text="Submit", \
                                       command=self.create_window)
        
        self.entry = tk.Entry(self)
        
        self.assignmentEntry = None
        
        # For the chosen questions, put the question and the answer formula
        # as key-value pairs
        self.chosenquestions_answers_dict = {}

    def display(self):
        # Display every question below and have a checkbox beside everyone
        # of them
        with open('questions.txt', 'r') as f:
            # read the file and then split them by newline character
            self.questions = f.read()
            self.allQuestions = self.questions.split('\n')
            
            tk.Label(self, text="Please enter the question numbers in the\
format of question number #1, question number #2, question number #3\n", \
                           font=("Helvetica", 28)).pack()

            # add every question to the GUI
            for i in range(len(self.allQuestions)):
                # display the question
                self.singleQuestion = tk.Label(self, text="question " + str(i)\
                                               + ":" + self.allQuestions[i].\
                                               split('|||')[0].split(':')[1],
                                               font=("Helvetica", 28))
                self.singleQuestion.pack()
        self.submit_button.pack()
        self.entry.pack()

    def create_window(self):
        # Create a new window for the assignment
        assignmentWindow = tk.Toplevel(self)
        root.withdraw()
        assignmentWindow.wm_title("ASSIGNMENT")

        # Get the list of question numbers the user chose and search in the 
        # text file
        chosenQuestionNums = self.entry.get().split(',')

        # Read all the questions in questions.txt and split them into a list
        with open('questions.txt', 'r') as f:
            self.questions = f.read()
            self.allQuestions = self.questions.split('\n')
            
            instructions = tk.Label(assignmentWindow, text="Please answer the \
following questions to the best of your abilities\n\n", font=("Helvetica", 28))
            instructions.pack()
            
            # If any chosen question numbers appear in the list, add the label
            # to the new screen
            for questionNum in range(len(self.allQuestions)):
                if str(questionNum) in chosenQuestionNums:
                    self.question = tk.Label\
                        (assignmentWindow,text=self.allQuestions[questionNum]\
                         .split('|||')[0].split(':')[1], font=("Helvetica", 28))
                    self.question.pack()
                    self.assignmentEntry = tk.Entry(assignmentWindow)
                    self.assignmentEntry.pack()
                    tk.Label(assignmentWindow, text="\n").pack()
            assignmentWindow.geometry("%dx%d" % (2000, 2000))
            
            assignment_submit_button = tk.Button(assignmentWindow,\
                                                 text = "Submit",\
                                                 command=self.validate)
            assignment_submit_button.pack()
            
        tk.Button(assignmentWindow, text="Exit",\
                  command=assignmentWindow.destroy).pack()
            
    def validate(self):
        # Reocrd the student answers
        # Compare them with the actual answers (put values into the answer
        # formula)
        # Display a CORRECT label if they match. INCORRECT otherwise
        pass

root = tk.Tk()
root.geometry('%sx%s' % (2000, 2000))
main = SelectQuestions(root)
main.pack(side="top", fill="both", expand=True)
root.mainloop()