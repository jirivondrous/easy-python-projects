"""
Simple Login & Signup System
- Allows users to login with existing credentials
- Supports new user signup
- Stores usernames and passwords in a dictionary
- For learning purposes only (no password hashing)
"""

def login_system():
	username: str = input('Enter your username: ')
	password: str = input('Enter your password: ')

	if username in credentials and credentials[username] == password:
		print('You have succesfully logged in!')
	else:
		print('Login failed. Incorrect username or password')


def signup_system():
	print('Sign up for a new account: ')
	while True:
		new_username = input('Choose a username: ')
		if new_username in credentials:
			print('This username is already taken. Please choose another')
		else:
			break

	new_password = input('Choose a password:')

	credentials[new_username] = new_password
	print('Signup successful. You can now login with your new account.')


def main():
	while True:
		action = input('Do you want to login or signup? (login/signup): ').lower()
		if action == 'login':
			login_system()
			break
		elif action == 'signup':
			signup_system()
			break
		else:
			print('Please enter login or signup!')


credentials = {
	'admin': 'adminpass'
}

main()