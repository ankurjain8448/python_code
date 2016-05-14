t = int(raw_input())


def two_dec_place(a):
	pass
	f = str(a)
	dot = f.index(':')
	dec = f[dot+1:dot+3]
	if not len(dec)==2 :
		dec+='0'
	if dot == 2 :
		ans = f[:dot+1]+dec
	else :
		ans = '0'+f[:dot+1]+dec
	return ans



def calculate(angle):
	diff = float(1.0/120.0)
	# 50n -5.5p = angle
	angle = float(angle)
	arr = []
	for hour in xrange(12):
		hour = float(hour)
		minute = int((2*(30*hour - angle))/11)
		if minute > -1 :				
			if minute == 60 :
				minute=0
			hour = int(hour)
			x = float(60*hour - 11*minute)
			print "hour : ",str(hour) ," and minute : ",str(minute)," and x : ",str(x), " -d : ",str(angle - diff), " +d : ",str(angle + diff)
			if  angle - diff < x and x < angle+diff :
				if hour == 11 and minute == 60 :
					pass
				else:
					arr.append((str(hour)+":"+str(minute)))
	return arr


while t:
	t-=1
	angle = float(raw_input())
	for each in calculate(angle):
		print each