# --encoding=utf-8

import wx
class MyPopupMenu(wx.Menu):
	def __init__(self, frame, POS, textBox):
		wx.Menu.__init__(self)
		self.frame = frame
		self.txt = textBox
		self.x, self.y = POS

		if not self.frame.context.searchNearby(self.x, self.y):
			item = wx.MenuItem(self, wx.NewId(), u"დასვი მუხტი აქ")
			self.AppendItem(item)
			self.Bind(wx.EVT_MENU, self.add, item)
		else:
			item = wx.MenuItem(self, wx.NewId(), u"წაშალე მუხტი")
			self.AppendItem(item)
			self.Bind(wx.EVT_MENU, self.rem, item)
	def add(self, e):
		q = int(self.txt.GetValue())
		if self.frame.context.addPoint(self.x, self.y, q):
			self.frame.p1.Refresh()
			return True
		else:
			return False

	def rem(self, e):
		self.frame.context.removePoint(self.x, self.y)
		self.frame.p1.Refresh()