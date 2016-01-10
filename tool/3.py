from wxPython.wx import *
from wxPython.lib.rcsizer import RowColSizer
import MySQLdb


class LabeledEdit:
	def __init__(self, parent, id=-1, label="", pos=0, LSize=0, ESize=0):
		self.space = 10
		vert_offset = 2
		if not LSize:
			LSize = (60, 20)
		if not ESize:
			ESize = (90, 20)

		LPos = (pos[0], pos[1] + vert_offset)
		EPos = (pos[0] + LSize[0] + self.space, pos[1])
		self.label = wxStaticText(parent, -1, label, pos = LPos, size=LSize, style = wxALIGN_RIGHT)
		self.edit = wxTextCtrl(parent, id, "", pos = EPos, size=ESize)


class MainWin(wxFrame):
	def __init__(self, parent, id, title):
		wxFrame.__init__(self,parent,-4, title, size = ( 600,400), style=wxDEFAULT_FRAME_STYLE|wxNO_FULL_REPAINT_ON_RESIZE)
		self.panel = wxPanel(self, -1)

		self.db = MySQLdb.connect('localhost', 'root', '', 'bablo')
		self.cur = self.db.cursor()
		self.cur_ws_id = 0

		self.box = wxStaticBox(self.panel, -1, "Filter", pos = (5,5), size = (250, 80))


		sizer = RowColSizer()

		self.comp_text = wxTextCtrl(self.box, 100, "", size=(70, -1))
		sizer.Add(wxStaticText(self.box, -1, "Computer:", style=wxALIGN_RIGHT), pos=(1,1))
		sizer.Add(self.comp_text, pos=(1,2))

		self.room_text = wxTextCtrl(self.box, 101, "", size=(30, -1))
		sizer.Add(wxStaticText(self.box, -1, "Location:", style=wxALIGN_RIGHT), pos=(2,1))
		sizer.Add(self.room_text, pos=(2,2))

		#l2 = wxStaticText(self.box, -1, "Room", pos=(10,50), size=(50, -1), style=wxALIGN_RIGHT)
		#t3 = wxTextCtrl(self.box, -1, "", pos= (65,47), size=(30, -1))

		
		#sizer.AddSpacer(120,10, pos=(1,1))
		sizer.Add(wxButton(self.box,  -1, "match", size=(60,21)), pos=(1,3))


		#self.lb1 = wxListBox(self.panel, 60, size=(80, 120), style=wxLB_SINGLE&wxLB_SORT, choices=['necropol-pc', 'night-pc'])
		#sizer.Add(self.lb1, pos=(4,2), colspan=2)

		self.box1 = wxStaticBox(self.panel, -1, "Result", pos = (5,90), size = (250, 130))


		self.list = wxListCtrl(self.panel, 80, size = (180, 100), style=wxLC_REPORT)
		self.list.SetBackgroundColour(wxColour(255, 255, 255))
		sizer.Add(self.list, pos=(5,1), colspan=2)

		sizer.Add(wxButton(self.box1,  -1, "select", size=(60,21)), pos=(1,3), flag=wxALIGN_TOP)


		self.list.InsertColumn(1, "name")
		self.list.InsertColumn(2, "room")


		self.list.InsertStringItem(0, "1")
		self.list.SetStringItem(0, 0, "necropol-pc")
		self.list.SetStringItem(0, 1, "05-217")

		self.list.InsertStringItem(1, "2")
		self.list.SetStringItem(1, 0, "night-pc")
		self.list.SetStringItem(1, 1, "05-219")


		self.list.SetColumnWidth(0, 100)
		self.list.SetColumnWidth(1, wxLIST_AUTOSIZE)


		EVT_LIST_ITEM_SELECTED(self, 80, self.item_select)
		EVT_LIST_ITEM_ACTIVATED(self, 80, self.item_activated) 
		EVT_TEXT_ENTER(self, 100, self.texproc)
		EVT_TEXT_ENTER(self, 101, self.texproc)

		EVT_TEXT_ENTER(self, 110, self.add_ws)
		EVT_TEXT_ENTER(self, 111, self.add_ws)

		EVT_TEXT_ENTER(self, 220, self.payment)

		#EVT_KEY_DOWN(self.comp_text, self.tabproc)
		EVT_LISTBOX_DCLICK(self, 60, self.listproc)
		self.panel.SetSizer(sizer)
		self.panel.SetAutoLayout(true)


		print self.list.GetItem(0, 1).GetText()

		sizer.AddSpacer(75,-1, pos=(1,2))

		
		LabeledEdit(self.panel, -1, "Name", pos = (300,10))
		LabeledEdit(self.panel, -1, "Room", pos = (300,30))
		wxButton(self.panel,  -1, "Locations", size=(60,18), pos =(470, 30))

		LabeledEdit(self.panel, -1, "Nick", pos = (300,50))
		wxButton(self.panel,  -1, "Go to User", size=(70,18), pos =(470, 50))

		LabeledEdit(self.panel, -1, "Balanse", pos = (300,70))
		wxButton(self.panel,  -1, "Pay story", size=(60,18), pos =(470, 70))

		LabeledEdit(self.panel, -1, "IP Address", pos = (300,90))
		wxButton(self.panel,  -1, "Address history", size=(110,18), pos =(470, 90))

		wxCheckBox(self.panel,-1, "Я трезвый", pos =(470, 300))

		self.pay_box = wxStaticBox(self.panel, -1, "Balance", pos = (300,120), size = (250, 100))

		self.current = LabeledEdit(self.panel, -1, "current #", pos = (300,140))
		self.dolg = LabeledEdit(self.panel, -1, "dolg #", pos = (300,160))

		self.pay = LabeledEdit(self.panel, 220, "pay sum #", pos = (300,180))
		wxButton(self.panel,  -1, "yo", size=(30,18), pos =(470, 180))




		self.add_box = wxStaticBox(self.panel, -1, "add new", pos = (5,230), size = (250, 130))	
		self.new_name = LabeledEdit(self.panel, 110, "name", pos = (5,250))
		self.new_room = LabeledEdit(self.panel, 111, "room", pos = (5,270))
		wxButton(self.panel,  -1, "add", size=(30,18), pos =(180, 270))


		self.Show(1)

	def texproc(self, a):
		self.list.DeleteAllItems()
		name_value = self.comp_text.GetValue()
		room_value = self.room_text.GetValue()
		if room_value == '':
			query = "select * from ws where ws_name like '%s%%'" % (name_value)
		else:
			query = "select * from ws where ws_name like '%s%%' and ws_room = '%s'" % (name_value, room_value)

		print query
		self.cur.execute(query)
		i = 0
		present = 0
		for res in self.cur.fetchall():
			present = 1
			self.list.InsertStringItem(i, "1")
			self.list.SetStringItem(i, 0, str(res[1]).lower())
			self.list.SetStringItem(i, 1, str(res[3]))
			self.list.SetItemData(i, res[0])
			i += 1
			#self.comp_text.SetValue("")
			#self.room_text.SetValue("")

		if not present:
			print "not found"


		self.comp_text.SetFocus()
		self.room_text.SetSelection(-1, -1)
		self.comp_text.SetSelection(-1, -1)


	def item_select(self, a):
		print "dfg"

	def item_activated(self, a):
		self.cur_ws_id = self.list.GetItem(a.GetIndex()).GetData()
		self.get_balance(self.cur_ws_id)

	def tabproc(self, a):
		print "tab"

	def listproc(self, a):
		print self.lb1.GetString(self.lb1.GetSelection())


	def add_ws(self, a):
		print "adding ws"
		if self.new_name.edit.GetValue() and self.new_room.edit.GetValue():
			new_name = self.new_name.edit.GetValue()
			new_room = self.new_room.edit.GetValue()
			query = "insert into ws (ws_name, ws_corp, ws_room) values ('%s', 5, %s)" % (self.new_name.edit.GetValue(), self.new_room.edit.GetValue())
			self.cur.execute(query)
			self.new_room.edit.SetValue("")
			self.new_name.edit.SetValue("")
		else:
			print "Blocked"

	def OnFileExit(self):
		pass


	def payment(self, a):
		if self.cur_ws_id:
			pay = self.pay.edit.GetValue()
			self.pay.edit.SetValue("")
			query = "insert into money_trans (ws_id, t_time, t_size) values (%s, NOW(), %s)" % (self.cur_ws_id, pay)
			self.cur.execute(query)
			self.get_balance(self.cur_ws_id)
			self.cur_ws_id = 0
			print "%s payed" % (pay)
		else:
			print "Blocked"

		self.comp_text.SetFocus()
		self.comp_text.SetSelection(-1, -1)

#========================================

	def get_balance(self, ws_id):
		query = "select sum(t_size) from money_trans where ws_id = %s" % (ws_id)
		self.cur.execute(query)
		total = self.cur.fetchall()[0][0]
		if not total:
			total = 0

		OLD_TAX = 50
		NEW_TAX = 100
		OLD_M = 6
		NEW_M = 1
		MUST = ((OLD_TAX * OLD_M))# + (NEW_TAX * NEW_M))

		balance =  total - MUST
		if balance <= 0:
			dolg = MUST - total
		else:
			dolg = 0

		self.current.edit.SetValue(str(balance))
		self.dolg.edit.SetValue(str(dolg))
		return balance
#========================================


app = wxPySimpleApp()

frame = MainWin(None, -1, "Money flow v2.018")
app.MainLoop()



