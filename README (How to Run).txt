Email Spam Classifier — README

1. Open the notebook: Md_Emdadul_Hasan_Shishir_Email_Spam_Classifier.ipynb
2. Upload your kaggle.json (Kaggle API token) to Colab (if needed) and run the download cell.
3. Run cells sequentially (1 → 17).
4. The best performing model from this run is Random Forest (TF-IDF). Saved pipeline: /content/rf_tfidf_pipeline.joblib
5. For inference, load saved model with joblib.load('/content/rf_tfidf_pipeline.joblib') and call predict([clean_text(your_message)]).
