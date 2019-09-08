import pyscreenshot as ImageGrab
import time

images_folder = "orig_images/6/"

for i in range (0,45):
	
	time.sleep(10)
	if __name__ == "__main__":
		im = ImageGrab.grab(bbox=(0, 100, 400, 400)) # X1,Y1,X2,Y2
		print ("saved....",i)
		im.save(images_folder+str(i)+'.png')
		print ("clear screen now and redraw now...")
	