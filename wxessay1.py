# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.html
import wx.adv

MNU_VIEW_LIST = 1000
MNU_VIEW_ICON = 1001
MNU_ON_TOP = 1002

###########################################################################
## Class WxAppMenuLauncherEssay1
###########################################################################

class WxAppMenuLauncherEssay1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"WxAppMenuLauncher", pos = wx.DefaultPosition, size = wx.Size( 305,429 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_menubar1 = wx.MenuBar( 0 )
        self.fileMenu = wx.Menu()
        self.fileExitMenuItem = wx.MenuItem( self.fileMenu, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
        self.fileMenu.Append( self.fileExitMenuItem )

        self.m_menubar1.Append( self.fileMenu, u"File" )

        self.editMenu = wx.Menu()
        self.editAbsToRelativeMenuItem = wx.MenuItem( self.editMenu, wx.ID_ANY, u"absolute paths to relative", wx.EmptyString, wx.ITEM_NORMAL )
        self.editMenu.Append( self.editAbsToRelativeMenuItem )

        self.m_menubar1.Append( self.editMenu, u"Edit" )

        self.viewMenu = wx.Menu()
        self.viewListMenuItem = wx.MenuItem( self.viewMenu, MNU_VIEW_LIST, u"List", wx.EmptyString, wx.ITEM_NORMAL )
        self.viewMenu.Append( self.viewListMenuItem )

        self.iconsMenuItem = wx.MenuItem( self.viewMenu, MNU_VIEW_ICON, u"Icons", wx.EmptyString, wx.ITEM_NORMAL )
        self.viewMenu.Append( self.iconsMenuItem )

        self.ViewOnTopMenuItem = wx.MenuItem( self.viewMenu, MNU_ON_TOP, u"On Top", wx.EmptyString, wx.ITEM_CHECK )
        self.viewMenu.Append( self.ViewOnTopMenuItem )

        self.m_menubar1.Append( self.viewMenu, u"View" )

        self.helpMenu = wx.Menu()
        self.aboutMenuItem = wx.MenuItem( self.helpMenu, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
        self.helpMenu.Append( self.aboutMenuItem )

        self.m_menubar1.Append( self.helpMenu, u"Help" )

        self.SetMenuBar( self.m_menubar1 )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.listView = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_SMALL_ICON )
        bSizer3.Add( self.listView, 1, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer3 )
        self.Layout()
        self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_ACTIVATE, self.onActivate )
        self.Bind( wx.EVT_CLOSE, self.onClose )
        self.Bind( wx.EVT_MENU, self.onClose, id = self.fileExitMenuItem.GetId() )
        self.Bind( wx.EVT_MENU, self.onViewMenuClick, id = self.viewListMenuItem.GetId() )
        self.Bind( wx.EVT_MENU, self.onViewMenuClick, id = self.iconsMenuItem.GetId() )
        self.Bind( wx.EVT_MENU, self.onViewOnTopMenuItem, id = self.ViewOnTopMenuItem.GetId() )
        self.Bind( wx.EVT_MENU, self.aboutMenuItemOnMenuSelection, id = self.aboutMenuItem.GetId() )
        self.listView.Bind( wx.EVT_LIST_BEGIN_DRAG, self.onListViewDrag )
        self.listView.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.OnListViewOnDblClick )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onActivate( self, event ):
        event.Skip()

    def onClose( self, event ):
        event.Skip()


    def onViewMenuClick( self, event ):
        event.Skip()


    def onViewOnTopMenuItem( self, event ):
        event.Skip()

    def aboutMenuItemOnMenuSelection( self, event ):
        event.Skip()

    def onListViewDrag( self, event ):
        event.Skip()

    def OnListViewOnDblClick( self, event ):
        event.Skip()


###########################################################################
## Class SystrayMenu
###########################################################################

class SystrayMenu ( wx.MenuBar ):

    def __init__( self ):
        wx.MenuBar.__init__ ( self, style = 0 )

        self.m_menu5 = wx.Menu()
        self.m_menu5.AppendSeparator()

        self.m_menuItem7 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"Show", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu5.Append( self.m_menuItem7 )

        self.m_menuItem8 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu5.Append( self.m_menuItem8 )

        self.Append( self.m_menu5, u"SystrayMenuBar" )


    def __del__( self ):
        pass


###########################################################################
## Class AboutWindow
###########################################################################

class AboutWindow ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"About", pos = wx.DefaultPosition, size = wx.Size( 288,198 ), style = wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer9.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.m_bitmap1, 0, wx.ALL, 5 )


        bSizer9.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer6.Add( bSizer9, 1, wx.EXPAND, 5 )

        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer10.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"WxAppMenuLauncher", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        self.m_staticText2.SetFont( wx.Font( 16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer10.Add( self.m_staticText2, 0, wx.ALL, 5 )

        self.m_htmlWin2 = wx.html.HtmlWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.html.HW_SCROLLBAR_AUTO )
        bSizer10.Add( self.m_htmlWin2, 0, wx.ALL, 5 )


        bSizer10.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer6.Add( bSizer10, 1, wx.EXPAND, 5 )

        bSizer101 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer101.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_hyperlink11 = wx.adv.HyperlinkCtrl( self, wx.ID_ANY, u"Github", u"https://github.com/digfish/wxappmenulauncher", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
        bSizer101.Add( self.m_hyperlink11, 0, wx.ALL, 5 )


        bSizer101.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer6.Add( bSizer101, 1, wx.EXPAND, 5 )

        bSizer102 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer102.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"by digfish@digfish.org", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )

        bSizer102.Add( self.m_staticText21, 0, wx.ALL, 5 )

        self.m_htmlWin21 = wx.html.HtmlWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.html.HW_SCROLLBAR_AUTO )
        bSizer102.Add( self.m_htmlWin21, 0, wx.ALL, 5 )


        bSizer102.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer6.Add( bSizer102, 1, wx.EXPAND, 5 )


        bSizer4.Add( bSizer6, 1, wx.EXPAND, 5 )


        bSizer4.Add( ( 0, 0), 1, wx.ALIGN_CENTER, 5 )

        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.m_button1, 0, wx.ALL, 5 )


        bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer4.Add( bSizer8, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer4 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


