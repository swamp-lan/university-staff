from wxPython.wx import *
from wxPython.lib.rcsizer import RowColSizer

class MainWin(wxFrame):
	def __init__(self, parent, id, title):
		wxFrame.__init__(self,parent,-4, title, size = ( 400,400), style=wxDEFAULT_FRAME_STYLE|wxNO_FULL_REPAINT_ON_RESIZE)
		self.panel = wxPanel(self, -1)

		self.box = wxStaticBox(self.panel, -1, "Filter", pos = (5,5), size = (250, 80))


		sizer = RowColSizer()

		self.comp_text = wxTextCtrl(self.box, 100, "", size=(70, -1))
		sizer.Add(wxStaticText(self.box, -1, "Computer", style=wxALIGN_RIGHT), pos=(1,2), flag=wxALIGN_BOTTOM)
		sizer.Add(self.comp_text, pos=(2,2))

		sizer.Add(wxStaticText(self.box, -1, "Room", style=wxALIGN_RIGHT), pos=(1,3), flag=wxALIGN_BOTTOM)
		sizer.Add(wxTextCtrl(self.box, -1, "", size=(30, -1)), pos=(2,3))

		#l2 = wxStaticText(self.box, -1, "Room", pos=(10,50), size=(50, -1), style=wxALIGN_RIGHT)
		#t3 = wxTextCtrl(self.box, -1, "", pos= (65,47), size=(30, -1))

		
		#sizer.AddSpacer(120,10, pos=(1,1))
		sizer.Add(wxButton(self.box,  -1, "match", size=(60,21)), pos=(2,4))


		#self.lb1 = wxListBox(self.panel, 60, size=(80, 120), style=wxLB_SINGLE&wxLB_SORT, choices=['necropol-pc', 'night-pc'])
		#sizer.Add(self.lb1, pos=(4,2), colspan=2)

		self.box1 = wxStaticBox(self.panel, -1, "Result", pos = (5,90), size = (250, 130))


		self.list = wxListCtrl(self.panel, 80, size = (180, 100), style=wxLC_REPORT)
		sizer.Add(self.list, pos=(5,2), colspan=15)


		self.list.InsertColumn(1, "name")
		self.list.InsertColumn(2, "room")

		self.list.InsertStringItem(0, "1")
		self.list.SetStringItem(0, 0, "necropol-pc")
		self.list.SetStringItem(0, 1, "05-217")

		self.list.InsertStringItem(1, "2")
		self.list.SetStringItem(1, 0, "night-pc")
		self.list.SetStringItem(1, 1, "05-219")


		self.list.SetColumnWidth(0, wxLIST_AUTOSIZE)
		self.list.SetColumnWidth(1, wxLIST_AUTOSIZE)



		EVT_TEXT_ENTER(self, 100, self.texproc)
		#EVT_KEY_DOWN(self.comp_text, self.tabproc)
		EVT_LISTBOX_DCLICK(self, 60, self.listproc)
		self.panel.SetSizer(sizer)
		self.panel.SetAutoLayout(true)

		print self.list.GetItem(0, 1).GetText()

		self.Show(1)

	def texproc(self, a):
		print "sdf"
		

	def tabproc(self, a):
		print "tab"

	def listproc(self, a):
		print self.lb1.GetString(self.lb1.GetSelection())



	def OnFileExit(self):
		pass


app = wxPySimpleApp()

frame = MainWin(None, -1, "Test app 1")
app.MainLoop()


