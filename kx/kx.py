from wxPython.wx         import *
from wxPython.lib.editor import wxEditor

#----------------------------------------------------------------------




class MyApp(wxApp):
	def OnInit(self):
		frame = wxFrame(NULL, -1, "Keks", wxDefaultPosition, wxSize(400,400))

		sc = wxScrolledWindow(frame)
		sc.SetScrollbars(10,10,10,10,0)
		button = wxButton(sc, -1, "sdf", wxDefaultPosition, wxSize(400,400))
		frame.Show(true)
		'''
		ed = wxEditor(frame, -1, style=wxSUNKEN_BORDER)
		box = wxBoxSizer(wxVERTICAL)
		box.Add(ed, 1, wxALL|wxGROW, 1)
		frame.SetSizer(box)
		frame.SetAutoLayout(true)

		ed.SetText(["",
					"This is a simple text editor, the class name is",
					"wxEditor.  Type a few lines and try it out.",
					"",
					"It uses Windows-style key commands that can be overriden by subclassing.",
					"Mouse select works. Here are the key commands:",
					"",
					"Cursor movement:     Arrow keys or mouse",
					"Beginning of line:   Home",
					"End of line:         End",
					"Beginning of buffer: Control-Home",
					"End of the buffer:   Control-End",
					"Select text:         Hold down Shift while moving the cursor",
					"Copy:                Control-Insert, Control-C",
					"Cut:                 Shift-Delete,   Control-X",
					"Paste:               Shift-Insert,   Control-V",
					""])

		'''
		#self.SetTopWindow(frame)
		return true



def runTest(frame, nb, log):
    win = wxPanel(nb, -1)
    ed = wxEditor(win, -1, style=wxSUNKEN_BORDER)
    box = wxBoxSizer(wxVERTICAL)
    box.Add(ed, 1, wxALL|wxGROW, 1)
    win.SetSizer(box)
    win.SetAutoLayout(true)


    return win

app = MyApp(0)
app.MainLoop()




#----------------------------------------------------------------------
