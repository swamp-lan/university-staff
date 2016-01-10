from wxPython.wx import *
from   wxPython.html import wxHtmlWindow

class MainWin(wxFrame):
	def __init__(self, parent, id, title):
		wxFrame.__init__(self,parent,-4, title, size = ( 200,100), style=wxDEFAULT_FRAME_STYLE|wxNO_FULL_REPAINT_ON_RESIZE)
		self.CreateStatusBar(1, wxST_SIZEGRIP)

		splitter = wxSplitterWindow(self, -1, style=wxSP_3DSASH|wxNO_3D)
		#splitter.SetWColour(wxNamedColour("Blue"))
		splitter2 = wxSplitterWindow(splitter, -1, style=wxNO_3D|wxSP_3D)
		def EmptyHandler(evt): pass
		EVT_ERASE_BACKGROUND(splitter, EmptyHandler)
		EVT_ERASE_BACKGROUND(splitter2, EmptyHandler)

		tID = wxNewId()
		self.treeMap = {}
		self.tree = wxTreeCtrl(splitter, tID,
							   style=wxTR_HAS_BUTTONS |
							   wxTR_EDIT_LABELS |
							   wxTR_HAS_VARIABLE_ROW_HEIGHT |
							   wxSUNKEN_BORDER)
		
		root = self.tree.AddRoot("Overview")
		child = self.tree.AppendItem(root, "Users")
		child = self.tree.AppendItem(root, "Computres")
		child = self.tree.AppendItem(root, "Network")
		child = self.tree.AppendItem(root, "Money Flow")
		child = self.tree.AppendItem(root, "Topology")
		self.tree.Expand(root)
		self.nb = wxNotebook(splitter2, -1, style=wxCLIP_CHILDREN)

		panel = wxPanel(self.nb, -1, style=wxCLIP_CHILDREN|wxNO_3D)
		#self.ovr = wxHtmlWindow(panel, -1, size=(400, 400))
		self.nb.AddPage(panel, "Overview")


		self.txt = wxTextCtrl(self.nb, -1,
							  style = wxTE_MULTILINE|wxTE_READONLY|wxHSCROLL)
		self.nb.AddPage(self.txt, "Demo Code")


		self.txt = wxTextCtrl(self.nb, -1,
							  style = wxTE_MULTILINE|wxTE_READONLY|wxHSCROLL)
		self.nb.AddPage(self.txt, "Demo Code")


		# Set up a log on the View Log Notebook page
		self.log = wxTextCtrl(splitter2, -1,
							  style = wxTE_MULTILINE|wxTE_READONLY|wxHSCROLL)
		# Set the wxWindows log target to be this textctrl
		#wxLog_SetActiveTarget(wxLogTextCtrl(self.log))
		



		

		# add the windows to the splitter and split it.
		splitter2.SplitHorizontally(self.nb, self.log)
		splitter2.SetSashPosition(50, true)
		splitter2.SetMinimumPaneSize(20)

		
		splitter.SplitVertically(self.tree, splitter2)
		splitter.SetSashPosition(80, true)
		splitter.SetMinimumPaneSize(20)


		# select initial items
		self.nb.SetSelection(0)
		self.tree.SelectItem(root)

		self.Show(1)






















app = wxPySimpleApp()
frame = MainWin(None, -1, "Sample editor")
app.MainLoop()