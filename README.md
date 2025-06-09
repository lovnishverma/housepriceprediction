# House Price Prediction Web Application

A Flask-based web application that predicts house prices in Delhi using machine learning. The application uses a Random Forest Regressor model to estimate property prices based on various features like BHK, bathrooms, parking, price per square foot, and furnishing status.

## Features

- **Web Interface**: Clean and user-friendly web interface for inputting property details
- **Machine Learning**: Uses Random Forest Regressor for accurate price predictions
- **Real-time Predictions**: Instant price estimates based on user input
- **Responsive Design**: Works on desktop and mobile devices

## Technologies Used

- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn (Random Forest Regressor)
- **Data Processing**: pandas
- **Frontend**: HTML templates (Jinja2)
- **Dataset**: Delhi house price data (CSV format)

## Project Structure

```
house-price-predictor/
│
├── app.py                    # Main Flask application
├── delhi_house_price_ML.csv  # Dataset for training
├── templates/
│   ├── index.html           # Home page template
│   └── predict.html         # Prediction form and results template
├── static/                  # CSS, JS, images (if any)
└── README.md               # Project documentation
```

## Installation & Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/lovnishverma/housepriceprediction.git
cd housepriceprediction
```

### Step 2: Install Dependencies

```bash
pip install flask pandas scikit-learn
```

### Step 3: Prepare the Dataset

Ensure `delhi_house_price_ML.csv` is in the root directory. The CSV should contain the following columns:
- `id`: Unique identifier
- `BHK`: Number of bedrooms
- `Bathroom`: Number of bathrooms
- `Parking`: Number of parking spaces
- `Per_Sqft`: Price per square foot
- `Furnishing`: Furnishing status (encoded as numeric)
- `Price`: Target variable (house price)

### Step 4: Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

## Usage

1. **Home Page**: Navigate to `http://localhost:5000` to access the home page
2. **Prediction Form**: Go to `http://localhost:5000/form` or click the prediction link
3. **Input Details**: Fill in the property details:
   - BHK (Number of bedrooms)
   - Bathroom (Number of bathrooms)
   - Parking (Number of parking spaces)
   - Per_Sqft (Price per square foot)
   - Furnishing (Furnishing status as numeric value)
4. **Get Prediction**: Submit the form to get the predicted house price

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page |
| `/form` | GET | Prediction form page |
| `/predict` | POST | Process prediction and return results |

## Model Details

- **Algorithm**: Random Forest Regressor
- **Features**: BHK, Bathroom, Parking, Per_Sqft, Furnishing
- **Target**: House Price
- **Training**: Model is trained on each prediction request using the entire dataset

## Input Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| BHK | Integer | Number of bedrooms (e.g., 1, 2, 3, 4) |
| Bathroom | Integer | Number of bathrooms |
| Parking | Integer | Number of parking spaces |
| Per_Sqft | Float | Price per square foot |
| Furnishing | Integer | Furnishing status (encoded) |

## Important Notes

⚠️ **Security Warning**: The current implementation uses `eval()` to process form data, which poses security risks. Consider replacing with safer alternatives like `int()` or `float()` for production use.

## Potential Improvements

1. **Security**: Replace `eval()` with type-safe parsing
2. **Performance**: Cache the trained model instead of retraining on each request
3. **Validation**: Add input validation and error handling
4. **Database**: Use a proper database instead of CSV files
5. **Styling**: Enhance the frontend with CSS frameworks
6. **API**: Add REST API endpoints for programmatic access
7. **Logging**: Implement proper logging for monitoring and debugging

## Troubleshooting

### Common Issues

1. **Module Not Found**: Ensure all dependencies are installed
   ```bash
   pip install flask pandas scikit-learn
   ```

2. **CSV File Not Found**: Verify `delhi_house_price_ML.csv` is in the correct location

3. **Port Already in Use**: Change the port in app.py:
   ```python
   app.run(debug=True, port=5001)  # Use different port
   ```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For questions or support, please open an issue in the repository or contact the development team.

---

**Note**: This application is for educational and demonstration purposes. For production use, please implement proper security measures, error handling, and performance optimizations.
