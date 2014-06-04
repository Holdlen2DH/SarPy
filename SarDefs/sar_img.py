""
 Module containing the sarImg class and some basic processing algorithm

 by Holdlen2DH 2014-06-05, holdlen2dh@gmail.com
"""

class sarImg:
    """
    A class defined for SAR images.

    Parameters:
    _____________________
    width: the width of sar image
    height: the height of sar image
    datatype: 
    """

    def __init__(self):
        print 'This class is defined for SAR images.'
        self.__width = 0
        self.__height = 0

    def openSARImg(self, filenames):
        print 'Open single or polarimetric SAR images.'
        # Create vrt files
        
        self.openSARImgByVRT('vrt_path')

    def openSARImgByVRT(self, vrt_path):
        print 'Open SAR images by vrt files.'

# Test
if __name__ == "__main__":
    sarimg = sarImg()
    sarimg.openSARImg('HH.pol')
