# gifviewer.py

import wx
import wx.adv


class frameMain ( wx.Frame ):
    
    def __init__( self ):
        wx.Frame.__init__ ( self, None, id = wx.ID_ANY, title = u"My gif Viewer", pos = wx.DefaultPosition, size = wx.Size( 923,636 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizerFrame = wx.BoxSizer( wx.VERTICAL )
        
        self.panelMain = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizerPanel = wx.BoxSizer( wx.VERTICAL )
        
        bSizerPanelMain = wx.BoxSizer( wx.VERTICAL )
        
        bSizerDir = wx.BoxSizer( wx.VERTICAL )
        
        bSizerDirHor = wx.BoxSizer( wx.HORIZONTAL )
        
        sbSizerDir = wx.StaticBoxSizer( wx.StaticBox( self.panelMain, wx.ID_ANY, u"Gif Directory\n" ), wx.VERTICAL )
        
        self.dirPickerDir = wx.DirPickerCtrl( sbSizerDir.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
        sbSizerDir.Add( self.dirPickerDir, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizerDirHor.Add( sbSizerDir, 1, wx.ALL|wx.BOTTOM, 5 )
        
        
        bSizerDir.Add( bSizerDirHor, 1, wx.ALL|wx.EXPAND, 0 )
        
        
        bSizerPanelMain.Add( bSizerDir, 0, wx.EXPAND, 0 )
        
        bSizerSplit = wx.BoxSizer( wx.VERTICAL )
        
        bSizerSplitHor = wx.BoxSizer( wx.HORIZONTAL )
        
        bSizerListBox = wx.BoxSizer( wx.VERTICAL )
        
        bSizeGifile = wx.BoxSizer( wx.VERTICAL )
        
        listBoxGifileChoices = []
        self.listBoxGifile = wx.ListBox( self.panelMain, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), listBoxGifileChoices, 0 )
        bSizeGifile.Add( self.listBoxGifile, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizerListBox.Add( bSizeGifile, 1, wx.EXPAND, 5 )
        
        
        bSizerSplitHor.Add( bSizerListBox, 1, wx.EXPAND, 0 )
        
        animCtriGifs = wx.BoxSizer( wx.HORIZONTAL )
        
        self.animCtrl1 = wx.adv.AnimationCtrl( self.panelMain, wx.ID_ANY, wx.adv.NullAnimation, wx.DefaultPosition, wx.DefaultSize, wx.adv.AC_DEFAULT_STYLE ) 
        animCtriGifs.Add( self.animCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizerSplitHor.Add( animCtriGifs, 1, wx.EXPAND, 5 )
        
        
        bSizerSplit.Add( bSizerSplitHor, 1, wx.EXPAND, 0 )
        
        
        bSizerPanelMain.Add( bSizerSplit, 1, wx.EXPAND, 0 )
        
        
        bSizerPanel.Add( bSizerPanelMain, 1, wx.EXPAND, 0 )
        
        
        self.panelMain.SetSizer( bSizerPanel )
        self.panelMain.Layout()
        bSizerPanel.Fit( self.panelMain )
        bSizerFrame.Add( self.panelMain, 1, wx.EXPAND |wx.ALL, 0 )
        
        
        self.SetSizer( bSizerFrame )
        self.Layout()
        self.menubar2 = wx.MenuBar( 0 )
        self.menu1 = wx.Menu()
        self.menuItem1 = wx.MenuItem( self.menu1, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu1.AppendItem( self.menuItem1 )
        
        self.menubar2.Append( self.menu1, u"File" ) 
        
        self.Edit = wx.Menu()
        self.menuItem2 = wx.MenuItem( self.Edit, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.Edit.AppendItem( self.menuItem2 )
        
        self.menubar2.Append( self.Edit, u"Edit" ) 
        
        self.menu3 = wx.Menu()
        self.menu21 = wx.Menu()
        self.menu3.AppendSubMenu( self.menu21, u"MyMenu" )
        
        self.menu3.AppendSeparator()
        
        self.menubar2.Append( self.menu3, u"View" ) 
        
        self.SetMenuBar( self.menubar2 )
        
        self.statusBar6 = self.CreateStatusBar( 1, 0, wx.ID_ANY )
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.dirPickerDir.Bind( wx.EVT_DIRPICKER_CHANGED, self.dirPickerDirOnDirChanged )
        self.listBoxGifile.Bind( wx.EVT_LISTBOX, self.listBoxGifileOnListBox )
    
        # ---------- Add widget program settings
        #self.GifPath = None
        # ---------- Add widget program settings
        self.Show()
        # ---------- Event handlers
    
    
    # Virtual event handlers, overide them in your derived class
    def dirPickerDirOnDirChanged( self, event ):
        event.Skip()
    
    def listBoxGifileOnListBox( self, event ):
        event.Skip()
    

if __name__ == "__main__":
    app = wx.App(False)
    frame = frameMain()
    app.MainLoop()
