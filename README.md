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
![Image of CUWebLogin](https://github.com/keritenerowicz/CourseEnroll/blob/master/images/CUWebLogin.png)
![Image of 2step](https://github.com/keritenerowicz/CourseEnroll/blob/master/images/2step.png)

After logging in, keep the window open in the background. The program will run until the user has been enrolled in all classes in the shopping cart.
![Image of EnrollmentScreen](https://github.com/keritenerowicz/CourseEnroll/blob/master/images/enroll1.png)

Wait for the popup window to appear as a notification that the program has been completed. One of the following notificaitons will be shown:
![Image of Success](https://github.com/keritenerowicz/CourseEnroll/blob/master/images/logo_success.jpg)
![Image of Failed](https://github.com/keritenerowicz/CourseEnroll/blob/master/images/logo_failed.jpg)

# TODO
- Automate term selection, have window asking for term at start
- Figure out why the course files aren't being read
- Fix adds() and drops()
- Eliminate use of shell
- Add delay when program goes faster
- start based on EST time

### Instructions for When Add/Drop Files Work

- List each course id (4-5 digit number) to be added to the shopping cart in the `addcourses.txt` file
- List each course id to be dropped from the shopping cart in the `dropcourses.txt` file
- Separate the leture, discussion, and lab sections with periods in the same line
```
course.dis.lab
```
- If course does not have any of the above sections, omit them entirely. See `addcourses.txt` and `dropcourses.txt` for some examples.
