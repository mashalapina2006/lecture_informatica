def decode_rle(encoded_list):
    if not encoded_list:
        return []
decoded_list = []
for i in range(0, len(encoded_list), 2):
        value = encoded_list[i]        
        count = encoded_list[i + 1]   
        decoded_list.extend([value] * count)
return decoded_list
encoded_list = ["A", 12, "B", 4, "A", 6, "B", 1]
decoded_list = decode_rle(encoded_list)
print(decoded_list)
