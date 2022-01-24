if __name__ == "__main__":
    import re
    import csv
    import os
    import pandas as pd
    import matplotlib as plt
    import sqlite3 as sq3

def parseSamples(exportfile):
    # 1.) initialize Sample-Dataframe to combine all results of the measured substances, which will be the result of the
    # parser and initialize a Dataframe where the single lines of a substance are stored in temporarly. 
    # Create Pandas-Frame for the given ASCII-results of the analyte and later extract the substance-specific conc.-column.
    # from the exportDf.

    with open(exportfile,"r") as f:
        found_analytes = int(0)
        for line in f:
            if str("ID#") in line:
                print(line)
            
            else:
                print("No match")

#parseSamples(exportfile="ASCIIExport.txt")


sampleNames = []
with open("ASCIIExport.txt","r") as f:
    pattern = re.
    for line in f:
        if "Conc." in line:
            print(line)

print("end")

# python samplepars.py