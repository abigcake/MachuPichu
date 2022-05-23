import re

registers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
commands_list = []
command_index = 0

class MovReg:
        def __init__(self, destRegister, sourceRegister):
            self.destRegister = destRegister
            self.sourceRegister = sourceRegister

        def movreg(self):
            registers[destRegister] = registers[sourceRegister]


class MovNum:
        def __init__(self, destRegister , sourceNumber):
            self.destRegister = destRegister
            self.sourceNumber = sourceNumber

        def movnum(self):
            registers[destRegister] = sourceNumber


class AddRegs:
        def __init__(self,destRegister,sourceRegister1, sourceRegister2):
            self.destRegister = destRegister
            self.sourceRegister1 = sourceRegister1
            self.sourceRegister2 = sourceRegister2

        def addregs(self):
            registers[destRegister] = registers[sourceRegister1] + registers[sourceRegister2]

class SubRegs:
        def __init__(self,destRegister,sourceRegister1, sourceRegister2):
            self.destRegister = destRegister
            self.sourceRegister1 = sourceRegister1
            self.sourceRegister2 = sourceRegister2

        def subregs(self):
            registers[destRegister] = registers[sourceRegister1] - registers[sourceRegister2]


print(registers)

with open('test.txt','r') as f:                                                # Parsing the assembly file

    for line in f:
        print(registers)
        if re.findall("\AMOV", line):                                          #Checking for MOV call

            if len(re.findall("R",line)) == 2:                                 #Checking for MOVReg

               reg = re.findall(r'R\d',line)                                   # Extracting the Registers ID's
               destRegister, sourceRegister = int(reg[0][1]),int(reg[1][1])    #Getting the registers numbers and saving them to the paramaters for the MovReg function
               commands_list.append(MovReg(destRegister,sourceRegister))           #Declaring MovReg
               commands_list[command_index].movreg()                                #Adiing MovReg object to the command list
               command_index+=1

            else:                                                              #In case this is a MovNum call

                destRegister = int(re.findall(r'R\d', line)[0][1])             #Extracting the Register's ID's
                sourceNumber = int(re.findall(r'#\d', line)[0][1])             #Extracting The source number
                commands_list.append(MovNum(destRegister,sourceNumber))
                commands_list[command_index].movnum()
                command_index += 1

                #Calling MovNum
        elif re.findall("\AADD", line):                                        # Checking for ADD call
            reg = re.findall(r'R\d', line)
            destRegister, sourceRegister1, sourceRegister2 = int(reg[0][1]),int(reg[1][1]),int(reg[2][1])       # Extracting the Registers ID's

            commands_list.append(AddRegs(destRegister, sourceRegister1, sourceRegister2))
            commands_list[command_index].addregs()
            command_index += 1

        elif re.findall("\ASUB", line):                                                                          # Checking for SUB call
            reg = re.findall(r'R\d', line)
            destRegister, sourceRegister1, sourceRegister2 = int(reg[0][1]), int(reg[1][1]), int(reg[2][1])  # Extracting the Registers ID's

            commands_list.append(SubRegs(destRegister, sourceRegister1, sourceRegister2))
            commands_list[command_index].subregs()
            command_index += 1

print(registers)  #printing registers
for i in commands_list: print(i.__repr__())
