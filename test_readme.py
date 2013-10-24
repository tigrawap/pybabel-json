from docutils.core import publish_string
import os

README_HTML_STORE_LOC='/tmp/pybabel_json_readme.html'

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

translated=publish_string(read('README.rst'),writer_name='html')
with open(README_HTML_STORE_LOC,'w') as html:
    html.write(translated)
os.system("open %s"%README_HTML_STORE_LOC)
