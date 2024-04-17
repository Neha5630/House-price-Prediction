from flask import Flask, request, render_template, jsonify
# Alternatively can use Django, FastAPI, or anything similar
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline
from src.category import data

application = Flask(__name__)
app = application

@app.route('/')
def home_page():
    return render_template('index.html')
@app.route('/predict', methods = ['POST', "GET"])

def predict_datapoint(): 
    
    if request.method == "GET": 
        return render_template("form.html")
    else: 
        
        from src.category import data
        
        if request.form.get("Name") not in data["Name_category"]:
            return render_template("form.html",message="Name type is not valid")
        if request.form.get("FuelType") not in data["FuelType_category"]:
            return render_template("form.html",message="FuelType type is not valid")
        if request.form.get("Gearbox") not in data["Gearbox_category"]:
            return render_template("form.html",message="Gearbox is not valid")
      
        
        
        datanew = CustomData( 
        Name =request.form.get("Name"),
        Mileage =float(request.form.get("Mileage")),
        FuelType =request.form.get("FuelType"),
        Year =float(request.form.get("Year")),
        Kms_Driven=float(request.form.get("Kms_Driven")),
        Gearbox=request.form.get("Gearbox"),
                             )
    new_data = datanew.get_data_as_dataframe()
    predict_pipeline = PredictPipeline()
    pred = predict_pipeline.predict(new_data)

    results = round(pred[0],2)

    return render_template("results.html", final_result = results)

if __name__ == "__main__": 
    app.run(host = "0.0.0.0", debug= True)

#http://127.0.0.1:5000/ in browser