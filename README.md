# Face Recognition System with OpenCV's LBPH, and Haar Cascade Algorithm in Python
![face-recognition](https://img.freepik.com/free-photo/face-recognition-personal-identification-collage_23-2150165601.jpg?uid=R16926637&ga=GA1.1.1191958343.1730485732&semt=ais_hybrid)

## Authors
[@tasfiakatha](https://github.com/tasfiakatha)

## Table of contents
- [Project overview](https://github.com/tasfiakatha/Face-recognition-system-with-OpenCV-LBPH-HaarCascade-algorithm-Python/blob/main/README.md#project-overview)
- [Methods](https://github.com/tasfiakatha/Face-recognition-system-with-OpenCV-LBPH-HaarCascade-algorithm-Python/blob/main/README.md#methods)
- [Installation](https://github.com/tasfiakatha/Face-recognition-system-with-OpenCV-LBPH-HaarCascade-algorithm-Python/blob/main/README.md#installation)
- [Quick Look at the Results](https://github.com/tasfiakatha/Face-recognition-system-with-OpenCV-LBPH-HaarCascade-algorithm-Python/blob/main/README.md#quick-look-at-the-results)
- [Troubleshooting](https://github.com/tasfiakatha/Face-recognition-system-with-OpenCV-LBPH-HaarCascade-algorithm-Python/blob/main/README.md#troubleshooting)
- [Explore the Notebook](https://github.com/tasfiakatha/Face-recognition-system-with-OpenCV-LBPH-HaarCascade-algorithm-Python/blob/main/README.md#explore-the-notebook)
- [Repository structure](https://github.com/tasfiakatha/Face-recognition-system-with-OpenCV-LBPH-HaarCascade-algorithm-Python/blob/main/README.md#repository-structure)
- [Contribution](https://github.com/tasfiakatha/Face-recognition-system-with-OpenCV-LBPH-HaarCascade-algorithm-Python/blob/main/README.md#controbution)
- [License](https://github.com/tasfiakatha/Face-recognition-system-with-OpenCV-LBPH-HaarCascade-algorithm-Python/blob/main/README.md#license)

## Project overview
This project performs face recognition using OpenCV's Local Binary Patterns Histograms (LBPH) and Haar Cascade for face detection. The model is trained on images of famous individuals, enabling it to identify and label faces in new images. The Haar Cascade model is used to detect faces in images, which are then classified by the LBPH algorithm.

**Objectives**
1. Detect and extract faces from images using Haar Cascades.  
2. Train an LBPH face recognizer to recognize known individuals.  
3. Evaluate the model on unseen images to test recognition accuracy.  

**Features**
1. Face Detection: Detect faces using a pre-trained Haar Cascade model.  
2. Face Recognition: Recognize faces using LBPH algorithm on grayscale facial ROIs.  
3. Confidence Score: Output the model's confidence in its predictions.  
4. Model Persistence: Save and load trained models and features for future predictions

## Methods
**Data Collection and Preprocessing**
Collected facial images of selected individuals from a designated dataset.  
Converted images to grayscale for faster processing and to improve accuracy.  
Used Haar Cascades to detect faces within images, generating face regions of interest (ROI).  

**Feature Extraction and Labeling**  
Created a list of features (image arrays) and corresponding labels by processing each face.  
Extracted key regions in each image to focus on recognizable facial features.  

**Face Recognition Model**  
Employed the LBPH algorithm to train a face recognition model on the extracted features and labels.  
Saved the trained model and associated arrays for testing and reuse.  

**Testing and Validation**  
Loaded the trained model to perform predictions on test images.  
Displayed recognized faces with a confidence score, visually identifying them with bounding boxes and labels.  

## Installation
1. Clone the repository:
   ![image](https://github.com/user-attachments/assets/bf29b954-d9b9-4a28-9bdc-a68b603a1c22)

2. Install the required libraries:
   ![image](https://github.com/user-attachments/assets/801a8ee6-8ccb-45da-82d4-3153d2a6433a)

3. Download Haar Cascade Model: Place the haar_face.xml file in the root directory or specify its path in the code. You can download it [here](https://github.com/opencv/opencv/tree/master/data/haarcascades).


## Quick Look at the Results
The model is able to successfully recognize individual faces from the validation images, with prediction labels and confidence scores displayed on detected faces. The confidence scores offer a measure of certainty, enhancing understanding of the model's performance.

**Correct face recognition**  
![image](https://github.com/user-attachments/assets/9ad9d61a-77bd-4aa7-b41f-831c05fa9be6)
![image](https://github.com/user-attachments/assets/dd51bcb3-f1e7-4668-8b56-f347ee0c134b)
![image](https://github.com/user-attachments/assets/5bd95753-3430-45ba-85fc-61ba7888c29a)

**Incorrect face recognition**   
![image](https://github.com/user-attachments/assets/30e08320-6631-4873-a31e-60fe816acb4d)

## Troubleshooting
**Model Not Found:** Ensure face_trained.yml is in the correct directory or specify the correct path.  
**No Faces Detected:** Check if haar_face.xml path is correct. Increase minNeighbors in detectMultiScale if faces are not detected.  
**Confidence Threshold:** Adjust confidence threshold if recognition is unreliable.  

## Explore the notebook
Explore the file [here](https://nbviewer.org/github/tasfiakatha/Face-recognition-system-with-OpenCV-LBPH-HaarCascade-algorithm-Python/blob/main/face_recognition.py)

## Repository structure
![image](https://github.com/user-attachments/assets/12ba1f74-8635-48ac-ac11-15fdb8551bc2)

## Contribution
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change or contribute.

## License
MIT License

Copyright (c) 2024 Tasfia Katha

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Learn more about [MIT](https://choosealicense.com/licenses/mit/) license
