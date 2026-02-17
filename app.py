insha = input ("Bandika insha yako hapa:\n")
print("\nInachambua insha yako...\n")
maneno = len(insha.split())
sentensi = insha.count(".") + insha.count("!")+ insha.count("?")
punctuation_missing = False
if sentensi == 0 or max(lens(s) for s in insha.split(". ")) > 120:
    punctuation_missing = True
words= insha.lower().split()
word_counts = {}
for W in words:
    word_counts[W] = word_counts.get(W, 0) + 1
repeated_words = {W: c for W, c in word_counts.items()if c > 3}
score = 0
if maneno >= 100:
    score += 10
elif maneno >= 50:
    score += 5
if sentensi >= 3:
    score += 10
elif sentensi >=1:
    score += 5
if not punctuation_missing:
    score += 10
if len(repeated_words) == 0:
    score += 10
else:
    score += max(0, 10 - len(repeated_words)) 
print("Insha yako ina", maneno, "maneno.")
print("Ina takribani", sentensi, "sentensi.\n")
print("Score ya jumla: ", score, "/40\n") 
print("Maoni ya Awali:")
if maneno < 100:
    print("- Ongeza maneno zaidi ili insha iwe ndefu.")
else:
    print("- Urefu wa insha ni mzuri.")

if sentensi < 3:
    print("- Tumia sentensi zaidi kueleza mawazo yako.")
else:
    print("- Muundo wa sentensi unaonekana sawa.")

if punctuation_missing:
    print("- Hakikisha unatumia alama za uandishi vizuri (., !, ?).")

if repeated_words:
    print("- Maneno yafuatayo yamerudiwa mara nyingi:")
    for w, c in repeated_words.items():
        print(f"  • {w} ({c} mara)")