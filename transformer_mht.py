import math
import numpy as np


class MultiHeadAttention:
    def __init__(self, d_model: int, num_heads: int):
        """
        Initialize the Multi-Head Attention module.
        
        Args:
            d_model: Dimension of the model
            num_heads: Number of attention heads
        """
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        
        # Ensure that the model dimension is divisible by the number of heads
        assert self.d_k * num_heads == d_model, "d_model must be divisible by num_heads"
        
        # Weight matrices for linear transformations
        self.W_q = np.random.randn(d_model, d_model)
        self.W_k = np.random.randn(d_model, d_model)
        self.W_v = np.random.randn(d_model, d_model)
        self.W_o = np.random.randn(d_model, d_model)

    def scaled_dot_product_attention(self, Q: np.ndarray, K: np.ndarray, V: np.ndarray, mask: np.ndarray = None) -> tuple[np.ndarray, np.ndarray]:
        """
        Compute scaled dot-product attention.
        
        Args:
            Q: Query matrix (batch_size, num_heads, seq_len_q, d_k)
            K: Key matrix (batch_size, num_heads, seq_len_k, d_k)
            V: Value matrix (batch_size, num_heads, seq_len_v, d_v)
            mask: Mask to apply (batch_size, 1, seq_len_q, seq_len_k) or None
        
        Returns:
            output: Attention output (batch_size, num_heads, seq_len_q, d_v)
            attention_weights: Attention weights (batch_size, num_heads, seq_len_q, seq_len_k)
        """
        # Compute attention scores (Q·K^T / √d_k)
        scores = np.matmul(Q, K.transpose(0, 1, 3, 2)) / math.sqrt(self.d_k)
        
        # Apply mask if provided
        if mask is not None:
            scores = np.where(mask == 0, -1e9, scores)
        
        # Compute attention weights (softmax over the last dimension)
        attention_weights = np.exp(scores) / np.sum(np.exp(scores), axis=-1, keepdims=True)
        
        # Compute output (attention_weights·V)
        output = np.matmul(attention_weights, V)
        
        return output, attention_weights

    def split_heads(self, x: np.ndarray, batch_size: int) -> np.ndarray:
        """
        Split the last dimension into (num_heads, d_k).
        
        Args:
            x: Input tensor (batch_size, seq_len, d_model)
            batch_size: Batch size
        
        Returns:
            Split tensor (batch_size, num_heads, seq_len, d_k)
        """
        x = x.reshape(batch_size, -1, self.num_heads, self.d_k)
        return x.transpose(0, 2, 1, 3)

    def combine_heads(self, x: np.ndarray, batch_size: int) -> np.ndarray:
        """
        Combine the heads by concatenating them.
        
        Args:
            x: Input tensor (batch_size, num_heads, seq_len, d_k)
            batch_size: Batch size
        
        Returns:
            Combined tensor (batch_size, seq_len, d_model)
        """
        x = x.transpose(0, 2, 1, 3)
        return x.reshape(batch_size, -1, self.num_heads * self.d_k)

    def forward(self, Q: np.ndarray, K: np.ndarray, V: np.ndarray, mask: np.ndarray = None) -> tuple[np.ndarray, np.ndarray]:
        """
        Forward pass of the Multi-Head Attention module.
        
        Args:
            Q: Query matrix (batch_size, seq_len_q, d_model)
            K: Key matrix (batch_size, seq_len_k, d_model)
            V: Value matrix (batch_size, seq_len_v, d_model)
            mask: Mask to apply or None
        
        Returns:
            output: Attention output (batch_size, seq_len_q, d_model)
            attention_weights: Attention weights (batch_size, num_heads, seq_len_q, seq_len_k)
        """
        batch_size = Q.shape[0]
        
        # Linear transformations
        Q = np.matmul(Q, self.W_q)
        K = np.matmul(K, self.W_k)
        V = np.matmul(V, self.W_v)
        
        # Split into multiple heads
        Q = self.split_heads(Q, batch_size)
        K = self.split_heads(K, batch_size)
        V = self.split_heads(V, batch_size)
        
        # Scaled dot-product attention
        output, attention_weights = self.scaled_dot_product_attention(Q, K, V, mask)
        
        # Combine heads
        output = self.combine_heads(output, batch_size)
        
        # Final linear transformation
        output = np.matmul(output, self.W_o)
        
        return output, attention_weights


# Example usage
if __name__ == "__main__":
    # Hyperparameters
    d_model = 512
    num_heads = 8
    batch_size = 2
    seq_len = 10
    
    # Create Multi-Head Attention instance
    mha = MultiHeadAttention(d_model, num_heads)
    
    # Random input tensors
    Q = np.random.randn(batch_size, seq_len, d_model)
    K = np.random.randn(batch_size, seq_len, d_model)
    V = np.random.randn(batch_size, seq_len, d_model)
    
    # Forward pass
    output, attn_weights = mha.forward(Q, K, V)
    
    print(f"Input shape: {Q.shape}")
    print(f"Output shape: {output.shape}")
    print(f"Attention weights shape: {attn_weights.shape}")