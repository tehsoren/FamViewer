from gedcom.parser import Parser
from gedcom.element.individual import IndividualElement
from gedcom.element.family import FamilyElement
from gedcom.element.element import Element


def LoadData(file_path):
    parser = Parser()
    parser.parse_file(file_path,False)
    
    people = FindPeople(parser)
    
    return people
    
def FindPeople(parser):
    people = {}
    for ele in parser.get_root_child_elements():
        if isinstance(ele, IndividualElement):#is it a person element
            people[ele.get_pointer()] = ParsePerson(ele)
    return people

def FindFamilies(parser):
    families = {}
    for ele in parser.get_root_child_elements():
        if isinstance(ele, FamilyElement):#is it a family element
            families[ele.get_pointer()] = ParseFamily(ele)
    return families

def ParseFamily(family):
    familyData = {}
    children = []
    parents = []
    familyData["id"] = family.get_pointer()
    for e in family.get_child_elements():
        tag = e.get_tag()
        if tag == "CHIL": 
            children.append(e.get_value())
        elif tag == "HUSB" or tag == "WIFE":
            parents.append(e.get_value())
    familyData["children"] = children
    familyData["parent"] = parents
    return familyData
    
def ParsePerson(person):
    personData = {}
    name = person.get_name()
    personData["id"] = person.get_pointer()
    personData["first"] = name[0]
    personData["last"] = name[1:]
    personData["families"] = []
    return personData

def FillPeopleWithFamilies(people,families):
    for f in families.values():
        for p in f["parent"]:
            people[p]["families"] += [f["id"]]
        for p in f["children"]:
            people[p]["families"] += [f["id"]]
    return people, families

def GetPeopleAndFamilies(file_path):
    parser = Parser()
    parser.parse_file(file_path,False)
    tempP = FindPeople(parser)
    tempF = FindFamilies(parser)
    people,families = FillPeopleWithFamilies(tempP, tempF)
    
    return people,families