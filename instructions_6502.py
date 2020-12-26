'''
Three things
1. I want whatever is at that position
2. I want whatever is at memory position x
3. I want whatever is x amount away from position x

Depending on indexing there is different data that can be used
so for example
aaaaaa
aa
aaaaa
'''

class Instructions:
    '''
    @param: b is the byte (processing as an int at the moment for clarity
    before i figure out how to move it to hex

    '''
    def __init__(self,b):
        self.b = b

    '''
    Different instructions different methods
    
    '''
    def pick_instr(self):
        pass

