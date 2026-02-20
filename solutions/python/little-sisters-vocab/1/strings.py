def add_prefix_un(word):
    return 'un'+ word


def make_word_groups(vocab_words):
    prefix = ' :: ' + vocab_words[0]
    return prefix.join(vocab_words[0:])


def remove_suffix_ness(word):
    root = word[0:-4]
    if root.endswith('i'):
        definitely_word = root.replace('i','y')
    else:
        definitely_word = root
    return definitely_word



def adjective_to_verb(sentence, index):
    sentence_without_point = sentence.replace('.',' ')
    definitely_sentence = sentence_without_point.split()
    return definitely_sentence[index]+'en'

