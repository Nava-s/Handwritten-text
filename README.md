This is a work in progress. As I said it uses the TrOCR large model pretrained on handwritten texts. It seems to work fine in english, but I'm having some struggles with italian language.
Two main insight, works fine when the image doesn't contains too much words, and works better when it is written in block letters. 
Next We're gonna try to combine the OpenCV object detection model in order to pass to the TrOCR slices of sentences
