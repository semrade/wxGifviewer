# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.animate

###########################################################################
## Class frameMain
###########################################################################

class frameMain ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"My gif Viewer", pos = wx.DefaultPosition, size = wx.Size( 923,636 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizerFrame = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panelMain = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizerPanel = wx.BoxSizer( wx.VERTICAL )
		
		bSizerPanelMain = wx.BoxSizer( wx.VERTICAL )
		
		bSizerDir = wx.BoxSizer( wx.VERTICAL )
		
		bSizerDirHor = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizerDir = wx.StaticBoxSizer( wx.StaticBox( self.m_panelMain, wx.ID_ANY, u"Gif Directory\n" ), wx.VERTICAL )
		
		self.m_dirPickerDir = wx.DirPickerCtrl( sbSizerDir.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		sbSizerDir.Add( self.m_dirPickerDir, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizerDirHor.Add( sbSizerDir, 1, wx.ALL|wx.BOTTOM, 5 )
		
		
		bSizerDir.Add( bSizerDirHor, 1, wx.ALL|wx.EXPAND, 0 )
		
		
		bSizerPanelMain.Add( bSizerDir, 0, wx.EXPAND, 0 )
		
		bSizerSplit = wx.BoxSizer( wx.VERTICAL )
		
		bSizerSplitHor = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizerListBox = wx.BoxSizer( wx.VERTICAL )
		
		bSizeGifile = wx.BoxSizer( wx.VERTICAL )
		
		m_listBoxGifileChoices = []
		self.m_listBoxGifile = wx.ListBox( self.m_panelMain, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), m_listBoxGifileChoices, 0 )
		bSizeGifile.Add( self.m_listBoxGifile, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizerListBox.Add( bSizeGifile, 1, wx.EXPAND, 5 )
		
		
		bSizerSplitHor.Add( bSizerListBox, 1, wx.EXPAND, 0 )
		
		m_animCtriGifs = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_animCtrl1 = wx.animate.AnimationCtrl( self.m_panelMain, wx.ID_ANY, wx.animate.NullAnimation, wx.DefaultPosition, wx.DefaultSize, wx.animate.AC_DEFAULT_STYLE ) 
		m_animCtriGifs.Add( self.m_animCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizerSplitHor.Add( m_animCtriGifs, 1, wx.EXPAND, 5 )
		
		
		bSizerSplit.Add( bSizerSplitHor, 1, wx.EXPAND, 0 )
		
		
		bSizerPanelMain.Add( bSizerSplit, 1, wx.EXPAND, 0 )
		
		
		bSizerPanel.Add( bSizerPanelMain, 1, wx.EXPAND, 0 )
		
		
		self.m_panelMain.SetSizer( bSizerPanel )
		self.m_panelMain.Layout()
		bSizerPanel.Fit( self.m_panelMain )
		bSizerFrame.Add( self.m_panelMain, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		self.SetSizer( bSizerFrame )
		self.Layout()
		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem1 )
		
		self.m_menubar2.Append( self.m_menu1, u"File" ) 
		
		self.Edit = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.Edit, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.Edit.AppendItem( self.m_menuItem2 )
		
		self.m_menubar2.Append( self.Edit, u"Edit" ) 
		
		self.m_menu3 = wx.Menu()
		self.m_menu21 = wx.Menu()
		self.m_menu3.AppendSubMenu( self.m_menu21, u"MyMenu" )
		
		self.m_menu3.AppendSeparator()
		
		self.m_menubar2.Append( self.m_menu3, u"View" ) 
		
		self.SetMenuBar( self.m_menubar2 )
		
		self.m_statusBar6 = self.CreateStatusBar( 1, 0, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_dirPickerDir.Bind( wx.EVT_DIRPICKER_CHANGED, self.dirPickerDirOnDirChanged )
		self.m_listBoxGifile.Bind( wx.EVT_LISTBOX, self.m_listBoxGifileOnListBox )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def dirPickerDirOnDirChanged( self, event ):
		event.Skip()
	
	def m_listBoxGifileOnListBox( self, event ):
		event.Skip()
	

