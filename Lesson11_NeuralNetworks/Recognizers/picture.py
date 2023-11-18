import cv2
from cv2 import Mat
from PIL import Image

class Picture:
    def __init__(self, path: str):
        self.Path: str = path
        self.Image: Mat = self.ReadImg(self.Path)
        self.MultiScale: list = list()

    def ReadImg(self, path: str):
        return cv2.imread(path)
    def ShowImg(self, winName: str):
        cv2.imshow(winName, self.Image)
        cv2.waitKey()
    def GetCoordinates(self, path: str, img: Mat):
        cascade = cv2.CascadeClassifier(path)
        return cascade.detectMultiScale(img)
    def HighLight(self, img: Mat):
        for (x, y, width, height) in self.MultiScale:
            cv2.rectangle(img, (x, y), (x+width, y+height), (215, 19, 19), 3)
    def PasteImg(self, maskPath: str, imgPath: str, newPath: str):
        try:
            fLayout = Image.open(imgPath)
            sLayout = Image.open(maskPath)
            fLayoutConverted = fLayout.convert('RGBA')
            sLayoutConverted = sLayout.convert('RGBA')
            for (x, y, width, height) in self.MultiScale:
                sLayoutConverted = sLayoutConverted.resize((width, int(height / 3)))
                fLayoutConverted.paste(sLayoutConverted, (x, int(y + height / 4)))
                fLayoutConverted.save(newPath)
                return cv2.imread(newPath)
        except Exception as ex:
            raise ex
if __name__ == '__main__':
    imgPath = '../Imgs/cat.jpeg'
    winName = 'Cat'
    filePath = '../Files/haarcascade_frontalcatface_extended.xml'
    glassesPath = '../Imgs/glasses.png'
    newPath = '../Imgs/cat_with_glasses.png'
    pict = Picture(imgPath)
    pict.MultiScale = pict.GetCoordinates(filePath, pict.Image)
    pict.HighLight(pict.Image)
    pict.Image = pict.PasteImg(glassesPath, imgPath, newPath)
    pict.ShowImg(winName)