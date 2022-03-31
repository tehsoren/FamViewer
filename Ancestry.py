class Ancestry():
    def __init__(self,people,families):
        self.people = people
        self.families = families
        self.peopleIds = list(people.keys())
        self.familyIds = list(families.keys()) 
    def GetPerson(self,index):
        id = self.peopleIds[index]
        return self.people[id]
    def GetFamily(self,index):
        id = self.familyIds[index]
        return self.families[id]
    def GetAllPeople(self):
        return [self.people[k] for k in self.peopleIds]
    def GetAllFamilies(self):
        return [self.families[k] for k in self.familyIds]
    def GetCloseFamily(self,index):
        siblings = []
        parents = []
        children = []
        spouses = []
        person = self.GetPerson(index)
        
        
        
        
        
        