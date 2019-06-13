# print("hello")


# class B:
#     def __init__(self, sentence):
#         """Initializes this partial parse.

#         @param sentence (list of str): The sentence to be parsed as a list of words.
#                                         Your code should not modify the sentence.
#         """
#         # The sentence being parsed is kept for bookkeeping purposes. Do not alter it in your code.
#         self.sentence = sentence
#         self.stack = [s for s in sentence[::-1]]
#         self.stack.insert(0, 'ROOT')
#         self.dependencies = []


# b = B(["parse", "this", "sentence"])


# l1 = [1, 2, 3, 4, 5, 6, 7]
# l2 = l1
# l1.pop(0)
# print(l1)
# print(l2)


import torch
import torch.nn as nn

embedding = nn.Embedding(10, 3)
# a batch of 2 samples of 4 indices each
input = torch.LongTensor([[1, 2, 4, 5], [4, 3, 2, 9]])
embedding(input)
print(input.size()[0])
batch_size = input.size()[0]
n_i, n_em = input.size()
print(batch_size)
print(n_i, n_em)
