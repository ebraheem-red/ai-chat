from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import mainthread
from kivy.core.window import Window
from arabic_textinput import Inp , a_text 


class ChatApp(App):
    def build(self):
        # تحميل ملف الواجهة
        self.load_kv('chatAI-1.kv')
        Window.softinput_mode = 'pan'
        return self.root
    


    	  
    	  
    def send_message(self,*args):
        text_input = self.root.ids.chat_input
        chat_history = self.root.ids.chat_history
        text_input.textd=""

        message = text_input.text
        if message:
            chat_history.text += f"\n[b]You:[/b] {message}"
            text_input.text = ""

            # Simulate a response
            self.process_message(message)

    def process_message(self, message):
        # Echo the same message back
        response = message
        self.update_chat(response)
    def re(self,text):
     	t=a_text(text)
     	return t
     
    @mainthread
    def update_chat(self, response):
        chat_history = self.root.ids.chat_history
        chat_history.text += f"\n[b]Bot:[/b] {response}"

if __name__ == '__main__':
    ChatApp().run()