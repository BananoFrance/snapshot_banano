from bananopy.banano import *

def representatives_snapshot(return_list):
    if return_list == True:
        b = representatives()["representatives"]
        liste=[]
        for cle,valeur in b.items():
            liste.append(cle)
        return liste
    elif return_list == False:
        c = representatives()["representatives"]
        rp_list = open("representatives.txt", "a")
        count = 0
        for key,value in c.items():
            count = count + 1
            rp_list.write(key + "\n")
            print("Account number = ", count)

        account_list.close()

def account_snapshot(list):
    account_list = open("account_list.txt", "a")
    count = 0
    for i in list:
        b = delegators(i)["delegators"]
        for key,value in b.items():
            count = count + 1
            account_list.write(key + "\n")
        print("Account number =", count)
    account_list.close()

account_snapshot(representatives_snapshot(True))