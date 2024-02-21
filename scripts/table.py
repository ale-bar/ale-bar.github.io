# Define the table data
headers = ['fruit', 'price', 'country']

tableData = [
    {'fruit':'apple', 'price':4, 'country':'singapore'},
    {'fruit':'orange', 'price':5, 'country':'singapore'},
    {'fruit':'pear', 'price':6, 'country':'singapore'},
    {'fruit':'apple', 'price':7, 'country':'malaysia'},
    {'fruit':'orange', 'price':8, 'country':'malaysia'},
    {'fruit':'pear', 'price':9, 'country':'malaysia'},
]

# Create an HTML string with the table data
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fruit Table</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>

<h1>Fruit Table</h1>

<table>
    <thead>
        <tr>
            {}
        </tr>
    </thead>
    <tbody>
        {}
    </tbody>
</table>

</body>
</html>
"""

# Generate table header HTML
header_html = " "
for header in headers:
    header_html += f"<th>{header}</th>"

# Generate table data HTML
data_html = " "
for data in tableData:
    data_html += "<tr>"
    for key, value in data.items():
        data_html += f"<td>{value}</td>"
    data_html += "</tr>"

# Format the HTML content with header and data
html_content = html_content.format(header_html, data_html)

# Write the HTML content to a file
with open("fruit_table.html", "w") as html_file:
    html_file.write(html_content)

# Open the HTML file in a web browser
import webbrowser
webbrowser.open("fruit_table.html")
