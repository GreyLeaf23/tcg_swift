import json

# Load the JSON data from a file
with open('./assets/python_&_json/raw_file_list.json', 'r') as json_file:
    pokemon_list = json.load(json_file)

html_template = '''
<div>
    <center>
        <img src="./assets/images/cards/{pokemon}">
        <p>{pokemon}</p>
        <button onclick="runPythonScript('{pokemon}')">ADD THIS CARD</button>
    </center>
</div>
'''

html_output = ''
for pokemon in pokemon_list:
    html_output += html_template.format(pokemon=pokemon)

with open('output.html', 'w') as html_file:
    html_file.write(html_output)

print("HTML file 'output.html' generated successfully.")