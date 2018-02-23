# Número Primo

def isPrime(number):
	if number < 2:
		return False
	elif number == 2:
		return True
	elif number > 2 and number % 2 == 0:
		return False
	else:
		for i in range(3, number):
			if number % i == 0:
				return False
			
	return True



def main():
	num = int(input("ingresar número: "))
	result = isPrime(num)

	if result is True:
		print("El número es primo")
	else:
		print("El número NO es primo")

if __name__ == '__main__':
	main()