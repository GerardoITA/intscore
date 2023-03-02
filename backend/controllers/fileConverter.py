import json
import argparse
import os
from zipfile import ZipFile, BadZipFile
from io import TextIOWrapper

from ClauseWizard import cwparse, cwformat

from backend.controllers.fileIndexer import fileIndexer


class fileConverter(fileIndexer):
    def __init__(self, in_fn, out_fld):
        fileIndexer.__init__(self,in_fn=in_fn, out_fld=out_fld)
        self.outFile(file_type=".json")


    # The function parser is a modified version of the setup.py of this project
    # https://github.com/Shadark/ClauseWizard
    def parser(self, in_fn, out_fn):
        parser = argparse.ArgumentParser(prog="ClauseWizard",
                                         description="Parses a Clausewitz file (savegame or txt) to a JSON file. \
                                                          Overwrites the output!\nCompatible with non-binary \
                                                          EU4, CK2, Stellaris and HOI4 games.")
        # TODO Check overwriting
        try:
            fh = open(in_fn, 'r')  # Check if file exists
            print('file exists')
            fh.close()
        except FileNotFoundError:
            parser.error('Input file "{}" not found.'.format(in_fn))
            exit(-1)
        except Exception as ex:
            parser.error('Error input file {}: {}'.format(in_fn, str(ex)))
            exit(-1)

        try:
            fh = open(out_fn, 'w')
            print('right output file')
            fh.close()
        except Exception as ex:  # Don't really know what exceptions could appear here
            parser.error('Error with output file {}: {}'.format(out_fn, str(ex)))
            exit(-1)
        try:
            with ZipFile(in_fn) as zipdata:  # Compressed file
                zipfn = 'gamestate'  # Default
                for zipelem in zipdata.infolist():
                    if zipelem.filename == 'gamestate' or zipelem.filename.endswith(
                            '.ck2'):  # EU4, HOI, Stellaris or CK2 files
                        zipfn = zipelem.filename
                        break
                with zipdata.open(zipfn, 'r') as fid:  # Save data
                    print("Found compressed data.")
                    print("Loading file in memory...")
                    gamedata = TextIOWrapper(fid,
                                             encoding='iso-8859-1').read()  # Load in memory, should be this encoding
                    # TODO Check for other encodings support
                    if gamedata[:7] == 'version':  # Stellaris does not follow same pattern
                        print("Game name: Stellaris")
                    else:
                        print("Game name: {}".format(gamedata[:3]))
                    if gamedata[4:6] == "bin":  # Binary file = HoI? ironman = not supported
                        # TODO Further checks
                        print("Ironman games are currently not supported.")
                        exit(-1)
                    print("Parsing file...")
                    res = cwparse(gamedata, debug=False)
                    if isinstance(res, int):  # Error
                        print('Error parsing input file {}'.format(in_fn))
                        return (-1)
                    print("Generating struct tree...")
                    res_dict = cwformat(res)
                    with open(out_fn, 'w', encoding='utf-8') as outf:
                        print("Writing results to file...")
                        outf.write(json.dumps(res_dict, indent=2, ensure_ascii=False))
        except BadZipFile:  # Uncompressed file
            with open(in_fn, 'r', encoding='iso-8859-1') as fid:
                print("Found raw data.")
                print("Loading file in memory...")
                gamedata = fid.read()  # Load in memory
                if gamedata[:7] == 'version':  # Stellaris does not follow same pattern
                    print("Game name: Stellaris")
                else:
                    print("Game name: {}".format(gamedata[:3]))
                if "bin" in gamedata[1:8]:  # Binary file = ironman = not supported
                    print("Binary (probably ironman) games are currently not supported.")
                    exit(-1)
                print("Parsing file...")
                res = cwparse(gamedata, debug=False)
                if isinstance(res, int):  # Error
                    print('Error parsing input file {}'.format(in_fn))
                    exit(-1)
                print("Generating struct tree...")
                res_dict = cwformat(res)
                with open(out_fn, 'w', encoding='utf-8') as outf:
                    print("Writing results to file...")
                    outf.write(json.dumps(res_dict, indent=2, ensure_ascii=False))
        except Exception as ex:
            raise ex


if __name__ == '__main__':
    out_fld = 'C:/Users/Diego/Downloads'
    in_fn = 'C:/Users/Diego/Downloads/mp_Ottoman_Empire1599_01_01.eu4'
    c= fileConverter(in_fn, out_fld)
    print(c.__dict__)