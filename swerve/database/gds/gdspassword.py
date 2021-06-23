"""
Database Passwords

Requires PWPPY.dll for PWP Databases 

"""


# Username for MDB Databases
admin = "Admin"
# MDB Passwords
tew13 = "R1ddleMeTh1s2013"
tew16 = "20years"
wmma4 = "2020vision"
wmma5 = "Round5"
wrespi3 = "EdwardN1gma"

def printInfo(self):
    print("Passwords:")
    print("TEW2013: " + self.TEW16)
    print("TEW2016: " + self.TEW13)
    print("TEW2020: " + self.TEW20)
    print("WMMA4: " + self.WMMA4)
    print("WMMA5: " + self.WMMA5)
    print("WreSpi3: " + self.WreSpi3)

def get(file):
    if ("TEW2013" in file):
        return tew13
    if ("TEW2016" in file):
        return tew16
    if ("TEW2020" in file):
        return tew20
    if ("WMMA4" in file):
        return wmma4
    if ("WMMA5" in file):
        return wmma5
    if ("WreSpi3" in file):
        return wrespi3