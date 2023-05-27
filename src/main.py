from localize_objects import localize_objects
from detect_faces import detect_faces
import csv
header = ['file_path', 'face_number', 'headware_likelyhood', 'roll_angle', 'pan_angle', 'tilt_angle', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4']
def main():
    with open('test.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i in range(1, 7):
            print(f'Image Number {i}:')
            detect_faces(f'images/test_image_{i}.jpg', writer)
            
if __name__ == '__main__':
    main()
