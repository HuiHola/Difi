class manu:
    def __init__(self):
        self.GREEN="\033[92m"
        self.RED="\033[91m"
        self.BLUE="\033[94m"
        self.YELLOW="\033[93m"
        self.NONE="\033[0m"
        self.options=None
        self.manuname=None
        self.select=None
        self.inputtext=None
        self.userinput=None
        self.context=None
    def setManu(self,array,manuname,inputtext,context):
        self.options=array
        self.manuname=manuname
        self.inputtext=inputtext
        self.context=context
    def showManu(self):
        print("\n\n")
        print(f"{self.RED}========[{self.YELLOW}{self.manuname}{self.NONE}{self.RED}]=========")
        print("\n")
        if(self.context != None):
            print(f"{self.BLUE}[+] {self.GREEN}{self.context} : {self.NONE}\n")
        for item in range(len(self.options)):
            print(f"{self.BLUE}[{item+1}] {self.GREEN}{self.options[item]} ")
        self.userinput=input(f"\n\n{self.BLUE}{self.inputtext} # {self.GREEN}")
        print(self.NONE)
    def getUserinput(self):
        try:
            return self.options[int(self.userinput)-1]
        except Exception as e:
            return f"{self.RED}[-] No option selected{self.NONE}"
    def getUserinputInt(self):
        return int(self.userinput)
    def getUserinputIndex(self):
        return int(self.userinput-1)



