from flask import Flask, request, send_file
from plugins.master import download_content

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        platform = request.form['platform']
        try:
            file_path = download_content(url, platform)
            return send_file(file_path, as_attachment=True)
        except Exception as e:
            return f"<h3>Error: {str(e)}</h3>", 400
    return '''
        <h1>TXT-Master-All (Render Edition)</h1>
        <form method="post">
            URL: <input name="url" type="text"><br>
            Platform: <input name="platform" type="text"><br>
            <input type="submit" value="Download">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
