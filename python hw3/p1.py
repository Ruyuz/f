def quadratic(A, B, C):
	x1 = (-B + (B**2 - 4*A*C) ** (1/2) ) / (2 * A)
	x2 = (-B - (B**2 - 4*A*C) ** (1/2) ) / (2 * A)
	return x1,x2