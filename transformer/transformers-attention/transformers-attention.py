import torch

def scaled_dot_product_attention(Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor) -> torch.Tensor:
    """
    Returns the scaled dot-product attention output.
    """
    b, q, d = Q.shape
    attention_score = Q @ K.transpose(-2, -1)
    scaled_attention_score = attention_score / (d**0.5)
    return torch.nn.Softmax(dim=-1)(scaled_attention_score) @ V