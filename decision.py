def label_trend(trend_dir: str) -> int:
    return 1 if trend_dir.lower() == 'up' else -1


def label_sentiment(sentiment_probs: dict) -> int:
    pos = sentiment_probs.get('Positive', 0)
    neg = sentiment_probs.get('Negative', 0)
    if pos > neg:
        return 1
    if neg > pos:
        return -1
    return 0  # Neutral


def recommend(trend_dir: str, sentiment_probs: dict):
    t = label_trend(trend_dir)
    s = label_sentiment(sentiment_probs)
    if t == 1 and s == 1:
        return 'BUY', 1.0
    if t == -1 and s == -1:
        return 'SELL', -1.0
    return 'HOLD', 0.0
