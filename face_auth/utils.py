import pickle
import base64
import tempfile

def base64_to_image(base64_data):
    img_data = base64.b64decode(base64_data.split(",")[1])
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as f:
        f.write(img_data)
        return f.name




def get_face_encoding(image_path):
    import face_recognition
    from PIL import UnidentifiedImageError

    try:
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)

        if len(encodings) != 1:
            return None

        return encodings[0]

    except UnidentifiedImageError:
        return None

    except Exception as e:
        print("FACE ENCODING ERROR:", str(e))
        return None



def serialize_encoding(encoding):
    return pickle.dumps(encoding)

 
def deserialize_encoding(binary):
    return pickle.loads(binary)


def verify_faces(stored_encoding, live_encoding, tolerance=0.5):
    import face_recognition

    distance = face_recognition.face_distance(
        [stored_encoding],
        live_encoding
    )[0]
    return distance <= tolerance

