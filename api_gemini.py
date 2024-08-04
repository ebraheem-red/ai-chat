

import google.generativeai as genai
genai.configure(api_key="APIKEY")
model = genai.GenerativeModel('gemini-pro')

def ai_message(text):
	response = model.generate_content(text)
	
	return response.text
	
