#author : HUI HOLA
#github : https://github.com/HuiHola
#version : 0.2
from rich.console import Console
from rich.table import Table
from rich.align import Align
class SimpleManu:
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
    def setManu(self,options,title="Simple Manu",console_text="select",context="Chose a Number"):
        self.options=options
        self.manuname=title
        self.inputtext=console_text
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
            return self.userinput
    def getUserinputAsInt(self):
        return int(self.userinput)
    def getUserinputIndex(self):
        return int(self.userinput)-1



class TableManu:
    def __init__(self):
        columns_name=None
        rows_section=None
        title=None
        table=None
        input_text=None
        user_input=None
        self.color='blue'
        self.style='bright'
    def setColors(self,color,style):
        self.color=color
        self.style=style
    def setManu(self,title="Table Manu",console_text="Select",columns=None,rows=None):
        self.table = Table(title=f"[bold yellow]{title}[/bold yellow]")
        Align.center(self.table)
        self.rows_section=rows
        self.columns_name=columns
        self.input_text=console_text
        for column in self.columns_name:
            self.table.add_column(column)

        for row in self.rows_section:
            self.table.add_row(*row, style=f'{self.style}_{self.color}')
    def showManu(self):
        console = Console()
        console.print(self.table)
        user=input(f"\033[94m{self.input_text} # \033[92m")
        self.user_input=user
        print("\033[0m")
    def getUserinput(self):
        return self.user_input
    def getUserinputRow(self):
        try:
            user_input=self.rows_section[int(self.user_input)-1]
        except Exception as e :
            raise Exception("Unexpected input")
        return user_input
