# Herbok-128
Masked Language Model

Herbok 128 is a masked language model for predicting masked words in a given text. For example:

![Masked Token Prediction](https://github.com/alihakimtaskiran/Herbok-128/raw/main/herbok-128-screenshot.png)


## Instructions to use
1. Make sure that `tensorflow`, `transformers` are installed.

    ```pip install tensorflow transformers```
    
2. Download the `.h5` file of the model from Google drive link:
[Download model](https://drive.google.com/file/d/1fn0H_ApTLiBCUX8I6hFq1MeR0T05CJfo/view?usp=sharing)
3. Download GUI based application. Make sure that 'Herbok-128-export.h5` and `Herbok-128-GUI-Inference.py` are in the same folder.
[Download GUI App](https://github.com/alihakimtaskiran/Herbok-128/raw/main/Herbok-128-GUI-Inference.py)
4. Use python to run `Herbok-128-GUI-Inference.py`.
5. Write any text to input. You can mask the input by writing `{MASK]`. Then press `ENTER`
6. The output will shown in the generated text field. You can regenerate the text by pressing enter after clicking to input field.

## Limitations
Model performs poor if predicted tokens are not seperated with any other words
Dataset solely depends on scientific books and therefore it may not perform in everyday language.
Dataset only contains English text
