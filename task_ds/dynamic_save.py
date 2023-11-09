import joblib
from datetime import datetime

def save_model(model):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = f'sales_model_{timestamp}.joblib'
    joblib.dump(model, filename)
    print(f'Model saved as {filename}')

def load_latest_model():
    # Assuming your models are in a directory called "models"
    list_of_files = glob.glob('models/*.joblib')
    latest_file = max(list_of_files, key=os.path.getctime)
    print(f'Loading {latest_file}')
    return joblib.load(latest_file)
