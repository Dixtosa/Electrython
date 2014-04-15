# --encoding=utf-8

from Electrons import *
from popup import *

import wx
import math


class Electrython(wx.Frame):
	RADIUS = 15
	ZOOM = 0.001
	DELTA_ON_FIELD_LINES = 10
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title,(0,0), wx.Size(1024, 768))
		self.p1=wx.Panel(self,-1,(0,0),wx.Size(800,1000))
		self.p2=wx.Panel(self,-1,(800,0),wx.Size(1000,1000))
		
		self.f10=wx.Font(10,wx.FONTFAMILY_DEFAULT,wx.NORMAL,wx.NORMAL,face="AcadNusx")
		self.Objects()
		self.Binding()
		self.MenuBar()

		self.context = Plane(self.RADIUS)

	def Binding(self):
		self.p1.Bind(wx.EVT_PAINT, self.on_paint)
		#MOUSE EVENT BIND START#
		self.p1.Bind(wx.EVT_LEFT_DOWN, self.DownL)
		self.p1.Bind(wx.EVT_LEFT_UP, self.Up)
		#MOUSE EVENT BIND END#
		
		self.p1.Bind(wx.EVT_RIGHT_DOWN, self.DownR)
		
		self.Bind(wx.EVT_MENU, self.about, id=57)

		self.showPointsCheckBox.Bind(wx.EVT_CHECKBOX,self.refreshClicked)
		self.showAllVectorsCheckBox.Bind(wx.EVT_CHECKBOX,self.refreshClicked)
		self.showAddedVectorsCheckBox.Bind(wx.EVT_CHECKBOX,self.refreshClicked)
		self.showFieldCheckBox.Bind(wx.EVT_CHECKBOX,self.refreshClicked)
	def DownR(self,evt):
		self.PopupMenu(MyPopupMenu(self, evt.GetPosition(), self.txt_1))
	def MenuBar(self):
		menu_bar=wx.MenuBar()
		file_menu = wx.Menu()
		file_menu.Append(57, "About")
		menu_bar.Append(file_menu,"&About")
		self.SetMenuBar(menu_bar)
	def Objects(self):
		self.txt_1 = wx.TextCtrl(self.p2,-1,"+1",(0,1),wx.Size(150,20))
		wx.Button(self.p2, wx.ID_ANY, u"მიახლოება",(0,150),wx.Size(215,50))\
			.Bind(wx.EVT_BUTTON, self.zoom_in)
		wx.Button(self.p2, wx.ID_ANY, u"განახლოება :D",(0,200), wx.Size(215,50))\
			.Bind(wx.EVT_BUTTON, self.zoom_out)
		wx.Button(self.p2, wx.ID_ANY, u"ყველაფრის წაშლა",(0,250),wx.Size(215,50))\
			.Bind(wx.EVT_BUTTON, self.clearClicked)
		wx.Button(self.p2, wx.ID_ANY, u"განახლება", (0,300), wx.Size(215,50))\
			.Bind(wx.EVT_BUTTON, self.refreshClicked)
		
		self.showPointsCheckBox=wx.CheckBox(self.p2,wx.ID_ANY, u"მაჩვენე მუხტები",(0,40))
		self.showPointsCheckBox.SetValue(True)
		self.showAllVectorsCheckBox=wx.CheckBox(self.p2,wx.ID_ANY,"Show All Vectors",(0,55))
		self.showAllVectorsCheckBox.SetValue(True)
		self.showAddedVectorsCheckBox=wx.CheckBox(self.p2,wx.ID_ANY,"Show Only Added Vectors",(0,70))
		self.showAddedVectorsCheckBox.SetValue(True)
		self.showFieldCheckBox=wx.CheckBox(self.p2,wx.ID_ANY, u"ძალწირების ჩვენება",(0,85))
		self.showFieldCheckBox.SetValue(True)
	def zoom_in(self,evt):
		self.ZOOM *= 2
		self.p1.Refresh()
	def zoom_out(self,evt):
		self.ZOOM /= 2
		self.p1.Refresh()
	def DownL(self,event):
		UP = True
		self.MOUSE_EVENT_LIST=[]
		self.MOUSE_EVENT_LIST.append(event.GetPosition())
		"""
		myCursor= wx.Cursor(r"C:\WINDOWS\Cursors\3dgarro.cur",
					wx.BITMAP_TYPE_CUR)
		self.SetCursor(myCursor)"""
		self.p1.SetCursor(wx.StockCursor(wx.CURSOR_HAND))
		self.p1.Refresh()

	def Up(self,event):
		self.p1.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
		self.dc.Clear()
		self.p1.Refresh()

	def clearClicked(self, event):
		self.dc.Clear()
		self.p1.Refresh()

	def refreshClicked(self, event):
		self.p1.Refresh()


	def update_drawing(self):
		self.dc.Clear()
		if self.showAllVectorsCheckBox.GetValue():
			self.drawAllVectors()
		if self.showAddedVectorsCheckBox.GetValue():
			self.drawAddedVectors()
		if self.showFieldCheckBox.GetValue():
			self.drawField()
		if self.showPointsCheckBox.GetValue():
			self.drawPoints()

	def drawPoints(self):
		for point in self.context.getPoints():
			x, y = point.x, point.y
			self.dc.SetPen(wx.Pen("BLACK"))
			self.dc.DrawCircle(x, y, self.RADIUS)
			self.dc.SetFont(wx.Font(22, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.NORMAL))
			self.dc.DrawText(str(point.charge), x-self.RADIUS/2, y-self.RADIUS)
	def drawAddedVectors(self):
		self.dc.SetPen(wx.Pen("RED", 1))
		points = self.context.getPoints()
		if (len(points) <= 1): return
		for point in points:
			x, y = point.x, point.y
			(forceX, forceY) = self.context.addedForcesOf(point)
			endx = x + self.ZOOM*forceX
			endy = y + self.ZOOM*forceY
			self.dc.DrawLine(x, y, endx, endy)
			self.__drawArrowsByEndpoints__(x, y, endx, endy, self.DELTA_ON_FIELD_LINES)

	def drawAllVectors(self):
		self.dc.SetPen(wx.Pen("BLACK", 1))
		for point in self.context.getPoints():
			x, y = point.x, point.y
			forces = self.context.forcesOf(point)
			for (forceX, forceY) in forces:
				endx=x + self.ZOOM*forceX
				endy=y + self.ZOOM*forceY
				self.dc.DrawLine(x, y, endx, endy)
				self.__drawArrowsByEndpoints__(x, y, endx, endy, self.DELTA_ON_FIELD_LINES)

	def drawField(self):
		self.dc.SetPen(wx.Pen("BLUE", 1))
		for point in self.context.getPoints():
			for j in range(4):
				x1, y1 = point.x, point.y
				
				if j==0:y1 += self.RADIUS
				if j==1:y1 -= self.RADIUS
				if j==2:x1 += self.RADIUS
				if j==3:x1 -= self.RADIUS

				x2, y2 = x1, y1
				N = 0

				while (0 < x2 < 800 and 0 < y2 < 800) and not bool(self.context.searchNearby(x2, y2)):
					x1, y1 = x2, y2

					#DUMB WAY!
					self.context.addPoint(x1, y1, 1)
					x2, y2 = self.context.addedForcesOf(Point(x1, y1, 1))
					self.context.removePoint(x1, y1)
					#DUMB WAY!

					(x2, y2) = self.__normalizeByMax__(x2, y2, self.DELTA_ON_FIELD_LINES)

					x2 += x1
					y2 += y1
					self.dc.DrawLine(x1, y1, x2, y2)
					N+=1
					if N % 15 == 0:
						self.__drawArrowsByEndpoints__(x1, y1, x2, y2, self.DELTA_ON_FIELD_LINES)

	def __drawArrowsByEndpoints__(self, x1, y1, x2, y2, Max):
		(deltax, deltay) = self.__normalizeByMax__(x2 - x1, y2 - y1, Max)
		
		x1 = x2 - deltax
		y1 = y2 - deltay

		leftVector = (-deltay, deltax)
		rightVector = (deltay, -deltax)
		startPoint = (x2, y2)
		endPoint = (x1 + leftVector[0], y1 + leftVector[1])
		self.dc.DrawLine(*(startPoint + endPoint))

		endPoint = (x1 + rightVector[0], y1 + rightVector[1])
		self.dc.DrawLine(*(startPoint + endPoint))
	def __normalizeByMax__(self, x, y, Max):
		r = math.hypot(x, y)
		factor = r / Max
		return (x/factor, y/factor)

	def on_paint(self, event):
		self.dc = wx.PaintDC(self.p1)
		self.dc.SetBackground(wx.Brush('#999033'))
		self.update_drawing()

	def about(self,event):
		info = wx.AboutDialogInfo()
		info.Name = "Electrython"
		info.Version = "v2.0"
		info.Description = "Description"
		info.WebSite = ("http://www.dixtosa.wordpress.com", u"ვებ გვერდი")
		info.Developers = ["Gio Eufshi aka Dixtosa aka Kioshimu Garakame aka Gautam Yolo"]
		wx.AboutBox(info)


app = wx.App() 
frame = Electrython(None, -1, "Electrython v 2.0")
frame.Centre()
frame.Show()
app.MainLoop()
