import math
t =long(raw_input())
while t>0:
	ans = ""
	t-=1
	n,x1,y1,x2,y2 = map(long,raw_input().split())
	r=[ long(i) for i in raw_input().split()]
	r1 = long(min(r))
	r=[ long(i) for i in raw_input().split()]
	r2 = long(min(r))
	d = math.sqrt(long((x2-x1)**2 + (y2-y1)**2))
	if d>=r1+r2:
		ans= "0.00"
	else:
		pi = math.pi
		if d<=(r1-r2):
			ans= pi*r2*r2
		elif d<=(r2-r1):
			ans= pi*r1*r1
		else :
			o1_radian =  math.acos((d*d + r1*r1 - r2*r2)/2*d*r1)
			o2_radian =  math.acos((d*d + r2*r2 - r1*r1)/2*d*r2)
			o1 =(2*o1_radian)*180/pi
			o2 =(2*o2_radian)*180/pi
			a1 = 0.5*r1*r1*sin(2*o1_radian)
			a2 = 0.5*r2*r2*sin(2*o2_radian)		
			ans = (pi/360)(o1*(r1**2) + o2*(r2**2)) - a1-a2
			# ans = r1*r1*(o1_radian - 0.5*sin(2*o1_radian)) + r2*r2*(o2_radian-0.5*sin(2*o2_radian))
		ans = str(ans)
		l = len(ans)
		found = '.' in ans
		if found :
			index = ans.index('.')
			index = index+2
			if l>index:
				ans = ans[:index+1]
	print ans