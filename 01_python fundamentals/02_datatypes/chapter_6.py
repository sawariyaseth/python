chai_type = "Ginger chai"
customer_name = "Priya"

print(f"Order for {customer_name} : {chai_type} please !")

chai_description = "Aromatic_and_Bold"
# String formatting with f-strings
# String slicing:
print(f"first word: {chai_description[:8]}")
print(f"last word: {chai_description[13:]}")
print(f"reversed word: {chai_description[::-1]}")
# [:8] - first 8 characters
# [12:] - from index 12 to end
# [::-1] - reverses the string

label_text = "Chai Spécial"
encoded_label= label_text.encode("utf-8")
print(f"Encoded label: {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")
# encode("utf-8") converts the string to bytes (notice the é becomes \xc3\xa9)
# decode("utf-8") converts bytes back to string