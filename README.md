# Data Science with Django

This is a project to implement data science pipelines including data collection, ETL, and visualization on a webpage. This project is solely made with a Python backend both for data science implementation and rendering webpages. I have used Django framework to power the website, Numpy and Pandas for processing collected data, and Matplotlib and Seaborn for creating visualizations.

Refer to the [`requirements.txt`](https://github.com/Rakib1508/django-data-science/requirements.txt) file to get all the necessary modules used for this project. The steps to build the project will be mentioned below as the project develops.

## Project timeline

Here I have documented each steps that I followed to build this project along with date & time when I have completed a step in the project timeline.

### Setup Environment & Create Django project

#### <time datetime="2021-07-18 21:52:00">July 18, 2021 - 21:52</time>

1. Start the project with a virtual environment. To create the virtual environment, run the given command in any command line terminal.
   `virtualenv djds`
   Activate virtual environment by running
   `djds\scripts\activate` in Windows, or `source bin/activate` in Mac.

2. Install all necessary Python modules given in the `requirements.txt` by running
   `pip install -r requirements.txt`

3. Run `django-admin startproject analyzr .` on your command prompt or terminal to create the basic layout of your django project. The `.` at the end creates the project files on the same directory where you are running the command. You should have a SECRET_KEY in your `settings.py` file; keep this secret from everyone. In this repository, the key has been hidden using random `****` characters.
