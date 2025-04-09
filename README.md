# AI4SAR Status Prediction

A machine learning model for predicting the status of subjects in search and rescue operations.

## Overview

AI4SAR Status Prediction is an API that uses machine learning to predict the likely status of a missing person in search and rescue scenarios. The model considers factors such as age, physical fitness, experience level, environment type, and time elapsed since the person was reported missing.

The model can predict several status categories:
- **Alive_Well**: Subject is alive and in good condition
- **Ill_Injured**: Subject is alive but injured or ill
- **DOA**: Deceased on arrival (fatality)
- **Not_Found**: Subject has not been located

## API Reference

### Prediction Endpoint

**URL**: `/predict`

**Method**: `POST`

**Request Body**:
```json
{
  "age": 35,
  "physical_fitness": "Good",
  "experience": "Experienced",
  "environment": "Forest",
  "total_hours": 24
}
```

**Parameters**:
- `age` (number): Age of the missing person
- `physical_fitness` (string): Level of physical fitness ("Good", "Poor", "na")
- `experience` (string): Level of experience in the environment ("Experienced", "Novice", "na")
- `environment` (string): Type of environment ("Forest", "Mountain", "Desert", "Urban", "Water", "na")
- `total_hours` (number): Hours since the person was reported missing

**Response**:
```json
{
  "status_code": "success",
  "status": "Alive_Well",
  "description": "Subject is alive and well, requiring standard evacuation procedures.",
  "probabilities": {
    "Alive_Well": 0.72,
    "DOA": 0.05,
    "Ill_Injured": 0.18,
    "Not_Found": 0.05
  }
}
```

### Health Check

**URL**: `/health`

**Method**: `GET`

**Response**:
```json
{
  "status": "healthy"
}
```

## Model Information

The prediction model is a stacking classifier that combines:
- Support Vector Machine (SVM)
- Logistic Regression

### Data Processing

Input features undergo the following preprocessing:
- Numerical features (age, total hours): Standardized
- Categorical features (physical fitness, experience, environment): One-hot encoded

### Performance

The model achieves approximately 67% accuracy in cross-validation, with class-specific performance:
- Alive_Well: 66% precision, 54% recall
- Ill_Injured: 68% precision, 87% recall
- DOA: Limited samples for reliable metrics
- Not_Found: Limited samples for reliable metrics
