import os, nltk, fitz, re
from nltk.sentiment import SentimentIntensityAnalyzer
from openai import OpenAI

# download VADER lexicon once
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()


def extract_pdf_text(path: str) -> str:
    """Read PDF text safely (auto⁐closes file to avoid Win32 lock)."""
    with fitz.open(path) as doc:
        return "\n".join(page.get_text() for page in doc)


def vader_sentiment(text: str):
    """Return {'Positive': p, 'Neutral': n, 'Negative': q}."""
    v = sia.polarity_scores(text)
    pos = max(v['compound'], 0)
    neg = max(-v['compound'], 0)
    neu = 1 - (pos + neg)
    return {"Negative": neg, "Neutral": neu, "Positive": pos}


def gpt_summary(text: str) -> str:
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        return '(OPENAI_API_KEY missing — summary skipped)'
    client = OpenAI(api_key=api_key)
    resp = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{
            'role': 'user',
            'content': (
                'Summarize the key financial insights and tone of this report in 120 words:\n\n'
                + text[:3000]
            )
        }],
        temperature=0.4,
        max_tokens=180
    )
    return resp.choices[0].message.content.strip()


def extract_company_name(text: str) -> str:
    """Try to extract company name from PDF content."""
    # crude regex: grab anything Title-case near 'Report' or 'Analysis'
    m = re.search(r'(\b[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+){0,2})\s+(?:Report|Analysis)', text)
    return m.group(1).strip() if m else '(Not Found)'
