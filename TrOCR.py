from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
from tqdm.auto import tqdm
from urllib.request import urlretrieve
from zipfile import ZipFile
from PIL import ImageSequence

import numpy as np
import matplotlib.pyplot as plt
import torch
import os
import glob
import cv2

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
    generated_ids = model.generate(pixel_values,max_new_tokens=100)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return generated_text



def eval_new_data(data_path=None, num_samples=4, model=None, num_lines=1,num_cols=1):
    image_paths = glob.glob(data_path)
    transcription = ''
    for i, image_path in tqdm(enumerate(image_paths), total=len(image_paths)):
        if i == num_samples:
            break
        image = Image.open(image_path).convert('RGB')
        width, height = image.size
        line_height = height // num_lines  # replace num_lines with the number of lines in your image
        line_width = width // num_cols
        if num_lines == 1:
            text = ocr(image, processor, model)
            plt.figure(figsize=(7, 4))
            plt.imshow(image)
            plt.title('\n'+ text)
            plt.axis('off')
            plt.show()
            transcription = text
        else:
            for j in range(num_lines):
                start = j * line_height
                end = (j + 1) * line_height
                for w in range(num_cols):
                    start_w = w * line_width
                    end_w = (w+1) * line_width
                    line_image = image.crop((start_w, start, end_w, end))
                    text = ocr(line_image, processor, model)
                    transcription += ' ' + text
                    plt.figure(figsize=(7, 4))
                    plt.imshow(line_image)
                    plt.title(text)
                    plt.axis('off')
                    plt.show()
        print(transcription)
processor = TrOCRProcessor.from_pretrained('microsoft/trocr-large-handwritten')
model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-large-handwritten').to(device)

eval_new_data(
    data_path=os.path.join('images', 'handwritten', '*'),
    num_samples=1,
    model=model,
    num_lines=5,
    num_cols = 2
)
