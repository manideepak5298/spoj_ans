'''http://www.spoj.com/problems/FCTRL2/'''
def main():
	numofval = int(raw_input())
	val = []
	for i in range(numofval):
		val.append(raw_input())
	for i in range(numofval):
		print fact(int(val[i]))

def fact(num):
	a = [0 for i in range(num)];
	a[0] = 1;
	for i in range(1,num):
		a[i] = a[i-1]*(i+1);
	return a[num-1];
main()