"""Generating a random sequence of numbers for a lottery. """

import random

def generate_random_seq(start: int = 1, end: int = 50, count: int = 6):
    if count > (end-start+1):
        raise ValueError("count can not exceed from the range.")
    return random.sample(range(start, end+1),count)

randon_seq = generate_random_seq(1, 1000, 100)
print (f"randon sequence : {sorted(randon_seq)}")

#Multiple Draws (like multiple tickets)

def generate_random_seq_multiple(ticket_count: int = 5, start: int = 1, end: int = 50, count: int = 6):
    if count > (end-start+1):
        raise ValueError("count can not exceed from the range.")
    titcket = []
    for counts in range(ticket_count):
        titckets = random.sample(range(start, end+1),count)
        titcket.append(titckets)
    return titcket    

randon_seq_ticket = generate_random_seq_multiple(3, 1, 1000, 6)
for i, t in enumerate(randon_seq_ticket, 1):
    print (f"randon sequence ticket {i}: {sorted(t)}")