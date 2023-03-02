class fileIndexer():
    def __init__(self, in_fn, out_fld):
        self.in_fn = in_fn
        self.out_fld = self.replacer(out_fld)
        self.out_fn = ""
        self.outFile()

    def replacer(self, original_string):
        resultant_string = ""
        for character in original_string:
            if character == "\\":
                resultant_string += "/"
            else:
                resultant_string +=character
        return resultant_string

    def outFile(self):
        filename = self.in_fn.split('/')[-1]
        self.out_fn = self.out_fld + '/' + filename
        self.out_fn = self.out_fn.split('.')[0] + ".json"


if __name__ == "__main__":
    print('asd')
    out_fld = 'C:/Users/diego/OneDrive/Documenti/NetBeansProjects'
    in_fn='C:/Users/diego/OneDrive/Documenti/NetBeansProjects/asd.xml'
    f= fileIndexer(in_fn, out_fld)