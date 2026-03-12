# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import layers
# import pandas as pd
# import numpy as np
# import cv2
# import os
# from sklearn.model_selection import train_test_split

# # Load metadata
# df = pd.read_csv('data/HAM10000_metadata.csv')

# # Map diagnosis codes to your diseases
# diag_dict = {
#     'bkl': 'Benign Keratosis',  # Includes seborrheic keratosis
#     'nv': 'Melanocytic Nevus',
#     'df': 'Dermatofibroma',
#     'mel': 'Melanoma',
#     'vasc': 'Vascular Lesion',
#     'bcc': 'Basal Cell Carcinoma',
#     'akiec': 'Actinic Keratosis'
# }

# df['label_name'] = df['dx'].map(diag_dict)

# # Function to load and preprocess images
# def load_image(image_id, size=(224, 224)):
#     # Check both image folders
#     image_path = None
#     for folder in ['data/images_part1', 'data/images_part2']:
#         path = f'{folder}/{image_id}.jpg'
#         if os.path.exists(path):
#             image_path = path
#             break
    
#     if image_path is None:
#         return None
    
#     # Read and preprocess image
#     img = cv2.imread(image_path)
#     img = cv2.resize(img, size)
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     img = img / 255.0  # Normalize to [0,1]
#     return img

# # Create balanced dataset (limit to 500 per class for speed)
# balanced_data = []
# for label in df['label_name'].unique():
#     class_samples = df[df['label_name'] == label].head(500)
#     balanced_data.append(class_samples)

# df_balanced = pd.concat(balanced_data)

# # Load images and labels
# X = []
# y = []
# label_to_idx = {label: i for i, label in enumerate(df_balanced['label_name'].unique())}

# print("Loading images...")
# for idx, row in df_balanced.iterrows():
#     img = load_image(row['image_id'])
#     if img is not None:
#         X.append(img)
#         y.append(label_to_idx[row['label_name']])

# X = np.array(X)
# y = np.array(y)

# # Split data
# X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# # Build a simple CNN model
# def create_model(num_classes):
#     model = keras.Sequential([
#         # Feature extraction
#         layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
#         layers.MaxPooling2D((2, 2)),
        
#         layers.Conv2D(64, (3, 3), activation='relu'),
#         layers.MaxPooling2D((2, 2)),
        
#         layers.Conv2D(128, (3, 3), activation='relu'),
#         layers.MaxPooling2D((2, 2)),
        
#         # Classification
#         layers.Flatten(),
#         layers.Dense(128, activation='relu'),
#         layers.Dropout(0.5),
#         layers.Dense(num_classes, activation='softmax')
#     ])
    
#     model.compile(
#         optimizer='adam',
#         loss='sparse_categorical_crossentropy',
#         metrics=['accuracy']
#     )
    
#     return model

# # Create and train model
# print("Creating model...")
# model = create_model(len(label_to_idx))

# print("Training model...")
# history = model.fit(
#     X_train, y_train,
#     validation_data=(X_val, y_val),
#     epochs=10,  # Reduced for speed
#     batch_size=32
# )

# # Save the model
# model.save('model/skin_classifier.h5')

# # Save label mapping
# import json
# with open('model/class_labels.json', 'w') as f:
#     json.dump({str(i): label for label, i in label_to_idx.items()}, f)

# print("Model training complete! Saved to 'model/skin_classifier.h5'")


def iddfs(graph, start, goal):
    
    def dls(node, goal, depth, path, visited):
        if depth == 0:
            if node == goal:
                return path
            return None
        
        if depth > 0:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    result = dls(neighbor, goal, depth - 1, path + [neighbor], visited)
                    if result is not None:
                        return result
            visited.remove(node)
        return None

    max_depth = len(graph)
    
    for depth in range(max_depth):
        visited = set()
        result = dls(start, goal, depth, [start], visited)
        if result is not None:
            return result
    
    return None

