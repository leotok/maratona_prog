pi = 3.14

while True:
    try:
        
    	volume = float(raw_input())
    	diameter = float(raw_input())

    	a = pi * (diameter / 2) ** 2
    	h = volume / a
    	

    	print "ALTURA = %.2f" %(h)
    	print "AREA = %.2f" %(a)

    except:
        break