import torch
from transformers import GPT2LMHeadModel,GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

text = 'Describe an encounter between a fantasy hero and a goblin'

inputs = tokenizer.encode(text, return_tensors = 'pt')

outputs = model.generate(inputs, max_length = 400, do_sample = True, temperature = 1, top_k = 50)

text = tokenizer.decode(outputs[0], skip_special_tokens = True)

print(text)