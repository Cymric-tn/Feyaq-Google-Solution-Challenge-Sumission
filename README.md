# Feyaq-Google-Solution-Challenge-Sumission

**Introduction:**
-
School violence is a problem that plagues many of the schools in Tunisia. It is heart breaking to see the place where students should feel safe being a source of suffering for them. Most of this is caused by the lack of intervention by the supervisors. Feyaq, a word meaning "awake," aims to address this issue by using computer vision algorithms to detect violence and alert the ones in charge of the students.

**How the app will work:**
-

 The security camera in the school will supervise student activity and rate the risk percentage of violent activities. When the risk percentage reaches a certain threshold a notification will be sent to the supervisor who will judge if there is a fight or not with the security camera's feed that will open in the app. If there is indeed a fight going on the user will write a report that will be saved and will help improve the dataset and he will be able to call the authorities or emergencies or even stop the fight the fight himself depending on the situation.

**Computer Vision Model:**
-

For our model we will be using tensorflow, keras, opencv and numpy.

The model architecture consists of the following steps:

1.  **Input**:

-   The input to the model is a sequence of frames from a video, represented as a 4D tensor: (frames, height, width, channels).

2.  **Pre-trained VGG19**:

-   Each frame in the input sequence is passed through a pre-trained VGG19 model, which extracts high-level features from the frames.

3.  **Flattening and Grouping**:

-   The output from the VGG19 model for each frame is flattened to a 2D shape (frames, spatial_feature_size), where spatial_feature_size is the product of height, width, and channels.
-   These flattened features are grouped into sequences representing the spatial feature vectors for each frame.

4.  **LSTM Processing**:

-   The LSTM layer processes the sequence of spatial feature vectors. Each spatial feature vector represents an input at a time step, and the LSTM learns temporal patterns in the sequence.

5.  **Time-Distributed Dense Layer**:

-   The LSTM output sequences are passed through a time-distributed dense layer, which helps in learning complex relationships between the spatial features across time steps.

6.  **Global Average Pooling**:

-   The output sequences from the dense layer are globally averaged along the temporal dimension to obtain a fixed-length representation of the entire sequence.

7.  **Output Layer**:

-   Finally, the averaged representation is passed through a dense layer with sigmoid activation to obtain the probability of violence existence in the given video.

**Dependencies:**
-
- Tensorflow: For the computer vision technology
- Flutter: For the mobile app.
- Google clouds: To store the data of the cameras.
- Firebase: To connect between the app,the cameras and the deep learning algorithm.
 
