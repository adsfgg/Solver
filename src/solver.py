from os import system


def load_logo(filenm):
	logo_array = [""] * 9

	try:
		title = open(filenm)
		index = 0
		for l in title:
			logo_array[index] = l.strip("\n")
			index += 1
		title.close()
	except FileNotFoundError:
		logo_array = [""] * 0
	return logo_array


def display_logo(logo):
	for l in logo:
		print(l)


def debugPrint(s):
	debug = True
	if debug:
		print(s)
		

def solve(eq1, eq2):
	matrix = [[0 for x in range(2)] for x in range(2)]
	inverse = [[0 for x in range(2)] for x in range(2)]
	solutions = [[0 for x in range(2)] for x in range(2)]

	# parse equation 1
	x_index = eq1.find("x")
	coeff = eq1[:x_index]
	if coeff == "+":
		coeff = "1"
	elif coeff == "-":
		coeff = "-1"
	elif (x_index == 0):
		coeff = "1"
	
	matrix[0][0] = int(coeff)
	y_index = eq1.find("y")
	coeff = eq1[x_index + 1: y_index]
	if coeff == "+":
		coeff = "1"
	elif coeff == "-":
		coeff = "-1"

	matrix[1][0] = int(coeff)
	eq_index = eq1.find("=") + 1
	solutions[0][0] = int(eq1[eq_index:])

	# parse equation 2
	x_index = eq2.find("x")
	coeff = eq2[:x_index]
	if coeff == "+":
		coeff = "1"
	elif coeff == "-":
		coeff = "-1"
	elif (x_index == 0):
		coeff = "1"

	matrix[0][1] = int(coeff)
	y_index = eq2.find("y")
	coeff = eq2[x_index + 1: y_index]
	if coeff == "+":
		coeff = "1"
	elif coeff == "-":
		coeff = "-1"

	matrix[1][1] = int(coeff)
	eq_index = eq2.find("=") + 1
	solutions[0][1] = int(eq2[eq_index:])

	# find inverse
	det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

	if det == 0:
		raise ValueError("No solution.")

	inverse[0][0] = matrix[1][1] / det
	inverse[0][1] = -matrix[0][1] / det
	inverse[1][0] = -matrix[1][0] / det
	inverse[1][1] = matrix[0][0] / det

	# solve
	x = (inverse[0][0] * solutions[0][0]) + (inverse[1][0] * solutions[0][1])
	y = (inverse[0][1] * solutions[0][0]) + (inverse[1][1] * solutions[0][1])

	solutions[0][0] = x
	solutions[0][1] = y

	return solutions


def main():
	logo = load_logo("res/logo.txt")
	running = True

	while running:
		system("cls")
		display_logo(logo)
		eq1 = input("Enter first equation (in the form ax + by = c): ").replace(" ", "")
		eq2 = input("Enter second equation (in the form ax + by = c): ").replace(" ", "")
		try:
			solutions = solve(eq1, eq2)
			print("\nx = " + str("{0:.2f}".format(solutions[0][0])) + ", y = " + str("{0:.2f}".format(solutions[0][1])) + "\n")
		except ValueError as e:
			print("\n")
			print(e)
			print("\n")
		running = input("Solve another? (Y/N): ").lower() == "y"


if __name__ == "__main__":
	main()
