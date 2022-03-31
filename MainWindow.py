from PyQt5 import QtWidgets, uic
import sys
import GedcomParser

class MainWindow(QtWidgets.QMainWindow):


    def __init__(self, file_path):
        super(MainWindow,self).__init__()
        uic.loadUi("pyqt.ui",self)
        self.listWidgetPeople.itemSelectionChanged.connect(self.NewPersonSelected)
        self.file_path = file_path
        self.FillPersonList()
        self.show()

    def FillPersonList(self):
        
        people,families = GedcomParser.GetPeopleAndFamilies(self.file_path)
        self.peopleData = people
        self.familiesData = families
        self.peopleKeys = list(people.keys())
        self.listWidgetPeople.addItems([self.GetPersonName(i) for i in self.peopleKeys])

    def GetPersonName(self,index):
        return self.peopleData[index]["first"] + " "+" ".join(self.peopleData[index]["last"])

    def NewPersonSelected(self):
        index = self.listWidgetPeople.currentRow()
        person = self.peopleData[self.peopleKeys[index]]
        self.firstNameLabel.setText(person["first"])
        self.lastNameLabel.setText(" ".join(person["last"]))
        
        self.listWidgetParents.clear()