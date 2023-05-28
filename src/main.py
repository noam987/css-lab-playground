from localize_objects import localize_objects
from detect_faces import detect_faces
import csv
import glob

header = ['file_path', 'face_number', 'headware_likelyhood', 'roll_angle', 'pan_angle', 'tilt_angle', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4']
def main():
    with open('test2.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for path in glob.iglob('images/*.jpg'):
            detect_faces(path, writer)
            
if __name__ == '__main__':
    main()
