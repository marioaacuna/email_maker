# This script is a simple email composer that uses Ollama to generate an email based on the format and what to fields.
# The user can input their desired format and what they want in the email, and then the script will use Ollama to generate an email based on those inputs.

import tkinter as tk
import ollama
import json

# Loading the config file
def load_config():
    try:
        with open('config.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Config file not found. Using default settings.")
        return {"model": "default_model"}
    except json.JSONDecodeError:
        print("Error reading the config file. Check its format.")
        return {"model": "default_model"}

config = load_config()



def generate_response():
    email_format = format_entry.get()
    what_to = What_entry.get()

    prompt = f'Given the format """ {email_format} """, You must compose an email. The email needs to include the following: """{what_to}""". Sign as """ Mario""" '


    # Calling the Ollama 
    
    response = ollama.chat(model=config['model'], messages=[
    #response = ollama.chat(model='mistral', messages=[
        {
            'role': 'user',
            'content': prompt
        },
    ])
    response_content = response['message']['content']

    # Displaying the response
    response_text.delete("1.0", tk.END)
    response_text.insert(tk.END, response_content)

# Set up the Tkinter window
root = tk.Tk()
root.title("Email Generator")

# Email format entry
tk.Label(root, text="Email Format:").pack()
format_entry = tk.Entry(root)
format_entry.pack()

# What to entry
tk.Label(root, text="What to:").pack()
what_entry = tk.Entry(root, width=25)
what_entry.pack()

# Button to generate response
generate_button = tk.Button(root, text="Generate Response", command=generate_response)
generate_button.pack()

# Text widget to display the response
response_text = tk.Text(root, height=25, width=125)
response_text.pack()

# Run the application
root.mainloop()
