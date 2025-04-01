import pickle
from pathlib import Path
import pandas as pd

__version__ = "0.1.0"
BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/trained_pipeline-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)

def get_status_description(status):
    """Return a description based on the predicted status."""
    descriptions = {
        "Alive_Well": "Subject is alive and well, requiring standard evacuation procedures.",
        "DOA": "Subject is deceased on arrival, requiring body recovery procedures.",
        "Ill_Injured": "Subject is ill or injured, requiring medical intervention and evacuation.",
        "Not_Found": "Subject has not been located, requiring continued search efforts.",
        "na": "Status could not be determined with available information."
    }
    return descriptions.get(status, "Unknown status")

def predict_status(
    age: float,
    physical_fitness: str,
    experience: str,
    environment: str,
    total_hours: float
):

    input_data = pd.DataFrame({
        "Age": [age],
        "Physical Fitness": [physical_fitness],
        "Experience": [experience],
        "Environment": [environment],
        "Total Hours": [total_hours]
    })

    predicted_status = model.predict(input_data)[0]

    probabilities = {}
    if hasattr(model, 'predict_proba'):
        proba_values = model.predict_proba(input_data)[0]
        probabilities = {class_name: float(prob) for class_name, prob in zip(model.classes_, proba_values)}

    description = get_status_description(predicted_status)
    
    return {
        "status": predicted_status,
        "description": description,
        "probabilities": probabilities
    }