n = int(input())
answers = input()

adrian = "ABC"
bruno = "BABC"
goran = "CCAABB"

scores = {"Adrian": 0, "Bruno": 0, "Goran": 0}

for i in range(n):
    if answers[i] == adrian[i % len(adrian)]:
        scores["Adrian"] += 1
    if answers[i] == bruno[i % len(bruno)]:
        scores["Bruno"] += 1
    if answers[i] == goran[i % len(goran)]:
        scores["Goran"] += 1

max_score = max(scores.values())
print(max_score)

for name in ["Adrian", "Bruno", "Goran"]:
    if scores[name] == max_score:
        print(name)
