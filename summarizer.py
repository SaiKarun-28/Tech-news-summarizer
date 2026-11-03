import json
import os

from evaluate import load
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

MODEL_NAME = "facebook/bart-large-cnn"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, "data.json")

with open(DATA_PATH, "r", encoding="utf-8") as file:
    data = json.load(file)

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
rouge = load("rouge")


def generate_and_evaluate(articles):
    references = []
    predictions = []

    for article in articles:
        inputs = tokenizer(article["content"], return_tensors="pt", truncation=True)
        output = model.generate(**inputs, max_length=50, min_length=10, do_sample=False)
        summary_text = tokenizer.decode(output[0], skip_special_tokens=True)

        predictions.append(summary_text)
        if "reference_summary" in article:
            references.append(article["reference_summary"])

        print(f"Title: {article['headline']}")
        print(f"Generated Summary: {summary_text}\n")

    if len(references) == len(predictions):
        return rouge.compute(predictions=predictions, references=references)
    return {}


scores = generate_and_evaluate(data)
print(f"ROUGE Scores: {scores or 'Unavailable: data.json has no reference summaries.'}")
