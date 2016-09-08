import sys

def most(words):
    most = 0
    for w in words:
        if w.count("e") > most:
            most = w.count("e")
    return [w for w in words if w.count("e") == most]


def main():
    words = [w.strip() for w in sys.stdin]
    print("Words containing 17 letters: {}".format([w for w in words if len(w) == 17]))
    print("Words containing 18+ letters: {}".format([w for w in words if len(w) > 17]))
    print("Shortest word containing all vowels: {}".format(min([w for w in words if all(c in w for c in list("aeiou"))], key=len)))
    print("Words with 4 a's: {}".format([w for w in words if w.lower().count("a") == 4]))
    print("Words with 2+ q's: {}".format([w for w in words if w.count("q") >= 2]))
    print("Words containing cie: {}".format([w for w in words if "cie" in w]))
    print("Anagrams of angle: {}".format([w for w in words if all(c.lower() in w.lower() for c in list("angle")) and len(w) == 5 and w != "angle"]))
    print("Words ending in iary: {}".format(len([w for w in words if w.endswith("iary")])))
    print("Words with q but no u: {}".format([w for w in words if "q" in w.lower() and "u" not in w]))
    print("Words with most e's: {}".format(most(words)))


if __name__ == "__main__":
    main()
