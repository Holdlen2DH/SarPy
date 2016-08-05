'''

'''
import sys

import gdal
from gdalconst import *
class AstRasterData(object):
    def __init__(self):
        self.__rows = 0
        self.__cols = 0
        self.__bandcount = 0
        self.__filepath = ""
        self.__datadir = ""
        self.__filename = ""

    def SetFilePath(self, filepath):
        self.__filepath = filepath
        # set filename and data directory then
        
        
class EnviBinReader(AstRasterData):
    def __init__(self):
        # gdal dataset
        self.__ds = None
        print "do nothing"
        driver = gdal.GetDriverByName('ENVI')
        driver.Register()
        
        

    def Open(self,filepath):
        super(EnviBinReader, self).SetFilePath(filepath)
        # call super __init__()
        
        self.__ds = gdal.Open(filepath, GA_ReadOnly)
        if self.__ds is None:
            print 'Could not open ' + filepath
            sys.exit(1)

        self.__rows = self.__ds.RasterXSize
        self.__cols = self.__ds.RasterYSize
        print('rows = ', self.__rows, 'cols = ', self.__cols)

    def ReadData(self, roiX, roiY, roiCols, roiRows, bandIndex):
        # check input parameters
        if(roiCols <= 0 or roiRows <= 0):
            print("The height or width of ROI is less than zero!")
            sys.exit(1)

        # get bandIndex-th band 
        band = self.__ds.GetRasterBand(bandIndex) # band index is 1-based
        # read data
        data = band.ReadAsArray(roiX, roiY, roiCols, roiRows)
        return data

        
        

if __name__ == '__main__':
    fn = "./C3/C11.bin"
    eb = EnviBinReader()
    eb.Open(fn)

    data = eb.ReadData(0,0,3,3,1)
    print data
