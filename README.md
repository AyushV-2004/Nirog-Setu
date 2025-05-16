# NirogSetu

**Intelligent Healthcare Companion for Chronic Illness Management**

---

## Project Overview

NirogSetu is a multi-agent AI-powered healthcare platform designed to monitor, analyze, and guide patients with chronic illnesses in the comfort of their homes. Leveraging advanced machine learning models and natural language processing, it aims to improve patient care and promote health awareness through an intelligent mobile application and backend AI services.

---

## Key Features

- **Vision Transformer-based Monitoring:** Uses Vision Transformer (ViT) models to analyze patient posture and skin condition from images for early detection and tracking.
- **Symptom Tracking & Medical Q&A:** Large Language Models (LLMs) powered chatbot to understand patient symptoms, answer queries, and provide health advice.
- **Retrieval-Augmented Generation (RAG):** Integrates relevant medical literature to offer accurate, up-to-date responses.
- **Real-Time Wearable Data Integration:** (Planned) To process live data from wearables for continuous health monitoring.
- **Mobile App Interface:** Developed with Expo (React Native) for seamless patient interaction and symptom logging.

---

## Technologies Used

- **Machine Learning & AI:**  
  - Vision Transformers (ViT) via Hugging Face Transformers  
  - Large Language Models (LLMs) with LangChain and RAG methods  
  - OpenCV for image processing  
- **Mobile App:**  
  - React Native (Expo)  
- **Backend & Tools:**  
  - Python  
  - Hugging Face Hub  
  - LangChain

---

## Project Structure

NirogSetu/
├── mobile-app/ # React Native app source code
├── ml-models/ # Vision Transformer and LLM inference scripts
│ ├── vit_models/ # ViT model code and image inference scripts
│ ├── llm_models/ # LLM wrappers and RAG setup (planned)
│ ├── data/ # Sample/test images and datasets
│ └── requirements.txt
├── README.md # Project documentation
└── .gitignore



---

## Setup Instructions

### Mobile App

1. Navigate to `mobile-app/`
2. Run `npm install` or `yarn` to install dependencies
3. Start the app with: expo start


### ML Models

1. Navigate to `ml-models/`
2. Create and activate a Python virtual environment
3. Install dependencies: pip install -r requirements.txt
4. Run inference scripts, for example: python vit_models/infer.py data/test.jpg


---

## Important Notes

- **Data Privacy:** Patient data privacy and HIPAA compliance are paramount.
- **Model Training:** Currently uses pretrained models; fine-tuning with medical datasets is planned.
- **Environment:** Do **not** commit virtual environment folders (`venv/`) to Git; they are added to `.gitignore`.
- **Future Work:** Integration of wearable data, enhanced symptom tracking, and advanced medical advice generation.

---

## Contribution

Contributions and suggestions are welcome! Please open issues or submit pull requests.

---

## License

This project is licensed under the MIT License.

