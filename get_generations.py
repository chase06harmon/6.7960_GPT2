from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig
from datasets import load_dataset

from huggingface_hub import login

hf_token = "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"

# Log in using the token
login(token=hf_token)
username = "chaseharmon"
repo_name = "shakespeare_gpt2.0"

# Path to the directory where the model is saved
model_dir = "../tmp/test-clm/"

# Load the model
model = AutoModelForCausalLM.from_pretrained(model_dir)

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("gpt2")
generation_config = GenerationConfig.from_pretrained(f"{username}/{repo_name}")
dataset = load_dataset("chaseharmon/6.7960_Shakespeare")

# Extract the text column (assuming it contains the relevant text)
text_data = dataset["train"]
result = []
for prompt in text_data['src'][:100]:
  input_ids = tokenizer(prompt, return_tensors="pt").input_ids
  output_ids = model.generate(input_ids, generation_config=generation_config)
  generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
  result.append((prompt, generated_text))


for prompt, response in result:
  print(f"Prompt: {prompt}\nResponse: {response}")
  print()