
def password_control(password):
	if len(password) < 8:
		print("Длина пароля меньше 8 символов")
		return False

	count_up_b = 0
	count_low_b = 0
	count_cifri = 0
	count_simv = 0

	for i in range(len(password)):
		if password[i].isupper:
			count_up_b += 1
			continue
		if password[i].islower:
			count_low_b += 1
			continue
		if password[i].isdigit:
			count_cifri += 1
			continue
		if password[i].isalpha:
			count_simv += 1

	if count_up_b < 2:
		print("как минимум две большие буквы")
		return False  
	if count_low_b < 2:
		print("как минимум две строчные буквы")  
		return False
	print(count_cifri)
	if count_cifri < 2:
		print(count_cifri)
		print("как минимум две цифры")  
		return False
	if count_simv < 2:
		print("как минимум два символа")  
		return False
	return True

print(password_control('G#!nbP_1'))