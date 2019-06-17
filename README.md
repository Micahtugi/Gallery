## PHOTO-GALLERY
## Author
Micah Mutugi
## Project Description
This is a project that allows the super user to post pictures in the gallery and the viewers could view them and search for different categories of photos in the gallery.
## SetUp instructions
1: Clone this repository from Github
2: Open the terminal and then navigate to the Photo-Gallery folder.
3: Create a virtual environment and run the pip install -r requirements.txt
4: Create a database by running the command below.
CREATE DATABASE gallery;
5: Migrate the database using the following command:
python3.6 manage.py migrate
6: Serve the application using the following command:
python manage.py runserver

## Technologies Used
Python 
Django- web framework used
CSS-for styling the User Interface
HTML-for the templates

## Known Bugs
There are none so far but you could contact me incase you come across one.

## Contact information
You can reach out to me by writing me an email at micahkimathi@gmail.com
## Licence
MIT License

Copyright (c) [2019] [Micah Mutugi]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.