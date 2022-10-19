def print_frog(word=None):
    '''None'''
    print(f"""
     _ _
     0_0 --{word}
    (|_|)
   /|   |\\""")

sound_list = ["ribbit", "merrr", "squeak"]

for fsound in sound_list:
    kermit = print_frog(fsound)
    print(kermit)
print()
