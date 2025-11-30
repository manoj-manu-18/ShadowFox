import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForMaskedLM, pipeline

def run_gpt2():
    print("\n--- GPT-2 Text Generation ---\n")
    model_name = "gpt2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

    prompt = "Explain artificial intelligence in simple terms."
    outputs = generator(prompt, max_length=50, temperature=0.7, num_return_sequences=1)

    print("Prompt:", prompt)
    print("Generated Text:\n", outputs[0]["generated_text"])


def run_bert():
    print("\n--- BERT Masked Word Prediction ---\n")
    model_name = "bert-base-uncased"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForMaskedLM.from_pretrained(model_name)

    fill_mask = pipeline("fill-mask", model=model, tokenizer=tokenizer)

    sentence = "The capital of France is [MASK]."
    outputs = fill_mask(sentence)

    print("Sentence:", sentence)
    print("Predictions:")
    for out in outputs:
        print(f"  {out['token_str']} (prob: {out['score']:.4f})")


if __name__== "__main__":
    print("Choose a demo:")
    print("1. GPT-2 (Text Generation)")
    print("2. BERT (Masked Word Prediction)")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        run_gpt2()
    elif choice == "2":
        run_bert()
    else:
        print("Invalid choice. Run again and select 1 or 2.")