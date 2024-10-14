class Numbers:
    list_0 = []
    list_1 = []
    def __init__(self, number, index):
        self.number = number
        self. index = index
        if self.index == 0:
            self.list_0.append(number)
        else:
            self.list_1.append(number)
    
    def __str__(self):
        return str(self.list_0) + " "+ str(self.list_1)
    
    def total_lists():
        total_list_0 = sum(Numbers.list_0)
        total_list_1 = sum(Numbers.list_1)
        return str(Numbers.list_0) + "="+ str(total_list_0)+ "\n"+ str(Numbers.list_1)+ "="+ str(total_list_1)
    
    def __eq__():
        if sum(Numbers.list_1) == sum(Numbers.list_0):
            return "Are " + str(Numbers.list_0) + " & " + str(Numbers.list_1) + " equal is True"
        else:
            return "Are" + str(Numbers.list_0) + "&" + str(Numbers.list_1) + "equal is False"