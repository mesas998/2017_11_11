import os
from cloudinary import uploader
def test():
    uploader.upload("/Users/michaelsweeney/Christmas_card.jpg")

if __name__=='__main__':
    test()
