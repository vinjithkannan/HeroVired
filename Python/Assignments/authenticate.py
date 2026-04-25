def validate_login(username, password):
	if len(username) < 5:
		print("Error: Username must be at least 5 characters")
		return False

	if len(password) < 8:
		print("Error: Password must be at least 8 characters")
		return False

	has_digit = False
	for char in password:
		if char.isdigit():
			has_digit = True
			break

	if not has_digit:
		print("Error: Password must contain at least one digit")
		return False

	print("Login successful")
	return True


username = input("Enter username: ")
password = input("Enter password: ")
result = validate_login(username, password)
print(f"Return: {result}")
