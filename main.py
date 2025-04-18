from google import genai
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

client = genai.Client(api_key=config["GOOGLE"]["GEMINI_API_KEY"])
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-2.5-flash-preview-04-17",
    contents=prompt
)

print(response.text)