import wx
from _Info import *
import Electrons
import os
from math import *
###########################################################################################################.
zoom=100000
###########################################################################################################
def ln():
        return Electrons.lenP()
def clr():
        return Electrons.CLRp()
def rt():
        return Electrons.ret()
def IsIn(x,y,k=15):
        for l in rt():
                xx,yy=l[0]
                if xx-k<x<xx+k and yy-k<y<yy+k:
                        return l
        else:
                return False
def Arrows(x1,y1,x2,y2,muxti):
	dx=5-abs(x2-x1)
	dy=5-abs(y2-y1)
	if muxti==-1:
		xx1=x1+dx
		yy1=y1+dy
		xx2=x1-dx
		yy2=y1-dy
		return [xx1,yy1,x2,y2],[xx2,yy2,x2,y2]
		"""
		return arrow(x1,y1,x2,y2)"""
	else:
		xx1=x2+dx
		yy1=y2+dy
		xx2=x2-dx
		yy2=y2-dy
		return [xx1,yy1,x1,y1],[xx2,yy2,x1,y1]
		"""
		return arrow(x2,y2,x1,y1)
		"""
###########################################################################################################
def arrow(x1,y1,x2,y2):
	dx=x2-x1
	dy=y2-y1
	c=hypot(dx,dy)
	k=7
	al=radians(30)
	cos_a=cos(acos(dx/c)+al)
	sin_a=sin(asin(dy/c)+al)
	sin_b=sin(asin(dy/c)-al)
	cos_b=cos(acos(dx/c)-al)
	Y_a=k*sin_a
	X_a=k*cos_a
	Y_b=k*sin_b
	X_b=k*cos_b
	return [x2-X_a,y2-Y_a,x2,y2],[x2-X_b,y2-Y_b,x2,y2]
class MyPopupMenu(wx.Menu):
	def __init__(self, parnt,POS,txt):
		wx.Menu.__init__(self)
		self.parnt = parnt
		self.pos=POS
		self.txt=txt
		item = wx.MenuItem(self, wx.NewId(), "Point Here :)")
		self.AppendItem(item)
		self.Bind(wx.EVT_MENU, self.ad, item)
		item = wx.MenuItem(self, wx.NewId(),"Remove That")
		self.AppendItem(item)
		self.Bind(wx.EVT_MENU, self.re, item)
	def ad(self, e):
		pos,Q=self.textentry(self.pos)
		Electrons.addp([pos,Q])
		self.parnt.refresh()
	def re(self, e):
                p=IsIn(self.pos[0],self.pos[1],10)
                print "self.pos",self.pos
                if p:
                        Electrons.remp(p)
		self.parnt.refresh()
	def textentry(self,pos):
		Q=self.txt.GetValue()
		return [pos,float(Q)]
###########################################################################################################
class Electrython(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title,(0,0), wx.Size(1024, 768))
		self.p1=wx.Panel(self,-1,(0,0),wx.Size(800,1000))
		self.p2=wx.Panel(self,-1,(800,0),wx.Size(1000,1000))
		#START()
		self.f10=wx.Font(10,wx.FONTFAMILY_DEFAULT,wx.NORMAL,wx.NORMAL,face="AcadNusx")
		self.Objectz()
		self.Binding()
		self.MenuBar()
	def Binding(self):
		self.p1.Bind(wx.EVT_PAINT, self.on_paint)
		self.p2.Bind(wx.EVT_BUTTON, self.default_,id=77)
		self.p2.Bind(wx.EVT_BUTTON, self.Clear,id=11)
		#MOUSE EVENT BIND START#
		self.p1.Bind(wx.EVT_LEFT_DOWN, self.DownL)
		self.p1.Bind(wx.EVT_LEFT_UP, self.Up)
		#MOUSE EVENT BIND END#
		
		self.p1.Bind(wx.EVT_RIGHT_DOWN, self.DownR)
		
		self.Bind(wx.EVT_MENU, self.A_Programm, id=57)

		self.Refresh_BTN.Bind(wx.EVT_BUTTON,self.refresh__)
		self.show_points.Bind(wx.EVT_CHECKBOX,self.refresh__)
		self.show_all_vectors.Bind(wx.EVT_CHECKBOX,self.refresh__)
		self.show_added_vectors.Bind(wx.EVT_CHECKBOX,self.refresh__)
		self.show_forces.Bind(wx.EVT_CHECKBOX,self.refresh__)
	def DownR(self,evt):
		self.PopupMenu(MyPopupMenu(self, evt.GetPosition(),self.txt_1))
	def MenuBar(self):
		menu_bar=wx.MenuBar()
		file_menu = wx.Menu()
		file_menu.Append(57, "About")
		menu_bar.Append(file_menu,"&About")
		self.SetMenuBar(menu_bar)
	def Objectz(self):
		self.txt_1=wx.TextCtrl(self.p2,-1,"1",(0,1),wx.Size(150,20))
		wx.Button(self.p2,11,"zoom in",(0,150),wx.Size(215,50)).Bind(wx.EVT_BUTTON,self.zoom_in)
		wx.Button(self.p2,11,"zoom out",(0,200),wx.Size(215,50)).Bind(wx.EVT_BUTTON,self.zoom_out)
		wx.Button(self.p2,11,"yvelafris waSla",(0,250),wx.Size(215,50)).SetFont(self.f10)
		self.Refresh_BTN=wx.Button(self.p2,wx.ID_ANY,"ganaxleba",(0,300),wx.Size(215,50))
		self.Refresh_BTN.SetFont(self.f10)
		self.show_points=wx.CheckBox(self.p2,wx.ID_ANY,"Show Points",(0,40))
		self.show_points.SetValue(True)
		self.show_all_vectors=wx.CheckBox(self.p2,wx.ID_ANY,"Show All Vectors",(0,55))
		self.show_all_vectors.SetValue(True)
		self.show_added_vectors=wx.CheckBox(self.p2,wx.ID_ANY,"Show Only Added Vectors",(0,70))
		self.show_added_vectors.SetValue(True)
		self.show_forces=wx.CheckBox(self.p2,wx.ID_ANY,"Show Forces",(0,85))
	def zoom_out(self,evt):
		global zoom
		zoom*=2
		self.refresh()
	def zoom_in(self,evt):
		global zoom
		zoom/=2
		self.refresh()
	def default_(self,event):
		self.dc.Clear()
	def DownL(self,event):
		UP = True
		self.MOUSE_EVENT_LIST=[]
		self.MOUSE_EVENT_LIST.append(event.GetPosition())
		"""
		myCursor= wx.Cursor(r"C:\WINDOWS\Cursors\3dgarro.cur",
					wx.BITMAP_TYPE_CUR)
		self.SetCursor(myCursor)"""
		self.p1.SetCursor(wx.StockCursor(wx.CURSOR_HAND))
		self.refresh()
	def Up(self,event):
		self.p1.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
		self.dc.Clear()
		self.refresh()
	def Clear(self,event):
		self.dc.Clear()
		clr()
	def refresh__(self,event):
		self.refresh()
	def refresh(self):
		point_l=rt()
		self.dc.Clear()
		if self.show_points.GetValue():
                        self.draw_pointz(point_l)
		if self.show_forces.GetValue():
                        self.draw_dzalwirebi()

		if ln()!=1:
			Point_managed=Electrons.convert(point_l)
			VECz=Electrons.Vec_Add_All(Point_managed)
			
                        if self.show_all_vectors.GetValue():
                                self.Draw_All_Vecs(Point_managed)
                        if self.show_added_vectors.GetValue():
                                self.Draw_Added_Vecs(VECz)
	def Draw_All_Vecs(self,Point_Managed):
		global zoom
		self.dc.SetPen(wx.Pen("black"))
		for a in Point_Managed:
			x1,y1=a[0][0]
			for b in a[1]:
				x2,y2=b[1]
				ans1,ans2=arrow(x1,y1,x1+(x2-x1)/zoom,y1+(y2-y1)/zoom)
				self.dc.DrawLine(*ans1)
				self.dc.DrawLine(*ans2)
				self.dc.DrawLine(x1,y1,x1+(x2-x1)/zoom,y1+(y2-y1)/zoom)
	def draw_pointz(self,point_l):
		for a in point_l:
			mx,my=a[0]
			Q=a[1]
			self.dc.SetPen(wx.Pen("BLACK"))
			self.dc.DrawCircle(mx,my,15)
			self.dc.DrawText(str(Q),mx-12,my-8)
	def draw_dzalwirebi(self):
		K=15
		muxti=1
		points=rt()
		for i in points:
			for j in range(4):
				x1,y1=i[0]
				muxti__=i[1]
				x2,y2=1,1
				if j==0:
					y1+=K
				if j==1:
					y1-=K
				elif j==2:
					x1+=K
				elif j==3:
					x1-=K
				N=0
				while (0<x2<800 and 0<y2<800) and not (bool(IsIn(x2,y2))&(N>1)):
					if muxti__>0:
						muxti=-1
					else:
						muxti=1                         
					if N!=0:
						x1,y1=x2,y2
					x2,y2=Electrons.addp_dzalw([[x1,y1],muxti])
					dx=float(x1-x2)
					dy=y1-y2
					r=sqrt(dx**2+dy**2)
					zooming=r/5
					dx/=zooming
					dy/=zooming
					x2,y2=x1+dx,y1+dy
					if (N%8==0) & (N>=8):
                                                I_1,I_2=Arrows(x1,y1,x2,y2,muxti)
                                                self.dc.DrawLine(*I_1)
                                                self.dc.DrawLine(*I_2)
                                        self.dc.SetPen(wx.Pen("#"+str(hex(1000*N))))
					self.dc.DrawLine(x1,y1,x2,y2)
					N+=1
	def Draw_Added_Vecs(self,mngd):
		global zoom
		self.dc.SetPen(wx.Pen("RED"))
		for a in mngd:
			x1,y1=a[0]
			x2,y2=a[1]
			ans1,ans2=arrow(x1,y1,x1+(x2-x1)/zoom,y1+(y2-y1)/zoom)
			self.dc.DrawLine(*ans1)
			self.dc.DrawLine(*ans2)
			self.dc.DrawLine(x1,y1,x1+(x2-x1)/zoom,y1+(y2-y1)/zoom)
	def on_paint(self, event):
		self.dc = wx.PaintDC(self.p1)
		self.dc.SetBackground(wx.Brush('#FF9033'))
		self.refresh()
		event.Skip()
	def A_Programmers(self,event):
		import About
		About.ABOUT_PROGRAMMERS()
	def A_Programm(self,event):
		import About
		About.ABOUT_PROGRAMM()


app = wx.PySimpleApp() 
FRAME = Electrython(None,-1,Name+" v"+Version)
FRAME.Centre()
FRAME.Show()
app.MainLoop()
