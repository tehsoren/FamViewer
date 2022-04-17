from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import uic
import sys
import GedcomParser
from FamTreeViewWindow import FamTreeViewerWindow

class MainWindow(QMainWindow):


    def __init__(self,file_path=None):
        super(MainWindow,self).__init__()
        uic.loadUi("pyqt.ui",self)
        self.SetupUIConnections()
        self.show()
        if(not file_path == None):
            self.file_path = file_path
            self.FillPersonList()

    def SetupUIConnections(self):
        #buttons
        self.LoadFile.clicked.connect(self.LoadFileFunc)
        self.ShowTreeWindowButton.clicked.connect(self.OpenFamilyTreeWindow)
        #Data 
        self.listWidgetPeople.itemSelectionChanged.connect(self.NewPersonSelected)
        self.PersonDataFamilies.itemSelectionChanged.connect(self.NewFamilySelected)

    def LoadFileFunc(self):
        file_path,_ = QFileDialog.getOpenFileName(self,"Open file")
        self.file_path = file_path
        self.FillPersonList()

    def OpenFamilyTreeWindow(self):
        self.familyWindow = FamTreeViewerWindow()
        self.familyWindow.show()

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

