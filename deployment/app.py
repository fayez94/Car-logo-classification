from fastai.vision.all import load_learner
import gradio as gr

car_logo = [
"Audi car logo",
"BMW car logo",
"Chevrolet car logo",
"Dodge car logo",
"Ford car logo",
"Honda car logo",
"Hyundai car logo",
"Jaguar car logo",
"Jeep car logo",
"Kia car logo",
"Land Rover car logo",
"Lexus car logo",
"Mazda car logo",
"Mercedes-Benz car logo",
"Nissan car logo",
"Porsche car logo",
"Subaru car logo",
"Tesla car logo",
"Toyota car logo",
"Volkswagen car logo"]

model = load_learner("models/logo_recognizer_v1.pkl")


def recognize_image(image):
  pred, idx, probs = model.predict(image)
  return dict(zip(car_logo, map(float,probs)))

image = gr.Image()
label = gr.Label()

examples = [
    'test_images/lexus-logo.png',
    'test_images/Mazda-Logo.png',
    'test_images/toyota-logo.png']


demo = gr.Interface(fn=recognize_image, inputs="image", outputs="label", examples = examples)
demo.launch(inline = False, share = True)
