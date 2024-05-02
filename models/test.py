# import torch
# from transformers import GPT2LMHeadModel, GPT2Tokenizer

# path = "medical_chatbot"
# device = "cpu"
# tokenizer = GPT2Tokenizer.from_pretrained(path)
# model = GPT2LMHeadModel.from_pretrained(path, local_files_only=True).to(device)

# prompt_input = (
#     "The conversation between human and AI assistant.\n"
#     "[|Human|] {input}\n"
#     "[|AI|]"
# )
# sentence = prompt_input.format_map({'input': "what is parkinson's disease?"})
# inputs = tokenizer(sentence, return_tensors="pt").to(device)

# with torch.no_grad():
#     beam_output = model.generate(**inputs,
#                                  min_new_tokens=1,
#                                  max_length=512,
#                                  num_beams=3,
#                                  repetition_penalty=1.2,
#                                  early_stopping=True,
#                                  eos_token_id=198
#                                  )
#     print(tokenizer.decode(beam_output[0], skip_special_tokens=True))
