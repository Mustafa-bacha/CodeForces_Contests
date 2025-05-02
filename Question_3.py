def alice_wins_round(a, b, n):
    if a == 1 and b == n:
        return True
    if b == 1 and a == n:
        return False
    return a > b

def solve_case(n, s):
    alice_cards = []
    bob_cards = []
    for i in range(n):
        card_number = i + 1
        if s[i] == 'A':
            alice_cards.append(card_number)
        else:
            bob_cards.append(card_number)

    alice_has_unbeatable = False
    if alice_cards:
        for a in alice_cards:
            a_is_unbeatable = True
            for b in bob_cards:
                if not alice_wins_round(a, b, n):
                    a_is_unbeatable = False
                    break
            if a_is_unbeatable:
                alice_has_unbeatable = True
                break

    bob_has_dominant = False
    if bob_cards:
        for b in bob_cards:
            b_is_dominant = True
            for a in alice_cards:
                if alice_wins_round(a, b, n):
                    b_is_dominant = False
                    break
            if b_is_dominant:
                bob_has_dominant = True
                break

    if alice_has_unbeatable and not bob_has_dominant:
        return "Alice"
    else:
        return "Bob"

def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        s = input().strip()
        result = solve_case(n, s)
        results.append(result)
    for r in results:
        print(r)

if __name__ == "__main__":
    main()
