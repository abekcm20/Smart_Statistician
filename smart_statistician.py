import csv
Active = None
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
        print('\nsuccessfully change Rainfall To python\n')
    def sort_list(self,key_rename):
        post_sort_lst = ([int(n) for n in self.dataset[key_rename]])
        for i in range (len(post_sort_lst)):
            for j in range(i + 1, len(post_sort_lst)):
                if(post_sort_lst[i] > post_sort_lst[j]):
                    temp1 = post_sort_lst[i]
                    post_sort_lst[i] = post_sort_lst[j]
                    post_sort_lst[j] = temp1
        print(post_sort_lst)
    def Analyze(self,key_Analyze):
        temp_list = [int(n) for n in self.dataset[key_Analyze]]
        mean = 0
        len_num = len(temp_list)
        for m in temp_list:
            mean += m
        mean = mean/len_num
        
        
        temp_list.sort()
        if len_num % 2 == 0:
            median1 = temp_list[len_num//2]
            median2 = temp_list[len_num//2 - 1]
            median = (median1 + median2)/2
        else:
            median = temp_list[len_num//2]
            
        max_count = (0,0)
        for max_num in temp_list:
            occur = temp_list.count(max_num)
            if occur > max_count[0]:
                max_count = (occur, max_num)
        
        variance = sum([((x - mean) ** 2) for x in temp_list]) / len(temp_list)
        stdeV = variance ** 0.5
    
        
        print("\nnumber of values (n): ",len(temp_list))
        print("             minimum: ",min(temp_list))
        print("             maximum: ",max(temp_list))
        print("                Mean: ",round(mean,2))
        print("              Median: ",round(median,2))
        print("                Mode: ",max_count[1])
        print("  Standard deviation: ",round(stdeV,2))   
            
            
        
def printfun():
    if Active is None:
        print("\nWelcome to The Smart Statistician! \nProgrammed by Abhishek CM")
    print("\nPlease choose from the following options:    \n1 - Load data from a file    \n2 - Display the data to the screen    \n3 - Rename a set    \n4 - Sort a set    \n5 - Analyze a set    \n6 - Quit")
    
    
    
    
def printlist(num):
    if num == 3:
        print("\nWhich set do you want to rename?")
    elif num == 4:
        print("\nWhich set do you want to sort?")
    elif num == 5:
        print("\nWhich set do you want to Analyze?")
    for keys in data:
        lst.append(keys)
    for j in lst:
        print((lst.index(j)+1), '-', j)
    print('\n select one number\n')
    n = int(input())-1
    return n




        
while(Active !='Quit'):
    printfun()
    options = int(input())
    if options == 1:
        Active = not None
    if Active is None or options > 6:
        if options == 6:
            Active='Quit'
        elif options < 6:
            print("\nplease Load data from a file\n")
        else:
            print("\nInvalid option!! Please choose any among 1 to 6.\n")
    else:
        if options == 1:
            if bool(data):
                data.clear()
            print("\n Enter the file name with extension\n")
            with open(input(),'r') as ifile:
                dataReader = csv.reader(ifile)
                for line in dataReader:
                    data[line[0]] = line[1:]
                operation = Smart_Statistician(data)
        elif options == 2:
            operation.Display_Data()
        elif options == 3:
            return_num_3 = printlist(options)
            new = input("\nEnter the new name\n")
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
            Active='Quit'
