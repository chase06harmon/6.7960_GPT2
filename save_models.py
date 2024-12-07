from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    'gpt2',
    cache_dir=None,
    use_fast=True,
    revision='main',
    token=None,
    trust_remote_code=False
) 
tokenizer.save_pretrained('tokenizers/gpt-2')  # Save it locally