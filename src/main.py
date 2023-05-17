from localize_objects import localize_objects
from detect_faces import detect_faces


def main():
    for i in range(1, 7):
        print(f'Image Number {i}:')
        detect_faces(f'images/test_image_{i}.jpg')

if __name__ == '__main__':
    main()
