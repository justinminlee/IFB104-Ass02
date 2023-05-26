
# A function for exiting the program immediately (renamed
# because "exit" is already a standard Python function).
from sys import exit as abort

# A function for opening a web document given its URL.
# [You WILL need to use this function in your solution,
# either directly or via the "download" function below.]
from urllib.request import urlopen

# Some standard Tkinter functions.  [You WILL need to use
# SOME of these functions in your solution.]  You may also
# import other widgets from the "tkinter" module, provided they
# are standard ones and don't need to be downloaded and installed
# separately.  (NB: Although you can import individual widgets
# from the "tkinter.tkk" module, DON'T import ALL of them
# using a "*" wildcard because the "tkinter.tkk" module
# includes alternative versions of standard widgets
# like "Label" which leads to confusion.)
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Progressbar

# Functions for finding occurrences of a pattern defined
# via a regular expression.  [You do not necessarily need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.]
from re import *

# A function for displaying a web document in the host
# operating system's default web browser (renamed to
# distinguish it from the built-in "open" function for
# opening local files).  [You WILL need to use this function
# in your solution.]
from webbrowser import open as urldisplay

# All the standard SQLite functions.
from sqlite3 import *

# Confirm that the student has declared their authorship.
# You must NOT change any of the code below.
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer)\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string)\n')
    abort()

#
#--------------------------------------------------------------------#



#-----Supplied Function----------------------------------------------#
#
# Below is a function you can use in your solution if you find it
# helpful.  (You are not required to use this function, but it may
# save you some effort.)
#

# A function to download and save a web document.  The function
# returns the downloaded document as a character string and
# optionally saves it as a local file.  If the attempted download
# fails, an error message is written to the shell window and the
# special value None is returned.
#
# Parameters:
# * url - The address of the web page you want to download.
# * target_filename - Name of the file to be saved (if any).
# * filename_extension - Extension for the target file, usually
#      "html" for an HTML document or "xhtml" for an XML
#      document.
# * save_file - A file is saved only if this is True. WARNING:
#      The function will silently overwrite the target file
#      if it already exists!
# * char_set - The character set used by the web page, which is
#      usually Unicode UTF-8, although some web pages use other
#      character sets.
# * incognito - If this parameter is True the Python program will
#      try to hide its identity from the web server. This can
#      sometimes be used to prevent the server from blocking access
#      to Python programs. However we discourage using this
#      option as it is both unreliable and unethical to
#      override the wishes of the web document provider!
#
def download(url = 'http://www.wikipedia.org/',
             target_filename = 'downloaded_document',
             filename_extension = 'html',
             save_file = True,
             char_set = 'UTF-8',
             incognito = False):

    # Import the function for opening online documents and
    # the class for creating requests
    from urllib.request import urlopen, Request

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Import an exception raised when a web document cannot
    # be downloaded
    from urllib.error import URLError

    # Open the web document for reading
    try:
        if incognito:
            # Pretend to be a web browser instead of
            # a Python script (NOT RELIABLE OR RECOMMENDED!)
            request = Request(url)
            request.add_header('User-Agent',
                               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
                               'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                               'Chrome/42.0.2311.135 Safari/537.36 Edge/12.246')
            print("Warning - Request does not reveal client's true identity.")
            print("          This is both unreliable and unethical!")
            print("          Proceed at your own risk!\n")
        else:
            # Behave ethically
            request = url
        web_page = urlopen(request)
    except ValueError:
        print("Download error - Cannot find document at URL '" + url + "'\n")
        return None
    except HTTPError:
        print("Download error - Access denied to document at URL '" + url + "'\n")
        return None
    except URLError:
        print("Download error - Cannot access URL '" + url + "'\n")
        return None
    except Exception as message:
        print("Download error - Something went wrong when trying to download " + \
              "the document at URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None

    # Read the contents as a character string
    try:
        web_page_contents = web_page.read().decode(char_set)
    except UnicodeDecodeError:
        print("Download error - Unable to decode document from URL '" + \
              url + "' as '" + char_set + "' characters\n")
        return None
    except Exception as message:
        print("Download error - Something went wrong when trying to decode " + \
              "the document from URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None

    # Optionally write the contents to a local text file
    # (overwriting the file if it already exists!)
    if save_file:
        try:
            text_file = open(target_filename + '.' + filename_extension,
                             'w', encoding = char_set)
            text_file.write(web_page_contents)
            text_file.close()
        except Exception as message:
            print("Download error - Unable to write to file '" + \
                  target_filename + "'")
            print("Error message was:", message, "\n")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

# To make it easy for the marker to find, use this filename
# for your ticket in Task 2B
ticket_file = 'your_ticket.html'

# Your code goes here


#Create a Tk window
win = Tk()
win.geometry('700x350')
win.config(background='#3D59AB')

frame_font = ('Arial' , 20)
b_font = ('Arial', 15)
c_font = ('Arial', 10)
#Window a title
win.title("Justin Bieber's ticket shop")


event_name = 'Event name will appear here....'
event_date = 'Event date(s) will appear here....'

##Back-end

venues_status1 = IntVar()

superstadium_h='https://cbussuperstadium.com.au/what-s-on.aspx'
ricsbar_h='http://ricsbar.com.au/'
suncorp_h='https://suncorpstadium.com.au/what-s-on.aspx'
download(url = superstadium_h)
download(url = ricsbar_h)
download(url = suncorp_h)


##### Getting html from superstadium
superstadium_page = urlopen(superstadium_h)

byte_data1 = superstadium_page.read()
html_code1 = byte_data1.decode('UTF-8')

text_copy1 = open('superstadium_page.txt', 'w', encoding = 'UTF-8')
text_copy1.write(html_code1)
text_copy1.close()

pattern_superstadium_date = '<h7 class="event-date text-uppercase">(.+)</h7>'
pattern_superstadium_time = '<br>(.+)</h5>'
pattern_superstadium_title = ' <h6 class="event-title">(.+)</h6>'
pattern_superstadium_img = '<img src="(.+)" class="cover-img-top position-absolute">'

superstadium_date = findall(pattern_superstadium_date , html_code1)
superstadium_time = findall(pattern_superstadium_time , html_code1)
superstadium_title = findall(pattern_superstadium_title, html_code1)
superstadium_img = 'https://cbussuperstadium.com.au/'+findall(pattern_superstadium_img, html_code1)[0]

##### Getting name,date from ricsbar
ricsbar_page = urlopen(ricsbar_h)

byte_data2 = ricsbar_page.read()
html_code2 = byte_data2.decode('UTF-8')

text_copy2 = open('ricsbar_page.txt', 'w', encoding = 'UTF-8')
text_copy2.write(html_code2)
text_copy2.close()

pattern_ricsbar_date = ' <time class="datetime">(.+)</time>'
pattern_ricsbar_title = ' <h2>(.+)</h2>'
pattern_ricsbar_img = '<img src=(.+) alt="TAHNEE ROSE SUPPORTED BY MONSTERA" border="0" />'

ricsbar_date = findall(pattern_ricsbar_date , html_code2)
ricsbar_title = findall(pattern_ricsbar_title, html_code2)
ricsbar_img = findall(pattern_ricsbar_img, html_code2)
pattern_ricsbar_img.replace("TAHNEE ROSE SUPPORTED BY MONSTERA", ricsbar_title[0])

##### Getting name,date from suncorp
suncorp_page = urlopen(suncorp_h)

byte_data3 = suncorp_page.read()
html_code3 = byte_data3.decode('UTF-8')

text_copy3 = open('suncorp_page.html', 'w', encoding = 'UTF-8')
text_copy3.write(html_code3)
text_copy3.close()

pattern_sun_date = "<h7 class=\"event-date text-uppercase\">(.*)</h7>"
pattern_sun_time = "<br>(.*)</h5>"
pattern_sun_title = '<h6 class=\"event-title\"(.*)</h6>'
pattern_sun_img = ' <img src="(.+)" class="cover-img-top position-absolute">'

sun_date = findall(pattern_sun_date , html_code3)
sun_time = findall(pattern_sun_time, html_code3)
sun_title = findall(pattern_sun_title, html_code3)
sun_img = 'https://suncorpstadium.com.au/'+findall(pattern_sun_img, html_code3)[0]


#Define the function using regex to find event name and, date or time
def update_option1():
    if venues_status1.get() == 0:
        try:
            _Name['text'] = 'Event:',superstadium_title[0]
            _Date['text'] = 'Date:', superstadium_date[0],superstadium_time[0]
        except:
            _Name['text'] = 'No data found'
            _Date['text'] = 'No data found'

def update_option2():
    if venues_status1.get() == 1:
        try:
            _Name['text'] = 'Event:',ricsbar_title[0]
            _Date['text'] = 'Date:',ricsbar_date[0]
        except:
            _Name['text'] = 'No data found'
            _Date['text'] = 'No data found'
def update_option3():
    if venues_status1.get() == 2:
        try:
            _Name['text'] = 'Event:',sun_title[0]
            _Date['text'] = 'Date:', sun_date[0], sun_time[0]
        except:
            _Name['text'] = 'No data found'
            _Date['text'] = 'No data found'

all_command_op = lambda: [update_option1(),update_option2(),update_option3()]

## Open url
def open_url1():
    if venues_status1.get() == 0:
        urldisplay('https://cbussuperstadium.com.au/what-s-on.aspx')
def open_url2():
    if venues_status1.get() == 1:
        urldisplay('http://ricsbar.com.au/')
def open_url3():
    if venues_status1.get() == 2:
        urldisplay('https://suncorpstadium.com.au/what-s-on.aspx')

all_command_ur = lambda: [open_url1(),open_url2(),open_url3()]

#### Print the ticket
your_ticket = """<!DOCTYPE html>
<html>

  <head>

    <title>Your ticket from Justin Bieber's ticket shop</title>

    <style>
        p  {width: 500px; margin-left: auto; margin-right: auto}
        h1 {width: 500px; margin-left: auto; margin-right: auto} 
    </style>

  </head>
  <meta charset = 'UTF-8'>
  <body>

    <!-- A top-level heading -->
    <h1 align = "center">Admit one</h1>


    <p align = "center">
    This is your ticket courtesy of<br>
    Justin Bieber's ticket shop<br>
    </p>

    <!-- A centred paragraph -->
    <p align = "center">
        "<strong>***EVENT_Name***</strong>!!!"
    </p>

    <p align = "center">
       
            <img src=***Image***
            , width=40%>
    <p>

    <p align = "center">
        <strong>***location***</strong>
    <p>

    <p align = "center">
        ***Event_date***
    <p>

    <p align = "center">
      <a href= ***Web_address***> ***Web_address***</a>
    <p>

  </body>

</html>"""

def ticket_print():
    if venues_status1.get() == 0:
        html_code4 = your_ticket.replace('***EVENT_Name***', superstadium_title[0])
        html_code4 = html_code4.replace('***Image***', superstadium_img)
        html_code4 = html_code4.replace('***location***', 'Cbus Super Stadium')
        html_code4 = html_code4.replace('***Event_date***', superstadium_date[0])
        html_code4 = html_code4.replace('***Web_address***', 'https://cbussuperstadium.com.au/what-s-on.aspx')
        html_file = open('your_ticket.html', 'w', encoding='UTF-8')
        html_file.write(html_code4)
        html_file.close()
    elif venues_status1.get() == 1:
        html_code4 = your_ticket.replace('***EVENT_Name***', ricsbar_title[0])
        html_code4 = html_code4.replace('***Image***', ricsbar_img[0])
        html_code4 = html_code4.replace('***location***', 'Ricsbar')
        html_code4 = html_code4.replace('***Event_date***', ricsbar_date[0])
        html_code4 = html_code4.replace('***Web_address***', 'http://ricsbar.com.au/')
        html_file = open('your_ticket.html', 'w', encoding='UTF-8')
        html_file.write(html_code4)
        html_file.close()
    elif venues_status1.get() == 2:
        html_code4 = your_ticket.replace('***EVENT_Name***', sun_title[0])
        html_code4 = html_code4.replace('***Image***', sun_img)
        html_code4 = html_code4.replace('***location***', 'Suncorp Stadium')
        html_code4 = html_code4.replace('***Event_date***', sun_date[0])
        html_code4 = html_code4.replace('***Web_address***', 'https://suncorpstadium.com.au/what-s-on.aspx')
        html_file = open('your_ticket.html', 'w', encoding='UTF-8')
        html_file.write(html_code4)
        html_file.close()

## DB saving
connection = connect(database = 'bookings.db')
booking_db = connection.cursor()
def saving_button():
    if venues_status1.get() == 0:
        query1 = "INSERT INTO tickets_bought VALUES('***event***', '***date***', 'Cbu SuperStadium', 'https://cbussuperstadium.com.au/what-s-on.aspx')"
        query1 = query1.replace('***event***', superstadium_title[0])
        query1 = query1.replace('***date***', superstadium_date[0])
        booking_db.execute(query1)
        connection.commit()
        booking_db.close()
    elif venues_status1.get() == 1:
        query2 = "INSERT INTO tickets_bought VALUES('***event***', '***date***', 'Ricsbar', 'http://ricsbar.com.au/')"
        query2 = query2.replace('***event***', ricsbar_title[0])
        query2 = query2.replace('***date***', ricsbar_date[0])
        booking_db.execute(query2)
        connection.commit()
        booking_db.close()
    elif venues_status1.get() == 2:
        query3 = "INSERT INTO tickets_bought VALUES('***event***', '***date***', 'Suncorp Stadium', 'https://suncorpstadium.com.au/what-s-on.aspx')"
        query3 = query3.replace('***event***', sun_title[0])
        query3 = query3.replace('***date***', sun_date[0])
        booking_db.execute(query3)
        connection.commit()
        booking_db.close()


##Front-end
#Put picture in Label
image = tkinter.PhotoImage(file="Justinbieber.png")
image_put = Label(win, image=image).grid(padx=10,pady=20,rowspan=3,columnspan=3)

#Put Venues
Venues_st = LabelFrame(win, font = frame_font, width=100, height=50,
                       relief = 'groove' , bg ='#3D59AB', fg = 'skyblue', text = 'Venues')
Venues_st.grid(row=0,column=3)

#Put Options
Options_st = LabelFrame(win, font = frame_font, width=80, height=50,
                        relief = 'groove' , bg ='#3D59AB', fg = 'skyblue',text = 'Options')
Options_st.grid(row=0, column=4, columnspan=2)

#Put Chosen event
Choose_st = LabelFrame(win, font = frame_font, relief = 'groove', width=80, height=50,
                       bg ='#3D59AB', fg = 'skyblue', text = 'Chosen event', borderwidth = 10)
Choose_st.grid(padx=10,pady=20,row=2, column=3, columnspan=3)


#Radiobuttons which are in the venues
Super_buttons = Radiobutton(Venues_st, font = b_font, variable = venues_status1,
                             activeforeground='#3D59AB',activebackground='#3D59AB',
                             bg ='#3D59AB', text = 'Cbus Superstadium', value = 0, state='normal')
Super_buttons.grid(row=0, sticky='w')

Bar_buttons = Radiobutton(Venues_st, font = b_font, variable = venues_status1,
                               activeforeground='#3D59AB',activebackground='#3D59AB',
                               bg ='#3D59AB', text = 'Ricsbar', value = 1, state='normal')
Bar_buttons.grid(row=1, sticky='w')

suncorp_buttons = Radiobutton(Venues_st, font = b_font, variable = venues_status1,
                              activeforeground='#3D59AB',activebackground='#3D59AB',
                              bg ='#3D59AB', text = 'Suncorp Stadium', value = 2, state='normal')
suncorp_buttons.grid(row=2, sticky='w')

#Buttons which are in the options
show_buttons = Button(Options_st, font = b_font,
                      text = 'Show Events', width=14, activeforeground='red', command=all_command_op)
show_buttons.grid(row=0, sticky='w')

display_buttons = Button(Options_st, font = b_font,
                         text = 'Display Details', width=14, activeforeground='red', command=all_command_ur)
display_buttons.grid(row=1, sticky='w')

print_buttons = Button(Options_st, font = b_font,
                       text = 'Print Ticket', width=14, activeforeground='red', command = ticket_print)
print_buttons.grid(row=2, sticky='w')

save_buttons = Button(Options_st, font = b_font,
                      text = 'Save Booking', width=14, activeforeground='red', command = saving_button)
save_buttons.grid(row=3, sticky='w')

#Put text in the chosen event
_Name = Label(Choose_st, font = c_font, fg = '#838B8B', text = event_name,width=40)
_Name.grid(row= 0, sticky='e')

_Date = Label(Choose_st, font = c_font, fg = '#838B8B', text = event_date,width=40)
_Date.grid(row= 1, sticky='e')

#Let win be the mainloop
win.mainloop()

pass

