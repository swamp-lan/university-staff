import time

t1 = time.time()

from wxPython.wx import *


print time.time() - t1

def yo():
	app.ExitMainLoop()


class MainWin(wxFrame):
	def __init__(self, parent, id, title):
		wxFrame.__init__(self,parent,-4, title, size = ( 620,400), style=wxDEFAULT_FRAME_STYLE|wxNO_FULL_REPAINT_ON_RESIZE)


		self.mainmenu = wxMenuBar()
		menu = wxMenu()
		exitID = wxNewId()
		menu.Append(exitID, 'E&xit\tAlt-X', 'Get the heck outta here!')
		self.mainmenu.Append(menu, '&File')
		self.SetMenuBar(self.mainmenu)

		self.CreateStatusBar(1, wxST_SIZEGRIP)

		self.splitter = wxSplitterWindow(self, -1, style=wxNO_3D|wxSP_3D)

		self.panel = wxPanel(self.splitter, -1)
		self.panel2 = wxPanel(self.splitter, -1)


		self.splitter.SplitVertically(self.panel, self.panel2)
#		self.splitter.SetSashPosition(200, false)
		self.splitter.SetMinimumPaneSize(10)

		self.Show(1)
	
	def OnFileExit(self):
		pass


app = wxPySimpleApp()
frame = MainWin(None, -1, "Network Managment")
app.MainLoop()


