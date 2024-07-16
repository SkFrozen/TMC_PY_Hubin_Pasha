text = "hhhabchghhh"
print(text[0] + text[1:-1].replace("h", "H") + text[-1])

word = "Hello"
word_2 = "TEST-STR"
print(
    "\n",
    word[2],
    "\n",
    word[-2],
    "\n",
    word[:5],
    "\n",
    word[:-2],
    "\n",
    word[::2],
    "\n",
    word[1::2],
    "\n",
    word[::-1],
    "\n",
    word[-1::-2],
    "\n",
    len(word),
)

print(
    "\n",
    word_2[2],
    "\n",
    word_2[-2],
    "\n",
    word_2[:5],
    "\n",
    word_2[:-2],
    "\n",
    word_2[::2],
    "\n",
    word_2[1::2],
    "\n",
    word_2[::-1],
    "\n",
    word_2[-1::-2],
    "\n",
    len(word_2),
)

print("\n", str(200)[-1], "\n", str(123)[-1], "\n", str(587)[-1])

print("\n", 123 // 10 % 10, "\n", 978 // 10 % 10)

print("\n", sum(map(int, str(123))), "\n", sum(map(int, str(555))))
