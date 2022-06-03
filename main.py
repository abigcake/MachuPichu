import re

class RegState:

    registers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    commands_list = []
    command_index = 0


    def read_commands(self):
        select_command_dic = {"MOV R R": self.creation_mov_reg, "MOV R #": self.creation_mov_num, "ADD R R": self.creation_add,"SUB R R": self.creation_sub}

        with open('test.txt','r') as f:

            for line in f:

                  dic_key = " ".join([line[0:3], line[4], line[7]])
                  select_command_dic[dic_key](line)

    def run_next_command(self):

                RegState.commands_list[self.command_index].run()
                self.command_index+=1
                print(RegState.registers)

    def creation_mov_reg(self,line):

        reg = re.findall(r'R\d', line)  # Extracting the Registers ID's
        destRegister, sourceRegister = int(reg[0][1]), int(reg[1][1])
        RegState.commands_list.append(MovReg(destRegister, sourceRegister))


    def creation_mov_num(self,line):

        destRegister = int(re.findall(r'R\d', line)[0][1])  # Extracting the Register's ID's
        sourceNumber = int(re.findall(r'#\d', line)[0][1])  # Extracting The source number
        RegState.commands_list.append(MovNum(destRegister, sourceNumber))


    def creation_add(self,line):

        reg = re.findall(r'R\d', line)
        destRegister, sourceRegister1, sourceRegister2 = int(reg[0][1]), int(reg[1][1]), int(reg[2][1])  # Extracting the Registers ID's
        RegState.commands_list.append(AddRegs(destRegister, sourceRegister1, sourceRegister2))


    def creation_sub(self,line):
        reg = re.findall(r'R\d', line)
        destRegister, sourceRegister1, sourceRegister2 = int(reg[0][1]), int(reg[1][1]), int(reg[2][1])  # Extracting the Registers ID's
        RegState.commands_list.append(SubRegs(destRegister, sourceRegister1, sourceRegister2))

class BaseCommand:

    def __init__(self, destRegister, sourceNumber, sourceRegister1,sourceRegister2):
        self.destRegister = destRegister
        self.sourceNumber = sourceNumber
        self.sourceRegister1 = sourceRegister1
        self.sourceRegister2 = sourceRegister2


class MovReg(BaseCommand):
        def __init__(self, destRegister, sourceRegister):
            self.destRegister = destRegister
            self.sourceRegister = sourceRegister

        # CR: Also, you may want to make all the command classes inherit from "BaseCommand" that implements "run" as "raise NotImplementedError"
        # CR: If you are not familiar with / don't remember inheritance or exceptions - let me know :)

        def run(self):
            RegState.registers[self.destRegister] = RegState.registers[self.sourceRegister]

class MovNum:
        def __init__(self, destRegister , sourceNumber):
            self.destRegister = destRegister
            self.sourceNumber = sourceNumber

        def run(self):
            RegState.registers[self.destRegister] = self.sourceNumber


class AddRegs:
        def __init__(self,destRegister,sourceRegister1, sourceRegister2):
            self.destRegister = destRegister
            self.sourceRegister1 = sourceRegister1
            self.sourceRegister2 = sourceRegister2

        def run(self):
            RegState.registers[self.destRegister] = RegState.registers[self.sourceRegister1] + RegState.registers[self.sourceRegister2]

class SubRegs:
        def __init__(self,destRegister,sourceRegister1, sourceRegister2):
            self.destRegister = destRegister
            self.sourceRegister1 = sourceRegister1
            self.sourceRegister2 = sourceRegister2

        def run(self):
            RegState.registers[self.destRegister] = RegState.registers[self.sourceRegister1] - RegState.registers[self.sourceRegister2]


print(RegState.registers)
s = RegState()
s.read_commands()
for i in range(len(s.commands_list)):
    s.run_next_command()
