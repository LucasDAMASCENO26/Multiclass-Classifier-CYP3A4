import warnings
from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib
from lib.descriptor_gen import DescriptorGen

# Ignorar avisos de inconsistência de versão do Scikit-learn
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

app = Flask(__name__)

# Carregar o modelo treinado e o LabelEncoder
model = joblib.load('lgbm_model.pkl')
label_encoder = joblib.load('label_encoder.pkl')

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    molecule_smiles = data.get('smiles')
    
    if not molecule_smiles:
        return jsonify({'error': 'SMILES string is missing'}), 400
    
    try:
        # Gerar descritores a partir do SMILES
        desc_gen = DescriptorGen()
        desc = desc_gen.from_smiles(molecule_smiles)
        
        if desc is None:
            return jsonify({'error': 'Invalid SMILES string'}), 400
        
        desc = np.array(desc).reshape(1, -1)
        
        # Fazer a predição
        prediction = model.predict(desc)[0]
        
        # Decodificar a predição usando o LabelEncoder
        resultado = label_encoder.inverse_transform([prediction])[0]
        
        # Retornar o resultado da predição como JSON
        return jsonify({'prediction': resultado})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
