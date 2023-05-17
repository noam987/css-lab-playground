def localize_objects(path):
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content = content)
    objects = client.object_localization(image=image).localized_object_annotations
    print(f'Number of objects found: {len(objects)}')
    for object_ in objects:
        print(f'\n{object_.name} (confidence: {object_.score})')
        print('Normalized bounding polygon vertices: ')
        for vertex in object_.bounding_poly.normalized_vertices:
            print(f' - ({vertex.x}, {vertex.y})')
    #Notes from this Naive implementation: 
    # Cannot detect hats on people in the few images I tried
