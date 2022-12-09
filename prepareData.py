# MODULE FOR PREPARING DATA TO DISPLAY IT ON QT WIDGETS
# ======================================================

# LIBRARIES AND MODULES
# --------------------------
import pgModule
# from pyQt5.QtWidgets import * # Remove this line when ready
from PyQt5.QtWidgets import QTableWidgetItem # For handling a single table cell

"""# Temporary object to get help about object properties
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
    # If there is no error start processing rows and columns of the result set
    if resultObject.errorCode == 0:
        tableWidget.setRowCount(resultObject.rows)
        tableWidget.setColumnCount(resultObject.columns)
        tableWidget.setHorizontalHeaderLabels(resultObject.columnHeaders)

        rowIndex = 0 # Intialize row index
        for tupleIx in resultObject.resultSet: # Cycle through list of tuples
            columnIndex = 0 # Init column index

            for cell in tupleIx: # Cycle through values in the tuple
                cellData = QTableWidgetItem(str(cell))
                tableWidget.setItem(rowIndex, columnIndex, cellData)

            celldata = QTableWidgetItem()
        resultObject.columnHeaders

        resultObject.resultSet
    

    # BUG: