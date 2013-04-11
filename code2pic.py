import os
import sys
import Image
import math

class Code2Pic:
  """a module to convert the codes to images
  """

  def __init__(self):
    self.code_name = ''
    self.image_length = 0
  
  def readCode(self, file_path):
    try:
      file_read = open(file_path).read()
      file_length = len(file_read)
      file_length_sqrt = math.pow(file_length, 0.5)
      file_length_sqrt = int(file_length_sqrt) + 1
      self.image_length = file_length_sqrt
      
      result = [ord(each_char) for each_char in file_read]
      for i in range(file_length, self.image_length * self.image_length):
        result.append(0)

      return result
        
    except Exception as e:
      print e

  def saveImage(self, file_path, image_path):
    try:
      code_char = self.readCode(file_path)
      save_image = Image.new('RGB', (self.image_length, self.image_length))
      for i in range(0, self.image_length):
        for j in range(0, self.image_length):
          print i, j
          color = code_char[i*self.image_length + j]
          save_image.putpixel((i, j), (color, color, color))
      save_image.save(image_path, '')
    except Exception as e:
      print e
      return

  def main(self):
    """main method to deal with the code
    """
    self.saveImage('code2pic.py', 'test1.bmp')
    

if __name__ == '__main__':
  test_code2pic = Code2Pic()
  test_code2pic.main()
