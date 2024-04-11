# TrOCR Handwritten Text Recognition

This repository contains the implementation of the TrOCR model for handwritten text recognition. The TrOCR model is a state-of-the-art transformer-based Optical Character Recognition (OCR) model that has been pre-trained on a large corpus of handwritten text images.

## Features
- Utilizes the `TrOCRProcessor` and `VisionEncoderDecoderModel` from the Hugging Face Transformers library.
- Processes images using the Python Imaging Library (PIL).
- Employs `tqdm` for progress bars during image processing.

## Requirements
- Python 3.x
- PyTorch
- OpenCV
- Hugging Face Transformers
- PIL
- NumPy
- Matplotlib

## Usage
To use this model, ensure you have all the required libraries installed. Place your handwritten text images in the designated folder, and run the provided script. The model will divide the image into cropped parts and predict the text within each segment, effectively recognizing the handwritten text.

For detailed instructions and examples, please refer to the `examples` directory.

## Model Details
The `TrOCR handwritten large model` is specifically fine-tuned to handle a variety of handwriting styles with high accuracy. It leverages advanced deep learning techniques to interpret complex handwriting patterns.

For more information on the model architecture and training process, please see the `model` directory.

## Performance
This is a work in progress. As I said it uses the TrOCR large model pretrained on handwritten texts. It seems to work fine in english, but I'm having some struggles with italian language.
Two main insight, works fine when the image doesn't contains too much words, and works better when it is written in block letters. 
For the first reason we tried a segmentation without text detection. We simply divide the image into cropped parts in order to get better estimations.
A fine-tuning with italian handwritten examples may be needed

![File_1](https://github.com/Nava-s/Handwritten-text/blob/main/images/handwritten/Figure_1.png)

![File_2](https://github.com/Nava-s/Handwritten-text/blob/main/images/handwritten/Figure_2.png)

![File_3](https://github.com/Nava-s/Handwritten-text/blob/main/images/handwritten/Figure_3.png)

![File_4](https://github.com/Nava-s/Handwritten-text/blob/main/images/handwritten/Figure_4.png)

![File_5](https://github.com/Nava-s/Handwritten-text/blob/main/images/handwritten/Figure_5.png)

![File_6](https://github.com/Nava-s/Handwritten-text/blob/main/images/handwritten/Figure_6.png)

![File_7](https://github.com/Nava-s/Handwritten-text/blob/main/images/handwritten/Figure_7.png)

![File_8](https://github.com/Nava-s/Handwritten-text/blob/main/images/handwritten/Figure_8.png)

![File_9](https://github.com/Nava-s/Handwritten-text/blob/main/images/handwritten/Figure_9.png)

![File_10](https://github.com/Nava-s/Handwritten-text/blob/main/images/handwritten/Figure_10.png)

![File_11](https://github.com/Nava-s/Handwritten-text/blob/main/images/handwritten/Figure_11.png)

![File_12](https://github.com/Nava-s/Handwritten-text/blob/main/images/handwritten/Figure_12.png)

![File_13](https://github.com/Nava-s/Handwritten-text/blob/main/images/handwritten/Figure_13.png)

The end result will be printed as:
"What I'd like to get is a good result, in,ord her to achieve it. I need to try out a lot of models. This is done without text detection next I'd like to Try. another one with seq. mentation. Adesso Provo in Italiano. Vediamo cosa esce fa vari. Spero di niscire ad 
airtare Angelo!"

Not perfect, but still a nice result





