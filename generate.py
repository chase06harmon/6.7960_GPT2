from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig

model_path = 'pathtomodel'
def main():
    # Load a pre-trained model and tokenizer
    model = AutoModelForCausalLM.from_pretrained(model_path)
    print('-1')
# Load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    # print('0')
    # Verify loading
    # print(model.config)
    prompt = ""
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids

    generation_config = GenerationConfig.from_pretrained("/nobackup/users/paulg9/Deep_learning_project/saved_model.ckpt/")
    # print('1')
    # Generate with custom configuration
    output_ids = model.generate(input_ids, generation_config=generation_config)
    # print('2')
    for _ in range(25):
        generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
        # print('3')
    
        print(generated_text)

    # print(generated_text)


if __name__ == "__main__":
    main()
