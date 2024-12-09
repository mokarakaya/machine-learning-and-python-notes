# Reinforcement Learning from Human Feedback (RLHF)

# Parameter-Efficient Fine-Tuning
- The general idea is to freeze some weights in the model and partially fine-tune it.
- This prevents catastrophic forgetting in large models 
- Enables fine-tuning with limited computing resources.
- Low-Rank Adaptation (LoRa)
  - Lora creates a small matrix for each weight matrix W in the model
  - W_delta = A . B 
  - A = mXr
  - B = rXn
  - r is rank hyper-parameter that controls the size of the adaptation.
  - We freeze the original W and only train W_delta.
  - Final weights become:
    - W += W_delta

