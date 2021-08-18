# CourseEnroll
Automates the enrollment process for Cornell's Student Center
- Continually checks the student center 'Enroll'>'Add' page until enrollment opens
- Loops through the confirmation screens until user is enrolled in all chosen classes
- Notifies user when process is complete

### Read Before You Use:
- Initial courses must be added to the 'Shopping Cart' before the enrollment period opens
- Shopping cart may not be edited while program is running
- After login and term selection, window must be kept open, but it is able to run in the background

# Installation
This program was developed on python 3.6.5.

Copy the repository
```
git clone https://github.com/keri-tenerowicz/CourseEnroll.git
```

Install the requirements
```
pip install -r requirements.txt
```

Install the latest version of [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/), and place the executable into /CourseEnroll

# How to Use
- Start the program before enrollment to allow time for the user to log in. This will ensure that the user begins their enrollment process nearly as soon as it opens.

Change the directory to inside the CourseEnroll folder and start the program
```
python app.py
```

Log in through window created by CourseEnroll to both CUWebLogin and Two-Step Login.

<p align="center">
  <img src="https://github.com/keritenerowicz/CourseEnroll/blob/master/images/login.png" />
</p>

After logging in, keep the window open in the background. The program will run until the user has been enrolled in all classes in the shopping cart. Below is what the one of the enrollment screens should look similar to.

<p align="center">
  <img src="https://github.com/keritenerowicz/CourseEnroll/blob/master/images/enrollment.png" />
</p>

Wait for the popup window to appear as a notification that the program has been completed. It will be one of the following.

Successful:
<p align="center">
  <img src="https://github.com/keritenerowicz/CourseEnroll/blob/master/images/successful.png" />
</p>

Not Successful:
<p align="center">
  <img src="https://github.com/keritenerowicz/CourseEnroll/blob/master/images/not_successful.png" />
</p>
