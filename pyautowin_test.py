#from pywinauto.application import Application
#
#app = Application().start("C:\IMD_data_converter_25\converter2.exe", wait_for_idle=False)
#
#dlg_spec = app.IMDDataConverter
#actionable_dlg = dlg_spec.wait('visible')
########################################################################
#from pywinauto import Desktop, Application
#
#Application().start('explorer.exe "C:\\Program Files"')
#
## connect to another process spawned by explorer.exe
## Note: make sure the script is running as Administrator!
#app = Application(backend="uia").connect(path="explorer.exe", title="Program Files")
#
#app.ProgramFiles.set_focus()
#common_files = app.ProgramFiles.ItemsView.get_item('Common Files')
#common_files.right_click_input()
#app.ContextMenu.Properties.invoke()
#
#
#Properties = Desktop(backend='uia').Common_Files_Properties
#Properties.print_control_identifiers()
##Properties.Cancel.click()
##Properties.wait_not('visible') # make sure the dialog is closed
########################################################################
from pywinauto import Desktop, Application

infile = 'input file'
outfile = 'output file'

Application().start("C:\IMD_data_converter_25\converter2.exe", wait_for_idle=False)

app = Application(backend="uia").connect(path="C:\IMD_data_converter_25\converter2.exe", title="IMD Data Converter")

app.IMDDataConverter.set_focus()

Properties = Desktop(backend='uia').IMDDataConverter

Properties.print_control_identifiers()

#print(Properties.Custom1.print_control_identifiers())
Properties.Custom15.click_input()

Properties.Custom3.click_input()
Properties.Custom3.type_keys(infile)

Properties.Custom1.click_input()
Properties.Custom1.type_keys(outfile)

Properties.Custom9.click_input()


#from pywinauto.application import Application
#app = Application().start("notepad.exe")
#
#app.UntitledNotepad.menu_select("Help->About Notepad")
#app.AboutNotepad.OK.click()
#app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)