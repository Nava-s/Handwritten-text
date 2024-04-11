This is a work in progress. As I said it uses the TrOCR large model pretrained on handwritten texts. It seems to work fine in english, but I'm having some struggles with italian language.
Two main insight, works fine when the image doesn't contains too much words, and works better when it is written in block letters. 
For the first reason we tried a segmentation without text detection. We simply divide the image into cropped parts in order to get better estimations.
A fine-tuning with italian handwritten examples may be needed


