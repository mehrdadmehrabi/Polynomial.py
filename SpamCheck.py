class SpamCheck:
    
    def __init__(self, string):
        self.words = string.split()

        self.spam_count = 0
        for word in self.words:

            cap_count = 0
            chars_counts = {}
            has_vowel = False
            
            is_spam = False
            for char in word: 
                if "A" <= char <= "Z":
                    cap_count += 1
                    if cap_count >= 2:
                        is_spam = True
                        break

                if not char.isalpha():
                    is_spam = True
                    break

                char = char.lower()
                if char in chars_counts:
                    chars_counts[char] += 1
                    if chars_counts[char] >= 3:
                        is_spam = True
                        break
                else:
                    chars_counts[char] = 1

                if char.lower() in ["a", "e", "i", "o", "u"]:
                    has_vowel = True
            
            if is_spam:
                self.spam_count += 1
            else:
                if not has_vowel:
                    self.spam_count += 1


    def __str__(self):
        return str(self.spam_count)


print(SpamCheck("Takhfif VIZHEEEEE Porteghal dr Link zir:"))
print(SpamCheck("AGAR Mmmmmmmatn Zir ro baraye 3 nfr nafresti gooooshit hack mishe"))
