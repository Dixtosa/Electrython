#!/usr/local/bin/python
# -*- coding: latin-1 -*-

#Girl Or Boy Lib About

import wx
import time
from _Info import *

class ABOUT_PROGRAMMERS(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1, "About", wx.DefaultPosition, wx.Size(600, 600),style=wx.CLIP_CHILDREN)
		panel=wx.Panel(self,-1,(0,0),wx.Size(600,600))
		panel_color=panel.GetBackgroundColour()
		l=5
		self.Centre()
		self.Show()
		for i in range(1080/l):
			j=i*l
			LP=wx.StaticText(panel,-1,"Lead Programmer:",pos=(250,500-(j-l)))
			LP.SetForegroundColour(panel_color)
			LP.SetFont(wx.Font(8, wx.NORMAL, wx.ITALIC, wx.NORMAL))
			
			LP_D=wx.StaticText(panel,-1," Dixtosa",pos=(250,525-(j-l)))
			LP_D.SetForegroundColour(panel_color)
			LP_D.SetFont(wx.Font(8, wx.NORMAL, wx.NORMAL, wx.NORMAL))
			
			HP=wx.StaticText(panel,-1,"Helper Programmer:",pos=(250,600-(j-l)))
			HP.SetForegroundColour(panel_color)
			HP.SetFont(wx.Font(8, wx.NORMAL, wx.ITALIC, wx.NORMAL))
			
			HP_DN=wx.StaticText(panel,-1," Doesn't Need;)",pos=(250,625-(j-l)))
			HP_DN.SetForegroundColour(panel_color)
			HP_DN.SetFont(wx.Font(8, wx.NORMAL, wx.NORMAL, wx.NORMAL))
			
			L=wx.StaticText(panel,-1,"Dixtosa © 2009",pos=(270,1100-(j-l)))
			L.SetForegroundColour(panel_color)
			L.SetFont(wx.Font(8, wx.NORMAL, wx.NORMAL, wx.NORMAL))
			
			
			wx.StaticText(panel,-1,"Lead Programmer:",pos=(250,500-j)).SetFont(wx.Font(8, wx.NORMAL, wx.ITALIC, wx.NORMAL))
			wx.StaticText(panel,-1," Dixtosa",pos=(250,525-j)).SetFont(wx.Font(8, wx.NORMAL, wx.NORMAL, wx.NORMAL))
			wx.StaticText(panel,-1,"Helper Programmer:",pos=(250,600-j)).SetFont(wx.Font(8, wx.NORMAL, wx.ITALIC, wx.NORMAL))
			wx.StaticText(panel,-1," Doesn't Need;)",pos=(250,625-j)).SetFont(wx.Font(8, wx.NORMAL, wx.NORMAL, wx.NORMAL))
			wx.StaticText(panel,-1,"Dixtosa © 2009",pos=(270,1100-j)).SetFont(wx.Font(8, wx.NORMAL, wx.NORMAL, wx.NORMAL))
			if i==(1080/l-1):
				time.sleep(2)
				self.Close()
class ABOUT_PROGRAMM:
	def __init__(self):
		info = wx.AboutDialogInfo()
		info.Name = Full_Name
		info.Version = Version
		info.Copyright = Copyright
		info.Description =Description
		info.WebSite = ("http://www.Dixtosa.wordpress.com", "My site")
		info.Developers = Developers
		info.License = License
		wx.AboutBox(info)