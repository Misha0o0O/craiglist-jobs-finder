# code for creating tokenizer to change raw bytes into Byte-Pair encoding




text = "Ｕｎｉｃｏｄｅ! 🅤🅝🅘🅒🅞🅓🅔‽ 🇺‌🇳‌🇮‌🇨‌🇴‌🇩‌🇪! 😄 The very name strikes fear and awe into the hearts of programmers worldwide. We all know we ought to “support Unicode” in our software (whatever that means—like using wchar_t for all the strings, right?). But Unicode can be abstruse, and diving into the thousand-page Unicode Standard plus its dozens of supplementary annexes, reports, and notes can be more than a little intimidating. I don’t blame programmers for still finding the whole thing mysterious, even 30 years after Unicode’s inception."
tokens = text.encode("utf-8")
tokens = list(map(int,tokens))

#print(tokens)

def merging_pairs(ids):
    merged_units = []
    # merging pairs together
    for symbol in zip(ids, ids[1:]):
       merged_units.append(symbol)

    return merged_units


def pattern_check(merged_units):
    repeated = {}
    i = 0
    unit = 0
    size = len(merged_units)
    
    
    # Algorthim to slove how many dupilcates of characters common within the string of text
    while i != size:
        counter = 0
        inner_loop = size
        while inner_loop != 0:
         if merged_units[i] == merged_units[inner_loop - 1]:
            counter = counter + 1  
         inner_loop = inner_loop - 1
         if inner_loop == 0:
            repeated[merged_units[i]] =+ counter      
        i = i + 1

    return repeated

merged_units = merging_pairs(tokens)
most_common_pairs_repeated = pattern_check(merged_units)
get_top_pair = max(most_common_pairs_repeated, key=most_common_pairs_repeated.get)

def merger_swap(ids,top_pair,idc):
    swapped_most_occuring_pair = []
    i = 0
    arr_size = len(ids)
    while i != arr_size:
       if ids[i] == top_pair[0]:
        if ids[i + 1] == top_pair[1]:
           swapped_most_occuring_pair.append(idc)    
       else:
          swapped_most_occuring_pair.append(ids[i])
       i = i + 1
    return swapped_most_occuring_pair

# 256 is used as the vocba to indentify the most occuring pair within the list

replaced_with_256 = merger_swap(tokens,get_top_pair,256)
#print("total token:",len(tokens))
print(len(most_common_pairs_repeated))
print("new total tokens:", len(replaced_with_256))

vocab_size = 276 # the desired
num_merges = vocab_size - 256
ids = list(tokens)

merges = {} # (int, int) -> int
for i in range(num_merges):
   stats = pattern_check(merging_pairs(ids))
   pair = max(stats, key=stats.get)
   idx = 256 + i
   print(f"merging {pair} into a new token {idx}")
   ids = merger_swap(ids, pair, idx)
   merges[pair] = idx
print(merges)
#print(len(replaced_with_256)) 
# This part of the loop check thorough each item within the array for the most common occourance within the list.        
# This part of the function now searches throguh the list of the most occuring pairs and merger them then swap for single type
