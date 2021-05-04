class Q2_ave_list:
    def aveList(listarray):
        if type(listarray) is list:
            if not listarray:
                return "empty"
            else:
                total = 0.0
                for i in listarray:
                    if type(i) is not int:
                        return "not number"
                    total += i
                ave = float(total) / float(len(listarray))
                return ave
        else :
            return "not list"
        
        

    #print(aveList([1,2,3,4,5]))