# Preprocessing using Computer Vision Technics

The dataset presents a preprocessing of the output of the YOLOv5 model for the detection of insulators.

There are 12,827 original images used for training and validation (Training: 10,886 and Validation: 1,941), which can be also used for testing.
 
The 5 preprocessing technics are used:

* **Gaussian blur**

* **Binarization with threshold**

* **Adaptive threshold**

* **Threshold with Otsu and Riddler-Calvard**

* **Canny edge detection**

* **Sobel edge detection**

After the application of these preprocessing technics, this dataset has ***89,789 files*** (including the original files).

An example of the output compared to the original image is presented here:

![image](https://user-images.githubusercontent.com/88292916/203595844-cadc0239-f1aa-4445-9e5c-1626546b63a4.png)

---

Additional information can be found at the **[Original Paper](https://doi.org/10.1049/gtd2.12353)**.

BibTeX:
`@article{gtd2.12353, author = {Stefenon, Stéfano Frizzo and Corso, Marcelo Picolotto and Nied, Ademir and Perez, Fabio Luis and Yow, Kin-Choong and Gonzalez, Gabriel Villarrubia and Leithardt, Valderi Reis Quietinho}, title = {Classification of insulators using neural network based on computer vision}, journal = {IET Generation, Transmission \& Distribution}, volume = {16}, number = {6}, pages = {1096-1107}, doi = {10.1049/gtd2.12353}, year = {2022}}`

---

Thank you.

Dr. **Stefano Frizzo Stefenon**

Trento, Italy, March 10, 2023.
