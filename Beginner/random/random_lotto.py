import random
def generate_lotto_numbers():
    lotto_numbers = random.sample(range(1,46), 6)
    lotto_numbers.sort()
    return lotto_numbers

print('이번주 로또 번호:',generate_lotto_numbers())