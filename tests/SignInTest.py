import sys, inspect, os, csv
import unittest

 # script directory

sys.path.append("../src")

import SignIn, Professor, Student

## You just got your read to test. WriteUserFile has been obsoleted by the ProfileIndex-s' functions. I forgot that.

class TestSignIn(unittest.TestCase):

  def test_readUserFile(self):

  # How am I gonna test this without doing what the function is already doing?
  # ... Well, it's only noteworthy if it fails, so this is just a test that it hasn't changed...

    csv_file = open("TestUsers.csv", "w")
    csv_file.write("0,s,s,s,s,S\n")
    csv_file.write("1,p,p,p,p,P\n")
    csv_file.close()

    Users = [Student.Student("s", "s", "s", "s"), Professor.Professor("p", "p", "p", "p")]

    U = SignIn.readUserFile("TestUsers.csv")

    s = set()

    for i in range(len(U)):
      s.add(U[i].getName() == Users[i].getName())
      s.add(U[i].getEmail() == Users[i].getEmail())
      s.add(U[i].getPassword() == Users[i].getPassword())
      s.add(U[i].getPersonnelNumber() == Users[i].getPersonnelNumber())
      s.add(U[i].getType() == Users[i].getType())
      s.add(U[i].getId() == Users[i].getId())

    self.assertTrue(len(s) == 1)

if __name__ == '__main__':
    unittest.main(exit=False)
