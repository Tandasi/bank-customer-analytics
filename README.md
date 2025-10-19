# Bank Marketing ML Pipeline

A comprehensive machine learning pipeline for predicting bank marketing campaign success using Random Forest algorithm.

##  Project Overview

This project analyzes bank marketing data to predict whether customers will subscribe to term deposits. The model achieves **91.2% accuracy** using a Random Forest classifier.

##  Dataset

- **Source**: Bank Marketing Dataset
- **Size**: 45,211 records
- **Features**: 40+ customer attributes
- **Target**: Binary classification (yes/no for term deposit subscription)

##  Features

- **Complete ML Pipeline**: Data preprocessing, feature engineering, model training
- **Interactive Streamlit App**: Professional dark theme with real-time predictions
- **Comprehensive Analysis**: EDA, visualizations, and model evaluation
- **Production Ready**: Trained models saved for deployment

## Project Structure

```
├── bank_marketing_complete.ipynb  # Complete ML pipeline notebook
├── streamlit_deploy.py           # Interactive web application
├── data/
│   └── bank_marketing_complete.csv  # Dataset
├── final_model.joblib            # Trained Random Forest model
├── scaler.joblib                 # Feature scaler
├── label_encoder.joblib          # Label encoder
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

##  Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

##  Usage

### 🌐 View Online (Recommended)
**Live HTML Notebook**: [https://tandasi.github.io/bank-customer-analytics/bank_marketing_http.html](https://tandasi.github.io/bank-customer-analytics/bank_marketing_http.html)

### Run the Streamlit App
```bash
streamlit run streamlit_deploy.py
```

### View the Analysis
Open `bank_marketing_complete.ipynb` in Jupyter Notebook to explore the complete ML pipeline.

##  Model Performance

- **Accuracy**: 91.2%
- **Precision**: 85.7%
- **Recall**: 72.3%
- **F1-Score**: 78.5%
- **ROC-AUC**: 92.3%

##  Features

- **Professional UI**: Clean, modern interface with dark theme
- **Real-time Predictions**: Interactive customer data input
- **Comprehensive Analytics**: Performance metrics and visualizations
- **Enterprise Ready**: Production-grade deployment

##  License

This project is open source and available under the MIT License.

##  Contributing

Contributions are welcome! Please feel free to submit a Pull Request.