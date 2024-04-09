from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
from tqdm.auto import tqdm
from PIL import ImageSequence

import numpy as np
import matplotlib.pyplot as plt
import torch
import os
import glob

device = torch.device('cpu')


def ocr(image, processor, model):
    """
    :param image: PIL Image.
    :param processor: Huggingface OCR processor.
    :param model: Huggingface OCR model.
    Returns:
        generated_text: the OCR'd text string.
    """
    # We can directly perform OCR on cropped images.
    pixel_values = processor(image, return_tensors='pt').pixel_values.to(device)
    generated_ids = model.generate(pixel_values)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return generated_text

num_lines = 3

def eval_new_data(data_path=None, num_samples=4, model=None):
    image_paths = glob.glob(data_path)
    for i, image_path in tqdm(enumerate(image_paths), total=len(image_paths)):
        if i == num_samples:
            break
        image = Image.open(image_path)
        width, height = image.size
        line_height = height // num_lines  # replace num_lines with the number of lines in your image

        for j in range(num_lines):
            start = j * line_height
            end = (j + 1) * line_height
            line_image = image.crop((0, start, width, end))
            text = ocr(line_image, processor, model)
            plt.figure(figsize=(7, 4))
            plt.imshow(line_image)
            plt.title(text)
            plt.axis('off')
            plt.show()

processor = TrOCRProcessor.from_pretrained('microsoft/trocr-large-handwritten')
model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-large-handwritten').to(device)

eval_new_data(
    data_path=os.path.join('images', 'handwritten', '*'),
    num_samples=1,
    model=model
)
