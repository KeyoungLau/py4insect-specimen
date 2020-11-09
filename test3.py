# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"昆虫标本卡片制作程序", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 500,300 ), wx.Size( 500,300 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

		self.filePath = wx.Button( self, wx.ID_ANY, u"打开", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.filePath, 0, wx.ALL, 5 )

		self.startWork = wx.Button( self, wx.ID_ANY, u"运行", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.startWork, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

		self.output = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.output, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def open(self, event):
		# 打开文件
		dlg = wx.FileDialog(self, u'选择要打开的txt文件', style=wx.DD_DEFAULT_STYLE)
		if dlg.ShowModal() == wx.ID_OK:
			self.fileName.SetValue(dlg.GetPath())  # )# 将选择文件的路径输出到fileName里
			file = open(self.fileName.GetValue())
			self.textEdit.SetValue(file.read())
			file.close()



	def __del__( self ):
		pass




if __name__ == '__main__':
	app = wx.App()
	fram = MyFrame1(None)
	#fram.show()
	app.MainLoop()