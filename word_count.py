
#COUNTING FREQUENCY OF EACH WORD


import glob
import os 
def start():
    home = os.getcwd()
    os.chdir(os.getcwd()+'\\wc_input')
    file_list = glob.glob("*.txt")
    if "result.txt" in file_list:
        file_list.remove('result.txt')
    arr = []
    for f in file_list:
        ff = open(f,'r')
        lines = ff.readlines()
        if lines[-1][-1] != "\n":
            #print('ok!!')
            arr = arr + ['\n']
        arr = arr + lines
        #print(arr)
    
        

    os.chdir(home+"\\wc_output")

    with open('result.txt', 'w') as file:
        file.writelines(arr)


    

    
    ip = open("result.txt","r")
    #ip = ip.read()
    ip=ip.read()

    wdict = dict()
    for line in ip.split('\n'):
        for word in line.split():
            if(',' in word or '.' in word ):
                word = word[:-1]
                word = word.lower()
            if word in wdict:
                wdict[word.lower()] += 1
            else:
                wdict[word.lower()] = 1
    items = sorted(wdict.keys())

    for elem in items:
        print (elem, wdict[elem])
            
if __name__ == "__main__":
    start()




