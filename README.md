# Django Login System with OTP Verification

This is a Django-based login system that uses OTP (One-Time Password) verification for added security.

## Features
- User registration and login
- OTP verification via email 
## Installation
1. Clone the repository
```
git clone https://github.com/yourusername/django-login-otp.git
```
2. Install the required dependencies
```
pip install -r requirements.txt
```
3. Run the migrations
```
python manage.py migrate
```
4. Start the development server
```
python manage.py runserver
```

## Usage
- Register a new user by navigating to `/register` and filling out the form.
- After registering, you will receive an OTP via email
- Enter the OTP on the verification page to complete the registration process.
- Log in using your registered credentials at `/login`.\
  it is the part of my website you can see it in action at https://rahim-khan.azurewebsites.net/

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue.

Is there anything else you would like me to add?
