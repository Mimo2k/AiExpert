# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml, load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.neural_network import MLPClassifier

def logistic_regression_mnist():
    print("=== Logistic Regression on MNIST Dataset ===")

    # Load the MNIST dataset
    mnist = fetch_openml('mnist_784', version=1, as_frame=True)
    X = mnist.data / 255.0  # Normalize pixel values
    y = mnist.target.astype(int)  # Convert labels to integers

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Logistic Regression
    model = LogisticRegression(max_iter=10000)
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Logistic Regression Accuracy: {accuracy:.4f}")

    # Visualize predictions
    print("Displaying 5 sample predictions from MNIST test set...")
    for i in range(5):
        try:
            plt.imshow(X_test.iloc[i].values.reshape(28, 28), cmap='gray')
            plt.title(f"Predicted: {y_pred[i]}, Actual: {y_test.iloc[i]}")
            plt.axis('off')
            plt.show()
        except Exception as e:
            print(f"Error displaying image {i}: {e}")

def mlp_classifier_digits():
    print("\n=== MLP Classifier on Digits Dataset ===")

    # Load digits dataset
    digits = load_digits()
    X, y = digits.data, digits.target

    # Visualize first 10 digits
    plt.figure(figsize=(10, 5))
    for i in range(10):
        plt.subplot(2, 5, i+1)
        plt.imshow(digits.images[i], cmap='gray')
        plt.title(f'Digit: {digits.target[i]}')
        plt.axis('off')
    plt.tight_layout()
    plt.savefig('digits_sample.png')
    plt.close()

    # Prepare train/test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Define and train MLP
    mlp = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=500, activation='relu', solver='adam', random_state=42)
    mlp.fit(X_train_scaled, y_train)

    # Evaluate the model
    y_pred = mlp.predict(X_test_scaled)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(10, 7))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title("Confusion Matrix - MLP Classifier")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    plt.savefig("confusion_matrix_mlp.png")
    plt.close()

    # Visualize predictions
    print("Displaying 10 predictions from Digits test set...")
    plt.figure(figsize=(12, 6))
    for i in range(10):
        plt.subplot(2, 5, i+1)
        plt.imshow(X_test[i].reshape(8, 8), cmap='gray')
        plt.title(f'True: {y_test[i]}\nPred: {y_pred[i]}')
        plt.axis('off')
    plt.tight_layout()
    plt.savefig('predictions_mlp.png')
    plt.close()

    print(f"MLP Classifier Accuracy: {mlp.score(X_test_scaled, y_test) * 100:.2f}%")

def main():
    print("=== ML Project: Handwritten Digit Recognition ===")
    logistic_regression_mnist()
    mlp_classifier_digits()
    print("\nProject completed. All reports and visualizations saved.")

if __name__ == "__main__":
    main()
