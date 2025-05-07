import numpy as np
from jiwer import wer, cer  # jiwer library is used to calculate WER and CER

# Function to calculate WER and CER for a list of reference and predicted transcriptions
def evaluate_model(references, predictions):
    """
    Evaluates the model's performance using WER (Word Error Rate) and CER (Character Error Rate)
    
    Args:
        references (list of str): List of reference transcriptions (ground truth)
        predictions (list of str): List of predicted transcriptions
    
    Returns:
        tuple: WER and CER scores
    """
    # Calculate WER and CER for all the references and predictions
    wer_score = np.mean([wer(ref, pred) for ref, pred in zip(references, predictions)])
    cer_score = np.mean([cer(ref, pred) for ref, pred in zip(references, predictions)])

    return wer_score, cer_score


# Example reference and predicted transcriptions (can be replaced with your actual data)
references = [
    "hello world", 
    "how are you", 
    "this is a test"
]

predictions = [
    "helo wrld", 
    "how r you", 
    "this is test"
]

# Evaluate the model
wer_score, cer_score = evaluate_model(references, predictions)

# Output the evaluation results
print(f"Word Error Rate (WER): {wer_score:.4f}")
print(f"Character Error Rate (CER): {cer_score:.4f}")

# Additional metrics: You can also print out the WER and CER for individual transcriptions
for i, (ref, pred) in enumerate(zip(references, predictions)):
    print(f"Example {i+1}:")
    print(f"  Reference: {ref}")
    print(f"  Prediction: {pred}")
    print(f"  WER: {wer(ref, pred):.4f}")
    print(f"  CER: {cer(ref, pred):.4f}")
    print()
