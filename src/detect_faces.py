def detect_faces(path, writer):
    """Detects faces in an image."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Faces:')
    i = 0
    
    face_data =[]
    for face in faces: 
        row_data = []
        row_data.append(path)
        row_data.append(f'{i}')
        row_data.append(likelihood_name[face.headwear_likelihood])
        row_data.append(face.roll_angle)
        row_data.append(face.pan_angle)
        row_data.append(face.tilt_angle)
        print(f'Face {i}: headware: {likelihood_name[face.headwear_likelihood]}')
        print('Normalized bounding polygon vertices: ')
        j = 6
        for vertex in face.bounding_poly.vertices:
            print(f' - ({vertex.x}, {vertex.y})')
            row_data.append(vertex.x)
            row_data.append(vertex.y)
            j+=2
            if j > 12:
                break
        i +=1
        writer.writerow(row_data)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))