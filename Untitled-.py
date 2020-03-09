def five(input):
	list = input.split(",")
    print(list)
	newlist = []
	for i in range(0,len(list),4):
		if list[i+3] == "False":
         #   print(list[i+3])
			newlist[i] = list[i]
		return newlist
	return ""



print(five("Jeff,random.py,False,1445"))
print(five("Bert,numberGen.py,True,1447,Bert,integers.py,True,1318,Jeff,floats.py,False,1445"))
print(five("Bert,boolean.py,False,1447,Bert,conditions.py,False,1318,Jeff,loops.py,False,1445"))
print(five("Bert,prime.py,True,1447,Bert,ISBN.py,False,1318,Jeff,OOP.py,False,1445"))
    

    #five("Jeff,random.py,False,1445") → ["Jeff"]
	# five("Bert,numberGen.py,True,1447,Bert,integers.py,True,1318,Jeff,floats.py,False,1445") → ["Jeff"]
	# five("Bert,boolean.py,False,1447,Bert,conditions.py,False,1318,Jeff,loops.py,False,1445") → ["Bert","Jeff"]
    # five("Bert,prime.py,True,1447,Bert,ISBN.py,False,1318,Jeff,OOP.py,False,1445") → ["Bert","Jeff"]
    