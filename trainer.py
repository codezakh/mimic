from textgenrnn import textgenrnn

textgen = textgenrnn()
textgen.train_from_file('./data/final_data.txt', num_epochs=1)
generated_texts = textgen.generate(n=5, temperature=0.2, return_as_list=True)
print(generated_texts)