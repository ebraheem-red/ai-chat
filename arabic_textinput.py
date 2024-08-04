from kivy.uix.textinput import TextInput as tn
import arabic_reshaper as rsh
import bidi.algorithm 


def a_text(text):
	t=bidi.algorithm.get_display(rsh.reshape(text))
	return t
##--___----___----___----
class Inp(tn):
		def __init__(self,**kwargs):
			super(Inp,self).__init__(**kwargs)
			self.textd = ''
			self.text_language ='ar'
			self.font_name='arial.ttf'
		
		def on_touch_down(self,touch):
			super(Inp,self).on_touch_down(touch)
			self.cur=self.cursor
			
			
		def keyboard_on_textinput(self,window,keycode):
			super(Inp,self).keyboard_on_textinput(window,keycode)
			#self.cur= self.cursor
			self.resh()
			#self.insert_text(str(self.cursor_index()))
			

		def keyboard_on_key_down(self,window,keycode,text,modifiers):
			super(Inp,self).keyboard_on_key_down(window,keycode,text,modifiers)
			#self.text=str(keycode)
			if keycode[0] ==13 :
				self.textd = self.textd+ '\n'
			if keycode[0]== 8 :
				if self.cursor_index == len(self.text):
					self.textd = self.textd[:-1]
					self.text=self.set(self.textd)
				else :
						num=len(self.text)-self.cursor_index()
						self.textd = self.textd[:num-1] + self.textd[num:]
						self.text = self.set(self.textd)
						self.cursor= self.cur
		
		def set (self,text):
					sh = rsh.reshape(text)
					out=bidi.algorithm.get_display(sh)
					return out

		def resh(self):
			if self.cursor_index() == len(self.text):
				self.textd=self.textd + self.text[-1]
				self.text=self.set(self.textd)
			else :
				num=len(self.text)-self.cursor_index()
				self.textd = self.textd[:num] + self.text[self.cursor_index()-1]+self.textd[num:]
				self.text = self.set(self.textd)
				self.cursor= self.cur
				