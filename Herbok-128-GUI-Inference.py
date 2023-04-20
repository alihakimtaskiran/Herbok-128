import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QWidget
import numpy as np
from tensorflow.keras.models import load_model
from keras import backend as K
import pickle
from transformers import BertTokenizer




# Load the model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-large-cased')
model = load_model("Herbok-128-export.h5")

# Define the generate_text function 
def generate_text(text):
    seq = tokenizer.encode_plus(text, max_length=128, padding='max_length', return_tensors='tf', special_tokens=True)['input_ids']
    out=tokenizer.decode(np.argmax(model.predict(seq)[0], axis=-1))
    return out[:out.index(" [PAD]")]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set up the main window
        self.setWindowTitle("Herbok-128-Early-Development")
        self.setGeometry(100, 100, 600, 400)

        # Create the input text box
        self.input_label = QLabel("Enter input text:")
        self.input_textbox = QLineEdit()
        self.input_textbox.returnPressed.connect(self.generate_output)

        # Create the output text box
        self.output_label = QLabel("Generated text:")
        self.output_textbox = QTextEdit()
        self.output_textbox.setReadOnly(True)

        # Add the widgets to the main window
        layout = QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_textbox)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_textbox)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def generate_output(self):
        # Get the input text and generate the output
        input_text = self.input_textbox.text()
        generated_text = generate_text(input_text)

        # Display the generated text in the output textbox
        self.output_textbox.setText(generated_text)

if __name__ == "__main__":
    # Create the application and main window
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()

    # Run the application
    sys.exit(app.exec_())
