class Contact:
    def __init__(self, RID, SN, GN, PEM, WEM, PPN, WPN, SA, CITY, STP, CTY, PC):
        self.RID = RID
        self.SN = SN
        self.GN = GN
        self.PEM = PEM
        self.WEM = WEM
        self.PPN = PPN
        self.WPN = WPN
        self.SA = SA
        self.CITY = CITY
        self.STP = STP
        self.CTY = CTY
        self.PC = PC
    
    def __str__(self):
        finalString = ""
        if self.RID != "":
            finalString += self.RID + " "
        if self.SN != "":
            finalString += "SN=" + self.SN + " "
        if self.GN != "":
            finalString += "GN=" + self.GN + " "
        if self.PEM != "":
            finalString += "PEM=" + self.PEM + " "
        if self.WEM != "":
            finalString += "WEM=" + self.WEM + " "
        if self.PPN != "":
            finalString += "PPN=" + self.PPN + " "
        if self.WPN != "":
            finalString += "WPN=" + self.WPN + " "
        if self.SA != "":
            finalString += "SA=" + self.SA + " "
        if self.CITY != "":
            finalString += "CITY=" + self.CITY + " "
        if self.STP != "":
            finalString += "STP=" + self.STP + " "
        if self.CTY != "":
            finalString += "CTY=" + self.CTY + " "
        if self.PC != "":
            finalString += "PC=" + self.PC
        return finalString