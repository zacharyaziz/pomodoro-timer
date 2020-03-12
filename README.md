get started on windows by
```bat
git clone http://github.com/hassancodes/pomodoro-timer.git
cd pomodoro-timer
pip install -r requirements
py pomodoro-timer
```
get started on mac by
```sh
git clone http://github.com/hassancodes/pomodoro-timer.git
cd pomodoro-timer
pip install -r requirements
python pomodoro-timer
```

# project specs:
* a page with the timer in it
* a page with a record with past sessions 
* a page with a graph for sessions per day

# technology stack:
* gui framework tkinter (easy to learn)
* sqlite (great for apps with 1 user)

# architecture:
* controller.py a controller that controls all pages and the apps
* views.py has all the pags of the app
* schema.sql has the database schema
* utils.py has a set of utils to use
* manage.sh/manage.bat has the management code for the build/deployment/setting of the app
* requirements.txt has the required packages to run the app

# standerds: (open for change)
* single qoutes
* indent with 4 spaces
