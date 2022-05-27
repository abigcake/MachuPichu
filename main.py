import re

# CR: This is called a "state"
# CR: It's the thing that changes throut the running of this program
# CR: Therefore - It should be represented as a class, where these are the members
# CR: Also, add methods to the class like "read_commands", "run_next_command", things like that (basically what you have below)
class RegState:

    registers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    commands_list = []
    command_index = 0

class MovReg:
        def __init__(self, destRegister, sourceRegister):
            self.destRegister = destRegister
            self.sourceRegister = sourceRegister

        # CR: If you'll call this function "run" in all the command classess you'd be able to run a command without knowing what it is!
        # CR: Also, you may want to make all the command classes inherit from "BaseCommand" that implements "run" as "raise NotImplementedError"
        # CR: If you are not familiar with / don't remember inheritance or exceptions - let me know :)
        def run(self):
            RegState.registers[destRegister] = RegState.registers[sourceRegister]


class MovNum:
        def __init__(self, destRegister , sourceNumber):
            self.destRegister = destRegister
            self.sourceNumber = sourceNumber

        def run(self):
            RegState.registers[destRegister] = sourceNumber


class AddRegs:
        # CR: Add a space after each ,
        def __init__(self,destRegister,sourceRegister1, sourceRegister2):
            self.destRegister = destRegister
            self.sourceRegister1 = sourceRegister1
            self.sourceRegister2 = sourceRegister2

        def run(self):
            RegState.registers[destRegister] = RegState.registers[sourceRegister1] + RegState.registers[sourceRegister2]

class SubRegs:
        def __init__(self,destRegister,sourceRegister1, sourceRegister2):
            self.destRegister = destRegister
            self.sourceRegister1 = sourceRegister1
            self.sourceRegister2 = sourceRegister2

        def run(self):
            RegState.registers[destRegister] = RegState.registers[sourceRegister1] - RegState.registers[sourceRegister2]


print(RegState.registers)

# CR: Instead of many else-ifs you can create a dictionary that maps a word to a "creator function"
# CR: For example: { "MovReg": create_mov_reg, ... }
# CR: As long as all of the creator functions would expect the same parameters you'd be fine
# CR: (But what should be the parameters? the 2 sides of the ","? Perhaps the textual non-parsed command? IDK)
with open('test.txt','r') as f:                                                # Parsing the assembly file

    for line in f:
        print(RegState.registers)
        if re.findall("\AMOV", line):                                          #Checking for MOV call

            if len(re.findall("R",line)) == 2:                                 #Checking for MOVReg

               reg = re.findall(r'R\d',line)                                   # Extracting the Registers ID's
               destRegister, sourceRegister = int(reg[0][1]),int(reg[1][1])    #Getting the registers numbers and saving them to the paramaters for the MovReg function
               RegState.commands_list.append(MovReg(destRegister,sourceRegister))           #Declaring MovReg
               RegState.commands_list[RegState.command_index].run()                                #Adiing MovReg object to the command list
               RegState.command_index+=1

            else:                                                              #In case this is a MovNum call

                destRegister = int(re.findall(r'R\d', line)[0][1])             #Extracting the Register's ID's
                sourceNumber = int(re.findall(r'#\d', line)[0][1])             #Extracting The source number
                RegState.commands_list.append(MovNum(destRegister,sourceNumber))
                RegState.commands_list[RegState.command_index].run()
                RegState.command_index += 1

                #Calling MovNum
        elif re.findall("\AADD", line):                                        # Checking for ADD call
            reg = re.findall(r'R\d', line)
            destRegister, sourceRegister1, sourceRegister2 = int(reg[0][1]),int(reg[1][1]),int(reg[2][1])       # Extracting the Registers ID's

            RegState.commands_list.append(AddRegs(destRegister, sourceRegister1, sourceRegister2))
            RegState.commands_list[RegState.command_index].run()
            RegState.command_index += 1

        elif re.findall("\ASUB", line):                                                                          # Checking for SUB call
            reg = re.findall(r'R\d', line)
            destRegister, sourceRegister1, sourceRegister2 = int(reg[0][1]), int(reg[1][1]), int(reg[2][1])  # Extracting the Registers ID's

            RegState.commands_list.append(SubRegs(destRegister, sourceRegister1, sourceRegister2))
            RegState.commands_list[RegState.command_index].run()
            RegState.command_index += 1

print(RegState.registers)  #printing registers
for i in RegState.commands_list: print(i.__repr__())
