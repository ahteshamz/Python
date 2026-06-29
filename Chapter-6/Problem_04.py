#Write a class train which a method to book tickets, get status(number of berts) and get fare info of train running under Indian Railways.

from random import randint
class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no.: {self.trainNo} from{fro} to {to}")

    def getStatus(self):
         print(f"Train no.: {self.trainNo} is running on time")


    def getfare(self,fro, to):
        print(f"Ticket fare in train no.: {self.trainNo} from {fro} to {to} is {randint(220,5050)}")

t = Train(12565)
t.book = ("Hajipur", "New Delhi")
t.getStatus()
t.getfare("Hajipur", "New Delhi")
