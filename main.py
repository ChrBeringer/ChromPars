#/usr/bin/python

if __name__ == "__main__":
    import re
    import csv
    import pandas as pd
    import matplotlib as plt
    import sqlite3 as sq3
    import elabpy as eln

class Elab():
  '''Connection to the elabFTW-System via its python-API'''
  pass

class ShimdazuLS(Elab):
  '''specific handles of Shimdazu-resultfiles and instrument-batches '''
  def __init__(self,exportfile,concTable):
    self.exportfile = str(exportfile)
    self.concTable = pd.Dataframe(concTable)
  
  def parseExport():
    pass
  
  def createBatch():
    pass


class Experiment(Elab):
  def __init__(self,exId,variables,batch):
  '''handles experimental data, concentrations and the predifined variables/factors of the experiment'''
  def createExperiment():
    pass
  def attachRack():
    pass
  def detachRack():
  
class Rack(Elab):
  '''represents smallest unit of the physical storage system for samples inside the lab'''
  def createRack():
    pass
  def deleteRack():
    pass
