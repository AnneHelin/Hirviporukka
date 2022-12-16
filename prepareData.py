# MODULE FOR PREPARING DATA TO DISPLAY IT ON QT WIDGETS
# ======================================================

# LIBRARIES AND MODULES
# --------------------------
# from pyQt5.QtWidgets import * # Remove this line when ready
from PyQt5.QtWidgets import QTableWidgetItem # For handling a single table cell

"""
# Temporary object to get help about object properties
resultObject = pgModule.DatabaseOperation()
testConnectionArgs = resultObject.readDatabaseSettingsFromFile('settings.dat')
resultObject.getAllRowsFromTable(
    testConnectionArgs, 'pablic.jakoryhma_yhteenveto')

testTableWidget = QTableWidget()
"""

# DATA PREPARATION FUNCTIONS
#----------------------------


def preparaTable(resultObject, tableWidget):
    """Updates an existing TableWidget using and instance of DatabaseOperation class
    defined in the pgModule

    Args:
        resultObject (DatabaseOperation): Instance of DatabaseOperation class -> errors and result
        tableWidgets (QTableWidget): _description_
    """
    # Clear table widget before populating it
    tableWidget.clear()

    # If there is no error start processing rows and columns of the result set
    if resultObject.errorCode == 0:
        tableWidget.setRowCount(resultObject.rows)
        tableWidget.setColumnCount(resultObject.columns)
        tableWidget.setHorizontalHeaderLabels(resultObject.columnHeaders)

        rowIndex = 0 # Intialize row index
        for tupleIx in resultObject.resultSet: # Cycle through list of tuples
            columnIndex = 0 # Init column index

            for cell in tupleIx: # Cycle through values in the tuple
                cellData = QTableWidgetItem(str(cell)) # Format cell data
                tableWidget.setItem(rowIndex, columnIndex, cellData) # Set cell

                columnIndex +=1

            rowIndex += 1

    def prepareComboBox(resultObject, comboBox, ixToShow, ixToReturn):
        """Prepares data to be shown in a combo box
        
        Args:
            resultObject (DatabaseOperation): Instance of DatabaseOperation class -> errors and result
            comboBox (QComboBox): Combo box to the updated
            ixToShow (int): Index of the column to show in the combo box
            ixToReturn (int): Index of the column containing values of interest 
            
            Returns:
                list: Value of interest
        """ 

        # Clear combo box before populsting it
        comboBox.clear()

        # Result set is a list of tuples even when there is only one column in the view
        cBValuesOfInterest = [] # Empty list for values of interest
        cBItems = [] # Empty list for choices in the combo box
                        
     