#請撰寫一程式，將使用者輸入的三個參數，
#變數名稱分別為a（代表字元character）、x（代表個數）、y（代表列數），
#作為參數傳遞給一個名為compute()的函式，該函式功能為：一列印出x個a字元，總共印出y列。
#提示：輸出的每一個字元後方有一空格。
def compute(a,x,y):
    for i in range(y):
        for k in range(x):
            print('%s' %a,end=' ')
        print("   ")
a = input("代表字元character:")
x = eval(input("代表個數:"))
y = eval(input("代表列數:"))
compute(a, x, y)