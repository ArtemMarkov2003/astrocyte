import cv2
import glob
def load_cadrs_from_foulder(folder_path):
    image_list = []
    image_files = glob.glob(folder_path + '/*.png')
    for image_path in image_files:
        image = cv2.imread(image_path)
        image_list.append(image)
    return image_list