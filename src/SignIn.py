from tkinter import *
import tkinter.messagebox
from Student import *
from Professor import *
import StudentProfileIndex
import ProfessorProfileIndex
import csv
import io
import os

## Parent Class for all users

def readUser():
    return readUserFile("Users.csv")

def readUserFile(filename):
    csv_file = open("Users.csv", "r")

    Users = []

    lines = list(csv.reader(csv_file)) # Represents file as List of Lists, first list is of rows, deeper list is of row contents.

    for l in lines:

        # Could make the user and email pair now, instead of doing it when making the object...

        if l[5] == "P":
            Users.append(Professor(l[1], l[2], l[3], l[4]))
        elif l[5] == "S":
            Users.append(Student(l[1], l[2], l[3], l[4]))

    csv_file.close()
    # Should set it so it returns 0 if the file isn't there, then report that to the user.

    return Users

## Remember, Python or Tkinter or whatever doesn't check if these frames exist. these functions, when called by a buttonpress, act as if they're in the same scope as the button, or something.

def StudentRegistering(event):
    """ Execute the registration menu """

    newWindow = Toplevel()
    StudentProfileIndex.signUpIndex(newWindow)

def ProfessorRegistering(event):
    """ Execute the registration menu """ 

    newWindow = Toplevel()
    ProfessorProfileIndex.signUpIndex(newWindow)

def SignIn(event):

    # Need to declare globals locally, if modifying them, from inside a function?

    global CurrentUsr
    global Usrs

    Usrs = readUser()

    Em = EmailEntry.get()

    Pass = PassEntry.get()

    # Check if either name or email exist separately. Bad for security? Maybe not.
    EmEx = False
    PassEx = False

    for Usr in Usrs:

        if CurrentUsr is None:

            #If we have no idea who the correct user could be...
            if (Usr.getEmail() == Em):
                EmEx = True
                CurrentUsr = Usr

            if (Usr.getPassword() == Pass):
                PassEx = True
                CurrentUsr = Usr

        if not (CurrentUsr is None):

            if (Usr.getEmail() == Em):
                EmEx = True

            if (Usr.getPassword() == Pass):
                PassEx = True

            if (EmEx & PassEx):
                tkinter.messagebox.showinfo('Logged In', ('You are now logged in,' + " " + Usr.getName() + "."))
                goToTransitionScreen(Usr)
                break

    if not (EmEx and PassEx):
        tkinter.messagebox.showinfo('Invalid Credentials', "Invalid Credentials")

def goToTransitionScreen(user):
    newWindow = Toplevel()
    newWindow.attributes('-topmost', 'true')
    Button(newWindow, text="Display Assignment", command=lambda:callDisplayAllAssignments(newWindow, user)).pack()

    if (user.getType() == 'S'):
        studInfoBut = Button(newWindow, text="My Info", command=lambda:StudentProfileIndex.displayProfile(newWindow, user, studInfoBut))
        studInfoBut.pack()
    elif (user.getType() == 'P'):
        profInfoBut = Button(newWindow, text="My Info", command=lambda:ProfessorProfileIndex.displayProfile(newWindow, user, profInfoBut))
        profInfoBut.pack()
        addQuestionFormsBtn = Button(newWindow, text="Add a question formula", command=lambda:callAddQuestionFormulas(newWindow))
        addQuestionFormsBtn.pack()

def callDisplayAllAssignments(newWindow, user):
    newWindow.destroy()
    if (user.getType() == 'S'):
        os.system('python3 DisplayAllAssignments.py')
    elif (user.getType() == 'P'):
        os.system('python3 DisplayProfessorsAssignments.py')

def callAddQuestionFormulas(newWindow):
    newWindow.destroy()
    os.system('python3 user_story_3.py')

#### Okay... So bound functions can't take parameters...

root = Tk()
root.title("Sign In Page")

CredFrame = Frame(root)
CredFrame.pack()

EmailText = StringVar()
PassText = StringVar()

EmailLabel = Label(CredFrame, text="Email")
PassLabel = Label(CredFrame, text="Password")

EmailEntry = Entry(CredFrame, textvariable=EmailText)
PassEntry = Entry(CredFrame, show="*", textvariable=PassText)

# widgets centered by default, sticky option to change
EmailLabel.grid(row=1, sticky=E)
PassLabel.grid(row=2, sticky=E)

EmailEntry.grid(row=1, column=1)
PassEntry.grid(row=2, column=1)

checked = 0

c = Checkbutton(CredFrame, text="Keep me logged in", variable=checked)
c.grid(columnspan=2)

BottomFrame = Frame(root)
BottomFrame.pack(side=BOTTOM)

ButtonFrame = Frame(BottomFrame)
ButtonFrame.pack(side=BOTTOM)

if checked: print("hi!") #Do stuff

global Usrs

Usrs = readUser()

global CurrentUsr

CurrentUsr = None

RegisterButton = Button(ButtonFrame, text="Student Registration")
RegisterButton.pack(side=LEFT)
RegisterButton.bind("<Button-1>", StudentRegistering)

RegisterButton = Button(ButtonFrame, text="Professor Registration")
RegisterButton.pack(side=LEFT)
RegisterButton.bind("<Button-1>", ProfessorRegistering)

SignInButton = Button(ButtonFrame, text="Sign In")
SignInButton.bind("<Button-1>", SignIn)

if Usrs is not None:
    SignInButton.pack(side=RIGHT)

if __name__ == '__main__':
    
    root.mainloop()

### You can also put the form code inside the def function to make a form pop up when you click that button...:
