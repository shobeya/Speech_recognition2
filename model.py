import numpy as np

class DummyAcousticModel:
    def __init__(self):
        pass

    def predict(self, features):
        # Simulate output logits for a single frame (1, 30)
        logits = np.random.rand(1, 30)  # Random logits for this example
        return logits

class CTCDecoder:
    def __init__(self, blank_token=0):
        self.blank_token = blank_token
    
    def decode_greedy(self, logits):
        # Apply softmax to logits to get probabilities
        logits = np.exp(logits) / np.sum(np.exp(logits), axis=-1, keepdims=True)  # Softmax on logits
        # Pick the token with the highest probability at each time step
        best_sequence = np.argmax(logits, axis=-1)
        
        # Ensure best_sequence is iterable even if it's a single token
        if isinstance(best_sequence, np.int64):
            best_sequence = [best_sequence]

        # Decode the best sequence (ignore the blank tokens)
        transcription = ''.join([chr(65 + token) for token in best_sequence if token != self.blank_token])
        
        print("Greedy transcription:", transcription)
        return transcription

# Main Speech Recognition Model with Greedy Decoder
class SpeechRecognitionModel:
    def __init__(self, acoustic_model, ctc_decoder, transformer_lm, device='cpu'):
        self.acoustic_model = acoustic_model
        self.ctc_decoder = ctc_decoder
        self.transformer_lm = transformer_lm
        self.device = device
        
    def predict(self, features, decode_method='greedy', rescore=False):
        # Step 1: Get the logits from the acoustic model
        logits = self.acoustic_model.predict(features)
        print("Logits from acoustic model:", logits)
        print("Logits shape:", logits.shape)
        
        # Step 2: Use the CTC Decoder to get the transcription
        if decode_method == 'greedy':
            transcription = self.ctc_decoder.decode_greedy(logits[0])
        else:
            raise ValueError("Unsupported decode method")
        
        return transcription

# Main execution logic
if __name__ == '__main__':
    # Create a dummy acoustic model
    acoustic_model = DummyAcousticModel()
    
    # Create a CTC Decoder with blank token index 0
    ctc_decoder = CTCDecoder(blank_token=0)
    
    # Dummy transformer language model (Replace with actual LM if necessary)
    transformer_lm = None  # Not used in this example
    
    # Create a speech recognition model
    model = SpeechRecognitionModel(acoustic_model, ctc_decoder, transformer_lm, device='cpu')
    
    # Simulated feature input (replace with actual speech features)
    features = np.random.rand(1, 30)  # Example feature with shape (1, 30)
    
    # Predict the transcription using the model
    transcription = model.predict(features, decode_method='greedy', rescore=False)
    
    # Print the transcription
    print("Transcription:", transcription)
