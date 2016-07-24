def binaries(number):
	id_100 = 2048
	final_number = ""
	for id in range(10):
        	id_100 = id_100/2
        	if (number-id_100) >= 0:
                	final_number = final_number + ("1")
                	number = number - id_100
        	else:
                	if "1" in final_number:
                        	final_number = final_number + ("0")
	check_number=len(final_number)
	if check_number < 8:
		if check_number == 7:
			final_number = "0" + final_number
		if check_number == 6:
			final_number = "00" + final_number
                if check_number == 5:
                        final_number = "000" + final_number
                if check_number == 4:
                        final_number = "0000" + final_number
                if check_number == 3:
                        final_number = "00000" + final_number
                if check_number == 2:
                        final_number = "000000" + final_number
                if check_number == 1:
                        final_number = "0000000" + final_number
		if check_number == 0:
			final_number = "00000000" 
	return final_number

a=binaries(10)
b=binaries(21)
c=binaries(11)
d=binaries(0)
print a 
print b
print c
print d
