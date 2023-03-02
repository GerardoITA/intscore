from backend.controllers.fileIndexer import fileIndexer


class analyzerController(fileIndexer):
    def __init__(self):
        pass


if __name__ == "__main__":
    print('asd')
    out_fld = 'C:/Users/diego/OneDrive/Documenti/NetBeansProjects'
    in_fn='C:/Users/diego/OneDrive/Documenti/NetBeansProjects/asd.xml'
    f= fileIndexer(in_fn, out_fld)
    print(f.__dict__)