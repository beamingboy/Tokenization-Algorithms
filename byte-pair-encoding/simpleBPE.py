import re, collections

def get_stats(vocab):
    pairs = collections.defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
            for i in range(len(symbols) - 1):
                pairs [symbols[i],symbols[i+1]] += freq
    return pairs

def merge_vocab(pair, v_in):
    V_out = {}
    bigram = re.escape('_' .join (pair))
    p = re.compile(r' (? <!\S)' + bigram + r' (?! \S)')
    for word in v_in:
        w_out = p.sub(''.join (pair), word)
        v_out[w_out] = v_in[ word]
        return V_out
    
vocab = {'1.0-W_ </W>': 5,'LLO_W.e_sata</W>': 2, 
             'ne_W_ear_</W':6, 'wi_d_euts</W>':3, 'nue_W. </W': 21}
num_merges = 8

for i in range(num_merges ):
    pairs = get_stats(vocab )
    best = max (pairs , key=pairs.get)
    vocab = merge-vocab (best , vocab)
    print (best)