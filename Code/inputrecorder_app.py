from PyQt5 import QtWidgets, QtCore, QtGui, uic
import sys, os
import inputrecorder as ir
import threading
import counter_gui as counter_ui
from dialog_newrecord import Ui_Dialog
# load ui file
baseUIClass, baseUIWidget = uic.loadUiType("inputrecorder_gui.ui")

# use loaded ui file in the logic class
class Logic(baseUIWidget, baseUIClass):
	def __init__(self, parent=None):
		print(str(baseUIWidget),str(baseUIClass))
		super(Logic, self).__init__(parent)
		self.setupUi(self)
		
		self.ir = ir.InputRecorder(handle_mouse = self.cb_handle_m.isChecked(), handle_keyboard = self.cb_handle_k.isChecked(),output_callback = self.addRow,record_callback = self.stop_record, play_callback=self.stop_play)

		#self.b_play.setEnabled(False)
		self.b_record.clicked.connect(self.click_record)
		self.b_play.clicked.connect(self.click_play)
		self.b_datatable.clicked.connect(self.cick_datatable)
		self.b_save.clicked.connect(self.click_save)
		self.b_load.clicked.connect(self.click_load)
		self.b_remove.clicked.connect(self.click_remove)

		self.datatable_hidden = False
		self.cb_handle_k.setEnabled(False)
		#self.cb_handle_m.setEnabled(False)

		self.update_load_list()
		self.resize(445, 400)


	def start_rec(self):
		print("start record")
		self.tableWidget.setRowCount(0)
		if self.sb_delay_r.value() > 0:
			self.window = QtWidgets.QMainWindow()
			self.counterui = counter_ui.Ui_counter()
			self.counterui.setupUi(self.window, self.sb_delay_r.value())
			self.counterui.window.show()
		t = threading.Thread(target=self.ir.startRecord, args=(self.sb_delay_r.value(),)) #kwargs={'delay' : self.spinbox_record.value()}
		t.setDaemon(True)
		t.start()
		self.lcd_color("red")
		self.set_icon("img/stop_record.png", self.b_record)

		self.timer = QtCore.QTimer(self)
		
		self.timer.timeout.connect(self.show_time) 
		self.timer.start(1000)
		self.count = -2

	def click_record(self):
		#start record button
		if not self.ir.is_recording:
			if len(self.ir.recording) != 0:
				print("ici")
				dialog = QtWidgets.QDialog()
				ui = Ui_Dialog()
				ui.setupUi(dialog)
				dialog.show()
				resp = dialog.exec_()
				if resp == QtWidgets.QDialog.Accepted:
					self.ir = ir.InputRecorder(handle_mouse = self.cb_handle_m.isChecked(), handle_keyboard = self.cb_handle_k.isChecked(),output_callback = self.addRow, record_callback = self.stop_record, play_callback=self.stop_play)
					self.ir.resetRecording()
					self.start_rec()
				else:
					print("ref")
			else:
				self.ir = ir.InputRecorder(handle_mouse = self.cb_handle_m.isChecked(), handle_keyboard = self.cb_handle_k.isChecked(),output_callback = self.addRow, record_callback = self.stop_record, play_callback=self.stop_play)
				self.start_rec()

				

		#stop record button
		else:
			self.stop_record()

		# if self.sb_delay_r.value() > 0:
		# 	#create overlay gui counter
		# 	self.window = QtWidgets.QMainWindow()
		# 	self.counterui = counter_ui.Ui_counter()
		# 	self.counterui.setupUi(self.window, self.sb_delay_r.value())
			# self.window.show()
	def stop_record(self):
		self.ir.stopRecord()
		self.lcd_color("grey")
		self.set_icon("img/record.png", self.b_record)
		self.timer.stop()
		if len(self.ir.recording) != 0:
			self.b_play.setEnabled(True)
			self.l_time.setText(str(round(self.ir.recording[-1][0],3)))
			self.l_input.setText(str(len(self.ir.recording)))

	def show_time(self):
		self.count+= 1
		self.lcdNumber.display(self.count / 10)

	def set_icon(self, path, button):
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		button.setIcon(icon)
		try:
			button.setIconSize(QtCore.QSize(40, 40))
		except:
			pass

	def refresh_datatable(self):
		self.tableWidget.setRowCount(0)
		for instant in self.ir.recording:
			self.addRow(instant)

	def select_row(self,row):
		print(row)
		self.tableWidget.item(row,0).setBackground(QtGui.QColor(0, 0, 0))
		# if row!=0:
		# 	self.tableWidget.item(row-1,0).setBackground(QtGui.QColor(255, 255, 255))
		self.tableWidget.scrollToBottom()
		

		print(row)

	def addRow(self, data_elem):
		rowPos = self.tableWidget.rowCount()
		self.tableWidget.insertRow(rowPos)
		self.tableWidget.setItem(rowPos, 0, QtWidgets.QTableWidgetItem(str(round(data_elem[0],2))))
		self.tableWidget.setItem(rowPos, 2, QtWidgets.QTableWidgetItem(str(data_elem[1])))
		# if rowPos !=0:
		# 	self.tableWidget.item(rowPos-1,0).setBackground(QtGui.QColor(150,150,0))
		# self.tableWidget.item(rowPos,0).setBackground(QtGui.QColor(100,100,150))
		#self.tableWidget.setItem(rowPos, 1, QtWidgets.QTableWidgetItem('Key Down' if data_elem[2]=='p' else 'Key Up'))
		if data_elem[2]=='p':
			self.tableWidget.setItem(rowPos, 1, QtWidgets.QTableWidgetItem('Key Down'))
		elif data_elem[2]=='r':
			self.tableWidget.setItem(rowPos, 1, QtWidgets.QTableWidgetItem('Key Up'))
		elif data_elem[2]=='mp':
			self.tableWidget.setItem(rowPos, 1, QtWidgets.QTableWidgetItem('Mouse Click'))
		elif data_elem[2]=='mr':
			self.tableWidget.setItem(rowPos, 1, QtWidgets.QTableWidgetItem('Mouse Realese'))
		self.tableWidget.scrollToBottom()
		
	def click_play(self):
		#start play
		if not self.ir.is_playing and len(self.ir.recording) > 0 :
			#self.tableWidget.setFocus()
			t = threading.Thread(target=self.ir.playRecording ,kwargs={'do_loop' : self.cb_loop.isChecked(),
																   'start_delay' : self.sb_delay_p.value(),
																   'speed' : self.sb_speed.value(),
																   'f' : self.select_row
																   }) #, args=(self.checkBox.isChecked(),self.spinbox_play.value())
			t.setDaemon(True)
			t.start()
			self.lcd_color("green")
			self.b_record.setEnabled(False)
			self.set_icon("img/stop.png",self.b_play)

		#stop play
		elif len(self.ir.recording) > 0:
			self.stop_play()

	def stop_play(self):
		self.lcd_color("grey")
		self.ir.stopPlay()
		self.set_icon("img/play.png", self.b_play)
		self.b_record.setEnabled(True)

	def cick_datatable(self):
		if self.datatable_hidden:
			self.resize(445, 400)
			self.datatable_hidden = False
			self.b_datatable.setText("Hide data Table")
		else:
			self.resize(445, 162)
			self.datatable_hidden = True
			self.b_datatable.setText("Show data Table")

	def click_save(self):

		if len(self.ir.recording) > 0:
			resp = self.ir.saveRecord(self.entry_name.text())
			if resp:
				self.update_record_info()
				self.entry_preset.addItem(self.entry_name.text())

		
	def click_load(self):
		resp = self.ir.loadRecord(self.entry_preset.currentText())
		if resp:
			self.update_record_info()
			self.refresh_datatable()



	def update_record_info(self):
		self.l_time.setText(str(round(self.ir.recording[-1][0],3)))
		self.l_input.setText(str(len(self.ir.recording)))
		self.l_name.setText(self.ir.recording_name)

	def update_load_list(self):
		self.entry_preset.clear()  
		for file in os.listdir("."):
			if file.endswith(".dat"):
				print(os.path.join(".", file))
				self.entry_preset.addItem(str(file)[:-4])

	def click_remove(self):
		try:
			os.remove(self.entry_preset.currentText()+".dat")
			self.update_load_list()
			print('successfuly delete')
		except:
			print('delete error')


	def lcd_color(self,color):
		try:
			self.lcdNumber.setStyleSheet("QLCDNumber{\n"
"    color: "+color+";\n"
"}")
		except:
			pass

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	ui = Logic()
	ui.show()
	sys.exit(app.exec_())