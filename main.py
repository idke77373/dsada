from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template for the response
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>embed</title>
<meta content="{{ title }}" property="og:title" />
<meta content="{{ description }}" property="og:description" />
<meta content="#{{ color }}" data-react-helmet="true" name="theme-color" />
<meta property="og:image" content="{{ image }}" />
<meta content="{{ author }}" property="og:site_name">
</head>
</html>
"""

@app.route('/embed')
def generate_embed():
    # Get query parameters from the URL
    title = request.args.get('title', '')
    description = request.args.get('description', '')
    color = request.args.get('color', '000000')
    image = request.args.get('image', '')
    author = request.args.get('author', '')

    # Render the HTML template with the provided data
    html_response = render_template_string(html_template,
                                           title=title,
                                           description=description,
                                           color=color,
                                           image=image,
                                           author=author)

    return html_response

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
