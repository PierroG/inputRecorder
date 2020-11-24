
import time, pickle, random, threading
from pynput import keyboard
from pynput import mouse
import win32gui


class InputRecorder():
	def __init__(self, handle_mouse = False, handle_keyboard = True, output_callback = None, record_callback = None, play_callback = None):
		self.is_recording = False
		self.is_playing = False
		self.output_callback = output_callback
		self.record_callback = record_callback
		self.play_callback = play_callback
		self.start_time = 0
		self.keytmp = [] # Anti hold spam
		self.recording = [] # Recording container variable
		self.recording_name = None
		self.handle_mouse = handle_mouse # do need to habdle mouse
		self.handle_keyboard = handle_keyboard
		self.keyboardController = keyboard.Controller() # Keyboard Controller
		self.mouseController = mouse.Controller() # Mouse Controller

 # Keyboard Input Event 

	def on_press(self,key):
		if key == keyboard.Key.esc:
			self.stopRecord()
			self.stopPlay()
			
		elif key not in self.keytmp:
			print('pressed :',key)
			self.keytmp.append(key)
			self.recording.append([time.perf_counter() - self.start_time, key, 'p'])
			if self.output_callback is not None:
				self.output_callback(self.recording[-1])
				
	def on_release(self,key):
		if key in self.keytmp:
			self.keytmp.remove(key)
			print('realesed :',key)
			self.recording.append([time.perf_counter() - self.start_time, key, 'r'])
			if self.output_callback is not None:
				self.output_callback(self.recording[-1])
					
# Mouse Input Event

	def on_move(self,x, y):
		print('Pointer moved to ',(x, y), end="\r")

	def on_click(self,x, y, button, pressed):
		print('{0} at {1}'.format(
			'Pressed' if pressed else 'Released',
			(x, y)))
		if button == mouse.Button.left:
			print ('Left')
			self.recording.append([time.perf_counter() - self.start_time, [button,(x,y)], 'mp' if pressed else 'mr'])
			if self.output_callback is not None:
				self.output_callback(self.recording[-1])
		if button == mouse.Button.right:
			self.recording.append([time.perf_counter() - self.start_time, [button,(x,y)], 'mp' if pressed else 'mr'])
			if self.output_callback is not None:
				self.output_callback(self.recording[-1])
			print ('right')
		if button == mouse.Button.middle:
			print ('middle')

	def on_scroll(self,x, y, dx, dy):
		print('Scrolled {0} at {1}'.format(
			'down' if dy < 0 else 'up',
			(x, y)))

# Recorder function

	def startRecord(self, delay = 0):
		self.recording_name = None
		time.sleep(delay)
		self.start_time = time.perf_counter()
		if self.handle_mouse:
			self.mouse_listener = mouse.Listener(on_click=self.on_click) #, on_move=self.on_move
			self.mouse_listener.start()

		if self.handle_keyboard:
			self.key_listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
			self.key_listener.start()
			self.is_recording = True
		
		while self.is_recording:
			pass

		if self.handle_mouse:
			self.mouse_listener.stop()
		if self.handle_keyboard:
			self.key_listener.stop()
		print('--- end Recording ---')

	def stopRecord(self):
		if self.is_recording:
			if self.handle_mouse:
				self.mouse_listener.stop()
			if self.handle_keyboard:
				self.key_listener.stop()
			self.is_recording = False
			if self.record_callback is not None:
				self.record_callback()

	def resetRecording(self):
		self.recording = []

	def saveRecord(self,name):
		try:
			pickle.dump(self.recording, open(name+".dat","wb"))
			self.recording_name = name
			return True
		except:
			return False

	def loadRecord(self,name):
		try:		
			self.recording = pickle.load(open(name+".dat","rb"))
			self.recording_name = name
			return True
		except:
			return False

# Player function

	def playRecording(self, do_loop = False, start_delay = 0, with_reverse = False, speed = 1, f = None):#mode: normal,reverse
		self.key_listener = keyboard.Listener(on_press=self.on_press)
		self.key_listener.start()
		need_loop = True
		time.sleep(start_delay)
		self.is_playing = True
		last_instant = 0
		if self.recording is not None:
			while need_loop and self.is_playing:
				i = 0
				for instant in self.recording:
					print(len(self.recording))
					if self.is_playing:
						time.sleep(abs(instant[0]-last_instant)/speed)
						if f is not None:
							f(i)
						last_instant = instant[0]
						if instant[2] == 'p':
							self.keyboardController.press(instant[1])
							print('Do presse :',instant[1])
						elif instant[2] == 'r':
							self.keyboardController.release(instant[1])
							print('Do release :',instant[1])
						elif instant[2] == 'mp':
							self.mouseController.position = instant[1][1]
							self.mouseController.press(instant[1][0])
							print('Do press mouse:',instant[1])
						elif instant[2] == 'mr':
							self.mouseController.position = instant[1][1]
							self.mouseController.release(instant[1][0])
							print('Do release mouse:',instant[1])
						i += 1
					else:
						break
				if do_loop == False:
					need_loop = False
			self.key_listener.stop()
			print('--- end Playing ---')


	def stopPlay(self):
		if self.is_playing:
			self.is_playing = False
			if self.play_callback is not None:
				self.play_callback()
			self.play_callback()

# Test function

	def inverseZQSD(self):
		for i in range(0,len(self.recording)):
			try:
				if self.recording[i][2] == 'p':
					self.recording[i][2] = 'r'
				elif self.recording[i][2] == 'r':
					self.recording[i][2] = 'p'
				if self.recording[i][1].char == 'z':
					self.recording[i][1] = 's'
				elif self.recording[i][1].char == 'q':
					self.recording[i][1] = 'd'
				elif self.recording[i][1].char == 's':
					self.recording[i][1] = 'z'
				elif self.recording[i][1].char == 'd':
					self.recording[i][1] = 'q'
			except:
				pass

	def reverseRecoding(self,type=None):
		if type=='zqsd':
			self.inverseZQSD()	
		self.recording.reverse()



					

if __name__=='__main__':
	ir = InputRecorder(handle_mouse=True)
	ir.startRecord(delay=1)
