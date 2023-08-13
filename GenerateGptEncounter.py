# Using ChatGPT, I generate new scenarios for the main character
import openai
import os

# Open AI key should be stored in your environmet variables
api_key = os.getenv('openaikey')

# Initialize the OpenAI API client
openai.api_key = api_key

# Prompt for the ChatGPT conversation
prompt = "User: How are you today?\nAI:"

# Generate a response from ChatGPT
response = openai.Completion.create(
  engine="text-davinci-002",  # You can use other engines as well
  prompt=prompt,
  max_tokens=50  # You can adjust the length of the response
)

# Extract and print_slow the AI's response
ai_response = response.choices[0].text.strip()
print_slow("AI:", ai_response)
