from pdfreader import SimplePDFViewer

class ResumeReader:
    def __init__(self, file):
        self.file = file
        self.viewer = SimplePDFViewer(open(self.file,'rb'))
        self.viewer.render()
    
    def get_text(self):
        return self.viewer.canvas.strings
