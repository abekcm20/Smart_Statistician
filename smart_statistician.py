data = {}
lst = []
class Smart_Statistician:
    def __init__(self,dataset):
        self.dataset = dataset
    def Display_Data(self):
        for key in self.dataset:
            print(key)
            for i in self.dataset[key]:
                print(i,end = " ")
            print()
    def Rename(self,oldname,newname):
        temp = self.dataset[oldname]
        del self.dataset[oldname]
        self.dataset[newname] = temp
        print('successfully change Rainfall To python\n')
    def sort_list(self,key_rename):
        post_sort_lst = sorted(self.dataset[key_rename])
        print(post_sort_lst)
    def Analyze(self,key_Analyze):
        temp_list = self.dataset[key_Analyze]
        for i in range(0, len(temp_list)):
            temp_list[i] = int(temp_list[i])
        print("number of values (n): ",len(temp_list))
        print("             minimum: ",min(temp_list))
        print("             maximum: ",max(temp_list))
        print("                Mean: ",statistics.mean(temp_list))
        print("              Median: ",statistics.median(temp_list))
        print("                Mode: ",statistics.mode(temp_list))
        print("  Standard deviation: ",round(statistics.stdev(temp_list),2))   
            
            
        
def printfun():
    if Active is None:
        print("Welcome to The Smart Statistician! \nProgrammed by Abhishek CM")
    print("Please choose from the following options:    \n1 - Load data from a file    \n2 - Display the data to the screen    \n3 - Rename a set    \n4 - Sort a set    \n5 - Analyze a set    \n6 - Quit")
    
    
    
    
def printlist(num):
    if num == 3:
        print("Which set do you want to rename?")
    elif num == 4:
        print("Which set do you want to sort?")
    elif num == 5:
        print("Which set do you want to Analyze?")
    for keys in data:
        lst.append(keys)
    for j in lst:
        print((lst.index(j)+1), '-', j)
    n = int(input())-1
    return n




        
while(Active !='Quit'):
    printfun()
    options = int(input())
    if options == 1:
        Active = not None
    if Active is None or options > 6:
        print("please Load data from a file or Invalid option!! Please choose any among 1 to 6./n")
    else:
        if options == 1:
            with open(input(),'r') as ifile:
                dataReader = csv.reader(ifile)
                for line in dataReader:
                    data[line[0]] = line[1:]
                operation = Smart_Statistician(data)
        elif options == 2:
            operation.Display_Data()
        elif options == 3:
            return_num_3 = printlist(options)
            new = input()
            operation.Rename(lst[return_num_3],new)
            lst.clear()
        elif options == 4:
            return_num_4 = printlist(options)
            operation.sort_list(lst[return_num_4])
            lst.clear()
        elif options == 5:
            return_num_5 = printlist(options)
            operation.Analyze(lst[return_num_5])
            lst.clear()
        elif options == 6:
            print('Thanks')
            Active='Quit'
