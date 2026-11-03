# Tech News Summarizer

An automated NLP tool that generates concise, fact-checked, one-sentence summaries of technology news articles to streamline content triage for busy professionals.

## Project Overview
This project addresses the challenge of information overload by leveraging modern Natural Language Processing (NLP) techniques to distill complex technology articles into actionable insights. It serves as a proof-of-concept for implementing and evaluating a production-ready summarization pipeline.

## Approach
- **Core Model:** Utilizes a pre-trained BART (Bidirectional and Auto-Regressive Transformers) model from the HuggingFace `transformers` library, optimized for summarization tasks.
- **Evaluation:** Implements a quantitative evaluation pipeline using the ROUGE metric to measure semantic similarity against reference summaries, complemented by manual qualitative assessments to ensure factual consistency.

## Prerequisites
- Python 3.9+
- `pip`

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/tech-news-summarizer.git
   cd tech-news-summarizer
   ```
2. Install the required dependencies:
   ```bash
   pip install transformers torch evaluate rouge_score
   ```

## Usage
1. Prepare your data by populating `data.json` with your article text and reference summaries.
2. Execute the summarization and evaluation script:
   ```bash
   python summarizer.py
   ```
The output will display the generated summaries in the console, followed by the computed ROUGE metrics.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
