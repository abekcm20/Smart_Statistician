import csv
import re
Active = None
data = {}
lst = []
rows = []
class Smart_Statistician:
    def __init__(self,dataset):
        self.dataset = dataset
    def Display_Data(self):
        for key in self.dataset:
            print(key)
            for p in range(len(key)):
                print('-',end=(''))
            print()
            print(*self.dataset[key],sep=(','))
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
        print(*post_sort_lst, sep=(','))
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
        md_freq = {}
        md_temp = [] 
        for md in temp_list:
            if md not in md_freq:
                md_freq[md] = 1
            else:
                md_freq[md] += 1
        maxi = max(list(md_freq.values()))
        for key in md_freq:
            if md_freq[key] == maxi:
                md_temp.append(key)
        variance = sum([((x - mean) ** 2) for x in temp_list]) / len(temp_list)
        stdeV = variance ** 0.5   
        return [len(temp_list),min(temp_list),max(temp_list),round(mean,2),round(median,2),md_temp,round(stdeV,2),maxi]   
            

        

def printfun():
    if Active is None:
        print("\nWelcome to The Smart Statistician! \nProgrammed by Abhishek CM")
    print("\nPlease choose from the following options:    \n1 - Load data from a file    \n2 - Display the data to the screen    \n3 - Rename a set    \n4 - Sort a set    \n5 - Analyze a set    \n6 - Save data to a file    \n7 - Compare two sets    \n8 - Edit a set    \n9 - Quit")


    
    
    
    
def printlist(num,dum=False):
    if num == 3:
        print("\nWhich set do you want to rename?")
    elif num == 4:
        print("\nWhich set do you want to sort?")
    elif num == 5:
        print("\nWhich set do you want to Analyze?")
    elif num == 7:
        print("\nWhich set do you want to camoare first?\n")
    elif dum == True:
        print("\nWhich set do you want to camoare second?\n")
    elif num == 8:
        print("\nWhich set do you want to edit\n")
    for keys in data:
        lst.append(keys)
    for j in lst:
        print((lst.index(j)+1), '-', j)
    print('\n select one number\n')
    n = int(input())-1       
    return n

def campare(num,dum = True):
    first = printlist(num)
    first_data = operation.Analyze(lst[first])
    lst.clear()
    sec = printlist(0,dum)
    sec_data = operation.Analyze(lst[sec])
    fmode = []
    smode = []
    if first_data[-1] == 1:
        fmode.append("None")
    else:
        for x in first_data[5]:
            fmode.append(x)
    if sec_data[-1] == 1:
        smode.append("None")
    else:
        for x in sec_data[5]:
            smode.append(x)
    strf = 'Max Temp In '+str(lst[first])
    strc = 'Max Temp In '+str(lst[sec])
    print('                      '+strf+' '+strc)
    print('                      '+'-'*len(strf)+' '+'-'*len(strc))
    print("\nnumber of values (n): ",first_data[0],' '*(len(strf)-len(str(first_data[0]))),sec_data[0])
    print("             minimum: ",first_data[1],' '*(len(strf)-len(str(first_data[1]))),sec_data[1])
    print("             maximum: ",first_data[2],' '*(len(strf)-len(str(first_data[2]))),sec_data[2])
    print("                Mean: ",first_data[3],' '*(len(strf)-len(str(first_data[3]))),sec_data[3])
    print("              Median: ",first_data[4],' '*(len(strf)-len(str(first_data[4]))),sec_data[4])
    print("                Mode:  "+str(*fmode)+' '*(len(strf)-len(str(*fmode)))+str(*smode),sep=',')
    print("  Standard deviation: ",first_data[-2],' '*(len(strf)-len(str(first_data[-2]))),sec_data[-2])
    lst.clear()
    fmode.clear()
    smode.clear()
def printedit():
    print("(i)nsert a value")
    print("(m)odify a value")
    print("(d)elet a value")
    print("(f)inish editing")
    return input()
def insert1(array):
    for k in range(len(array)):
        if k == 0:
            print(str(k+1)+'. at the beginning')
        elif k == len(array)-1:
            print(str(len(array))+'. at the end')
        elif (k > 0) and (k != len(array)-1):
            print(str(k+1)+'. between '+str(array[k])+' and '+str(array[k+1]))
    print(' '*2+str(len(array)+1)+'. cancel insert')
    print('\n select one number')
    ins = int(input())-1
    return ins
def mod_del(mod,array_mod):
    if mod == 'm':
        print('\nWhich value will you modify?\n')
    elif mod == 'd':
        print('\nWhich value will you delete?\n')
    for l in range(len(array_mod)):
        print('  '+str(l+1)+'. ',array_mod[l])
    print(str(len(array_mod)+1)+'. cancel delete')
    print('\n select one number')
    n_mod = int(input())-1
    return n_mod
    
while(Active !='Quit'):
    printfun()
    options = int(input())
    if options == 1:
        Active = not None
    if Active is None or options > 9:
        if options == 9:
            Active='Quit'
        elif options < 9:
            print("\nplease Load data from a file\n")
        else:
            print("\nInvalid option!! Please choose any among 1 to 6.\n")
    else:
        if options == 1:
            if bool(data):
                data.clear()
            print("\n Enter the file name with extension\n")
            regexp = '^(\w|\.|\_|\-)+[.]csv'
            file_name = input()
            if(re.search(regexp, file_name)):
                try:
                    with open(file_name,'r') as ifile:
                        dataReader = csv.reader(ifile)
                        try:
                            for line in dataReader:
                                data[line[0]] = line[1:]
                        except:
                            print('\nthe file contains a dataset with no data\n')
                except IOError:
                    print('\nfile not found\n')
                else:
                    operation = Smart_Statistician(data)
            else:
                print('\nthe file is in an unexpected format\n')
        elif options == 2:
            operation.Display_Data()
        elif options == 3:
            return_num_3 = printlist(options)
            new = input("\nEnter the new name\n")
            if new in lst:
                print("\n Name must be unique\n")
            elif new:
                operation.Rename(lst[return_num_3],new)
            else:
                print("\nName cannot be blank\n")
            lst.clear()
        elif options == 4:
            return_num_4 = printlist(options)
            operation.sort_list(lst[return_num_4])
            lst.clear()
        elif options == 5:
            return_num_5 = printlist(options)
            oprt = operation.Analyze(lst[return_num_5])
            print("\nnumber of values (n): ",oprt[0])
            print("             minimum: ",oprt[1])
            print("             maximum: ",oprt[2])
            print("                Mean: ",oprt[3])
            print("              Median: ",oprt[4])
            if oprt[-1] != 1:
                print("                Mode: ",end = " ")
                print(*oprt[5],sep=(', '))
            else:
                print("                Mode: ",'None')
            print("  Standard deviation: ",oprt[-2])
            lst.clear()
        elif options == 6:
            for k, v in data.items():
                rows.append([k] + v)
            with open('save.csv', 'w') as csvfile:
                csvwriter = csv.writer(csvfile) 
                csvwriter.writerows(rows)
                print("save sucessfully")
        elif options == 7:
            campare(options)
        elif options == 8:
            select = printlist(options)
            p = printedit()
            if p == 'i':
                ins_tem = insert1(data[lst[select]])+1
                in_te = data[lst[select]]
                if len(data[lst[select]]) <= ins_tem:
                    print('\nYou have cancelled the insert operation\n')
                else:   
                    print("\nEnter the value\n")
                    ins_data = input()
                    print("You have modified",in_te[ins_tem],'to'+str(ins_data))
                    data[lst[select]].insert(ins_tem,ins_data)
                    lst.clear()
            elif p == 'm':
                mod_tem = mod_del(p,data[lst[select]])
                p_m = data[lst[select]]
                if len(data[lst[select]]) <= mod_tem:
                    print('\nYou have cancelled the modify operation\n')
                else:
                    print("\nEnter the value\n")
                    mod_data = input()
                    print("You have modify",p_m[mod_tem])
                    p_m[mod_tem] = mod_data
                    lst.clear()
            elif p == 'd':
                mod_del = mod_del(p,data[lst[select]])
                p_m = data[lst[select]]
                if len(data[lst[select]]) <= mod_del:
                    print('\nYou have cancelled the delete operation\n')
                else:
                    print("You have delet",p_m[mod_del])
                    p_m.pop(mod_del)
                    lst.clear()
            elif p == 'f':
                print("\nfinish editin\n")
            else:
                lst.clear()
                
        elif options == 9:
            Active='Quit'