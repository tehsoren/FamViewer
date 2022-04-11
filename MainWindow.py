from PyQt5 import QtWidgets, uic
import sys
import GedcomParser

class MainWindow(QtWidgets.QMainWindow):


    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi("pyqt.ui",self)
        self.SetupUIConnections()
        self.show()

    def SetupUIConnections(self):
        self.listWidgetPeople.itemSelectionChanged.connect(self.NewPersonSelected)
        self.LoadFile.clicked.connect(self.LoadFileFunc)
        self.PersonDataFamilies.itemSelectionChanged.connect(self.NewFamilySelected)

    def LoadFileFunc(self):
        file_path,_ = QtWidgets.QFileDialog.getOpenFileName(self,"Open file")
        self.file_path = file_path
        self.FillPersonList()

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

        self.FillPersonData(person)
        self.FillPersonFamilyData(person)

    def FillPersonData(self,person):
        self.firstNameLabel.setText(person["first"])
        self.lastNameLabel.setText(" ".join(person["last"]))

    def FillPersonFamilyData(self,person):
        self.PersonDataFamilies.clear()
        self.PersonDataFamily.clear()
        self.PersonFamilyKeys = list(person["families"])
        self.PersonDataFamilies.addItems([i for i in person["families"]])

    def NewFamilySelected(self):
        self.PersonDataFamily.clear()
        familyIndex = self.PersonDataFamilies.currentRow()
        fam = self.familiesData[self.PersonFamilyKeys[familyIndex]]

        peopleInFam = fam["parent"]+fam["children"]
        self.PersonDataFamily.addItems([self.GetPersonName(i) for i in peopleInFam])

