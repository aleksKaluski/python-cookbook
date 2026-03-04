""""""
"""
1) POS Tagging 
Part Of Speech (POS) Tagging is the process of labeling each word in a corpus with its corresponding grammatical category 
(Noun, Verb, Adjective, etc.) based on both its definition and its context.

Methods for POS Tagging:
- Lexical Based Methods — Assigns the POS tag the most frequently occurring with a word in the training corpus.
- Rule-Based Methods — Assigns POS tags based on rules. For example, we can have a rule that says, words
  ending with “ed” or “ing” must be assigned to a verb. Rule-Based Techniques can be used along with
  Lexical Based approaches to allow POS Tagging of words that are not present in the training
  corpus but are there in the testing data.
- Probabilistic Methods — This method assigns the POS tags based on the probability of a particular tag sequence occurring.
  Conditional Random Fields (CRFs) and Hidden Markov Models (HMMs) are probabilistic approaches to assign a POS Tag.
- Deep Learning Methods — Recurrent Neural Networks can also be used for POS tagging.

Conditional Random Fields
A CRF is a Discriminative Probabilistic Classifiers. The difference between discriminative and generative models is that while 
discriminative models try to model conditional probability distribution, i.e., P(y|x), 
generative models try to model a joint probability distribution, i.e., P(x,y).
"""