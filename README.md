# IFB104-Ass02

# Description
It is a ticket shop application that allows users to view and save data from multiple online sources. The application is implemented using Python and incorporates HTML/CSS markup languages, pattern matching, databases, and a graphical user interface (GUI) design using the Tkinter module.


# The main features and components of the application include:
1. Graphical User Interface (GUI): The application has a GUI built using Tkinter. The GUI window is created using the Tk() function and has a specific size and background color.

2. Web Document Download: The application includes a function called "download()" that allows the user to download and save web documents. It uses the urlopen() function from the urllib.request module to open web documents and read their contents. It also provides an option to save the downloaded document as a local file.

3. Regular Expression Pattern Matching: The re module is used to find occurrences of a pattern defined by a regular expression. This functionality is primarily used to extract specific information from the downloaded web documents, such as event names, dates, times, and images.

4. Data Extraction from Online Sources: The application retrieves data from multiple online sources, including Cbus Super Stadium, Rics Bar, and Suncorp Stadium. It downloads the HTML content of the web pages from these sources, parses the content using regular expressions, and extracts relevant information such as event names, dates, times, and images.

5. Event Information Display: The application displays the event information retrieved from the online sources on the GUI. It includes labels for event names and dates/times, which are dynamically updated based on the user's selection of the venue.

6. Venue Selection: The GUI includes radio buttons that allow the user to select the desired venue. The available options are Cbus Super Stadium, Rics Bar, and Suncorp Stadium. Based on the selected venue, the corresponding event information is displayed on the GUI.

7. Opening Web Links: The application provides functionality to open the web links of the selected venue in the user's default web browser. Clicking the "Open Website" button opens the respective website URL using the urldisplay() function from the webbrowser module.

8. Overall, the application provides a user-friendly interface for viewing event information from different venues and facilitates easy access to the corresponding websites for further details or ticket purchases.






