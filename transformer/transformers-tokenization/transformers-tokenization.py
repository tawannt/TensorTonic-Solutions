import numpy as np
from typing import List, Dict

class SimpleTokenizer:
    """
    A word-level tokenizer with special tokens.
    """
    
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0
        
        # Special tokens
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
    
    def build_vocab(self, texts: List[str]) -> None:
        """
        Build vocabulary from a list of texts.
        Add special tokens first, then unique words.
        """
        # YOUR CODE HERE
        self.id_to_word[0] = self.pad_token
        self.id_to_word[1] = self.unk_token
        self.id_to_word[2] = self.bos_token
        self.id_to_word[3] = self.eos_token

        unique = set()
        idx = 4
        for text in texts:
            for w in text.split():
                if w not in unique:
                    self.id_to_word[idx] = w
                    unique.add(w)
                    idx += 1
                    
        
        self.word_to_id = {v:k for k,v in self.id_to_word.items()}
        self.vocab_size = len(self.word_to_id)
        
    
    def encode(self, text: str) -> List[int]:
        """
        Convert text to list of token IDs.
        Use UNK for unknown words.
        """
        # YOUR CODE HERE
        tokens = text.split()

        tokenids = [
            self.word_to_id.get(t, self.word_to_id[self.unk_token]) 
            for t in tokens
        ]
        
        return tokenids
    
    def decode(self, ids: List[int]) -> str:
        """
        Convert list of token IDs back to text.
        """
        # YOUR CODE HERE

        tokens = [
            self.id_to_word.get(id, self.unk_token) 
            for id in ids
        ]
        
        return " ".join(tokens)
        
