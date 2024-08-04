

import google.generativeai as genai
genai.configure(api_key="AIzaSyAJIlnNv3R_FD5k06-Emx0u60otKeOsWAY")
model = genai.GenerativeModel('gemini-pro')

def ai_message(text):
	response = model.generate_content(text)
	
	return response.text
	
