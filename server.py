from flask import Flask, render_template, send_file
import glob
import os

MARKDOWN_DIR = 'markdown'

app = Flask(
    __name__,
    static_url_path=''
)

markdown_paths = glob.glob('%s/*.md' % MARKDOWN_DIR)
markdown_files = [os.path.splitext(os.path.basename(path))[0] for path in markdown_paths]

@app.route('/')
def index():
    return render_template('index.html', markdown_files=markdown_files)

@app.route('/<path>')
@app.route('/<path:path>')
def show(path):
    path = str(path)
    if path in markdown_files:
        with open('%s/%s.md' % (MARKDOWN_DIR, path), 'r') as f:
            markdown = f.read()
        markdown = markdown.replace('"', '\\"')
        markdown = markdown.replace('\n', '\\n')
        return render_template('print.html', markdown_files=markdown_files, markdown=markdown)
    elif not '.' in path or '.html' in path:
        return render_template(path, slack_usernames=slack_usernames)
    else:
        return backbone_app.send_static_file(path)

if __name__ == '__main__':
    app.run(debug=True)
