# APPLICATION FOR SHOWING SUMMARY DATA ABOUT MEAT GIVEN TO SHARE GROP
#-----------------------------------------------------------------------------------

# LIBRATES AND MODUKES
#--------------------------------------------------------------------------------

import SYS # Needed for starting the application
import psycopg2
from PyQt5Widget import * # All widgets
from PyQt5.uic import loadui

# CLASS DEFINITIONS FOR THE APP
#--------------------------------

class GroupMainWindow(QMainWindow):

        # Constructor, a method for creating objects from this class
        def __init__(self):
                QMainWindow.__init__(self)

                # Create an UI from the ui file
                loadui('groupInfoMainWindow.ui', self)

                # Define properties for ui elements
                self.refreshBtn = self.refreshBtn
                self.groupInfo = self.groupInfo
                self.sharedMeatInfo = self.meatSharedTableWidget

                # Database connection parameters
                self.database = "metsastys"
                self.user = "sovellus"
                self.userPassword = "O2werty"
                self.server = "localhost"
                self.port = "5432"

                # SIGNALS 

                # Emit a signal when refrsh push button is pressed
                self.refreshBtn.clicked.connect(self.refreshData)

#  SLOTS
        
    # Load data to table Widgets
    # Try to establish a connection to DB server
def refreshData(self):

        # To avoid Fata error crashing the app uses try-except-finally structure
        try:
        # Create a connection object
            dbaseconnection = psycopg2.connect(database= self.database, user= self.user, password= self.password,
                                        host= self.host, port= self.port)              
           
            # Create a cursor                             





            












