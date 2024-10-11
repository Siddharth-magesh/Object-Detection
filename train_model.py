from ultralytics import YOLO
from config import Model_Name , Yaml_Path

def train_and_eval():
    model = YOLO(Model_Name)
    print("\n\nDownloaded the Model\n\n")
    model.train(
        data = Yaml_Path,
        epochs = 50,
    )
    print("\n\nModel Training Completed\n\n")
    metric = model.eval()
    print(metric)

if __name__ == '__main__':
    train_and_eval()