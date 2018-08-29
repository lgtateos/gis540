# Author: Unknown. Possibly timmorgan. Found here: http://snippets.dzone.com/posts/show/2036
# Modified by: Laura Tateosian 3/17/09 Removed some methods. Added set_cell_value.
#              Laura Tateosian 3/15/11 Added getName
# Class for reading/writing excel files.
# Warning:  This class provides limited functionality and is designed to be relatively simple example of interacting
#           with Python classes.   Some functionality may be unstable. 
#           For extensive work with Excel, you may want to investigate more sophisticated approaches,
#           including packages like xlrd, xlwt, xlutils.  

from win32com.client import constants, Dispatch
import pythoncom
import os
     

borderTop = 3
borderBottom = 4
borderLeft = 1
borderRight = 2
borderSolid = 1
borderDashed = 2
borderDotted = 3
colorBlack = 1
directionUp = -4162
directionDown = -4121
directionLeft = -4131
directionRight = -4152 
class ExcelDocument(object):
    """
    Some convenience methods for Excel documents accessed
    through COM.
    """

    def __init__(self, visible=False):
        '''
        Constructor method
        '''
        self.app = Dispatch("Excel.Application") #Call the Component Object Model dispatch for Excel(COM) Microsoft interface for its software 
        self.app.Visible = visible  #Make the application visible or not
        self.sheet = 1  #Set the number of sheets to 1

    def new(self, filename=None):
        """
        Create a new Excel workbook. If 'filename' specified,
        use the file as a template.
        """
        self.app.Workbooks.Add(filename)

    def open(self, filename):
        """
        Open an existing Excel workbook for editing.
        """
        self.app.Workbooks.Open(filename)

    def set_sheet(self, sheet):
        """
        Set the active worksheet.
        """
        self.sheet = sheet

    def get_range(self, range):
        """
        Get a range object for the specified range or single cell.
        """
        return self.app.ActiveWorkbook.Sheets(self.sheet).Range(range)

    def cell_isColumn(self, cell):
        '''
        Return True if the given 'cell' is a range of vertically aligned cells,
          false otherwise.
        '''
        col = False
        if (":" not in cell):
            return col
        else:
            i = 0
            while not cell[i].isdigit():
                i +=1
            if cell.count(cell[:i]) >1:
                col = True
        return col

    def set_cell_value(self, col, row, value=''):
        """
        Set the value of 'cell' to 'value'.
        """
        self.app.ActiveWorkbook.ActiveSheet.Cells(row,col).Value = value

    def set_value(self, cell, value=''):
        """
        Set the value of 'cell' to 'value'.
        'cell' can be a single cell ("A1"), a range of horizontal cells ("A1:C1") or a range of vertical cells ("A1:A3").
        'value' can be a string or a list.
        If 'value' is a string, it will be printed in each cell.
        If 'value' is a list, each list item will be printed in a cell until cells are exhausted.
        """
        if isinstance(value,list):
            if self.cell_isColumn(cell):
                for i, v in enumerate(value):
                    value[i] = [v]
        self.get_range(cell).Value = value

    def getName(self):
         """
         Get the full path file name of the active workbook after it has been saved.  
         """
         return self.app.ActiveWorkbook.Path + "/" + self.app.ActiveWorkbook.Name

    def get_row(self, rowNum, lastColumnLetter):
        """
        Get the values of 'row'.
        """
        rowRange = "A"+str(rowNum)+":"+lastColumnLetter+str(rowNum)
        return self.get_value( rowRange  )        

    def get_value(self, cell):
        """
        Get the value of 'cell'.
        If 'cell' is a single cell ("A1"), it returns a string.
        If 'cell is a range of horizontal cells ("A1:C1")
            or a range of vertical cells ("A1:A3"), it returns a list.
        """
        value = self.get_range(cell).Value
        if isinstance(value, tuple):
          v = []
          for item in value:
              for i in item:
                  v.append(i)
          value = v
        return value

    def set_border(self, range, side, line_style=borderSolid, color=colorBlack):
        """
        Set a border on the specified range of cells or single cell.
        'range' = range of cells or single cell
        'side' = one of borderTop, borderBottom, borderLeft, borderRight
        'line_style' = one of borderSolid, borderDashed, borderDotted, others?
        'color' = one of colorBlack, others?
        """
        range = self.get_range(range).Borders(side)
        range.LineStyle = line_style
        range.Color = color

    def sort(self, range, key_cell):
        """
        Sort the specified 'range' of the activeworksheet by the
        specified 'key_cell'.
        """
        range.Sort(Key1=self.get_range(key_cell), Order1=1, Header=0, OrderCustom=1, MatchCase=False, Orientation=1)

    def hide_row(self, row, hide=True):
        """
        Hide the specified 'row'.
        Specify hide=False to show the row.
        """
        self.get_range('a%s' % row).EntireRow.Hidden = hide

    def hide_column(self, column, hide=True):
        """
        Hide the specified 'column'.
        Specify hide=False to show the column.
        """
        self.get_range('%s1' % column).EntireColumn.Hidden = hide
     
    def delete_row(self, row, shift=directionUp):
        """
        Delete the entire 'row'.
        To delete row x, give 'row' as x, the row number
        To delete rows x through y, give 'row' as Ax:Ay
        """
        self.get_range('a%s' % row).EntireRow.Delete(Shift=shift)

    def delete_column(self, column, shift=directionLeft):
       """
       Delete the entire 'column'.
       To delete column x, give 'column' as x, the column letter
       Only deletes one column at a time.
       """
       self.get_range('%s1' % column).EntireColumn.Delete(Shift=shift)
       
    def fit_column(self, column):
       """
       Resize the specified 'column' to fit all its contents.
       """
       self.get_range('%s1' % column).EntireColumn.AutoFit()
     
    def save(self):
         """
         Save the active workbook.
         """
         self.app.ActiveWorkbook.Save()         


    def save_as(self, filename, delete_existing=False):
        """
        Save the active workbook as a different filename.
        If 'delete_existing' is specified and the file already
        exists, it will be deleted before saving.
        """
        if delete_existing and os.path.exists(filename):
            os.remove(filename)
        self.app.ActiveWorkbook.SaveAs(filename)
   
##    def print_out(self): #AttributeError: <unknown>.PrintOut
##        """
##        Print the active workbook.
##        """
##        self.app.Application.PrintOut()
   
    def close(self):
        """
        Close the active workbook.
        """
        self.app.ActiveWorkbook.Close()
   
    def quit(self):
        """
        Quit Excel.
        """
        return self.app.Quit()

if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    exObj = ExcelDocument(True)
    exObj.open(filename)
    exObj.close()
    exObj.quit()
    
