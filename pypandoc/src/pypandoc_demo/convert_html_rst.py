import pypandoc

def html2rst():
    output = pypandoc.convert_file('somefile.md', 'rst', outputfile="somefile.rst")
    assert output == ""

if __name__ == '__main__':
    html2rst()
