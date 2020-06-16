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

Install version 83.0.4103.39 of [ChromeDriver](https://chromedriver.storage.googleapis.com/index.html?path=83.0.4103.39/), and place the executable into /CourseEnroll

# How to Use
- Start the program before enrollment to allow time for the user to log in. This will ensure that the user begins their enrollment process nearly as soon as it opens.

Change the directory to `/CourseEnroll` and start the program
```
python app.py
```

Log in through window created by CourseEnroll to both CUWebLogin and Two-Step Login.

After logging in, keep the window open in the background. The program will run until the user has been enrolled in all classes in the shopping cart.

Wait for the popup window to appear as a notification that the program has been completed.

# TODO
- Automate term selection, have window asking for term at start
- Figure out why the course files aren't being read
- Fix adds() and drops()
- Eliminate use of shell

### Instructions for When Add/Drop Files Work

- List each course id (4-5 digit number) to be added to the shopping cart in the `addcourses.txt` file
- List each course id to be dropped from the shopping cart in the `dropcourses.txt` file
- Separate the leture, discussion, and lab sections with periods in the same line
```
course.dis.lab
```
- If course does not have any of the above sections, omit them entirely. See `addcourses.txt` and `dropcourses.txt` for some examples.
