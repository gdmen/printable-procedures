import datetime
import flask
import glob
import os

MARKDOWN_DIR = 'procedures'

app = flask.Flask(
    __name__,
    static_url_path=''
)

class FileInfo:

    def __init__(self, name, last_modified):
        self.name = name
        self.last_modified = datetime.datetime.fromtimestamp(last_modified).strftime('%b %d, %Y')

def GetFileInfos():
    md_paths = glob.glob('%s/*.md' % MARKDOWN_DIR)
    md_file_infos = [FileInfo(os.path.splitext(os.path.basename(path))[0], os.path.getmtime(path)) for path in md_paths]
    return md_file_infos

@app.route('/')
def index():
    return flask.render_template('index.html', file_infos=GetFileInfos())

@app.route('/<path>')
@app.route('/<path:path>')
def show(path):
    md_names = [fi.name for fi in GetFileInfos()]
    path = str(path)
    if path in md_names:
        with open('%s/%s.md' % (MARKDOWN_DIR, path), 'r') as f:
            md = f.read()
        md = md.replace('"', '\\"')
        md = md.replace('\n', '\\n')
        return flask.render_template('print.html', markdown=md)
    else:
        return app.send_static_file(path)

if __name__ == '__main__':
    app.run(debug=True)
