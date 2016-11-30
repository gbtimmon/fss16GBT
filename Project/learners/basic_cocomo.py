#Calculations taken from https://arthurdejong.org/cocomo/cocomo.html
#Software project	ab	bb	cb	db
#Organic	2.4	1.05	2.5	0.38
#Semi-detached	3.0	1.12	2.5	0.35
#Embedded	3.6	1.20	2.5	0.32

# embedded=1, semidetached=2, organic=3

#effort =a*KLOCb, in person/months, with KLOC = lines of code, (in the thousands), and:

#duration =c*effortd, finally:
def cocomo_months(type, kloc):
	a,b,c,d=3.6,1.2,2.5,0.32
	if(type==2):
		a,b,c,d=3.0,1.12,2.5,0.35
	elif(type==3):
		a,b,c,d=2.4,1.05,2.5,0.38
	effort=a*(kloc**b)
	print str(effort) + " person months"
	print str(c*(effort**d))+" months"

def cocomo_person(type, kloc):
	a,b,c,d=3.6,1.2,2.5,0.32
	if(type==2):
		a,b,c,d=3.0,1.12,2.5,0.35
	elif(type==3):
		a,b,c,d=2.4,1.05,2.5,0.38
	effort=a*(kloc**b)
	print str(effort) + " person months"