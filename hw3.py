word = (input("Enter word:")).lower()
h = list(word)
# print(h)
dic_in = {"a": h.count("a"),
          "b": h.count("b"),
          "c": h.count("c"),
          "d": h.count("d"),
          "e": h.count("e"),
          "f": h.count("f"),
          "g": h.count("g"),
          "h": h.count("h"),
          "i": h.count("i"),
          "j": h.count("j"),
          "k": h.count("k"),
          "l": h.count("l"),
          "m": h.count("m"),
          "n": h.count("n"),
          "o": h.count("o"),
          "p": h.count("p"),
          "q": h.count("q"),
          "r": h.count("r"),
          "s": h.count("s"),
          "t": h.count("t"),
          "u": h.count("u"),
          "v": h.count("v"),
          "y": h.count("y"),
          "z": h.count("z"),
          "w": h.count("w"),
          "x": h.count("x"),
          }
dic_out = {}
for x, y in dic_in.items():
    if y != 0:
        dic_out[x] = y
print(dic_out)
