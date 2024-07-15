dic_list = {'names':['Adarsh',"Avinesh",'Anvesh'],'professions':['Software',"Banker","Army"]}

for n,p in dic_list.items():
    print('-----' ,n)
    for pro in p:
        print('-',pro)