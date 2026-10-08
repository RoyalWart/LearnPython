playlist = ["Song A", "Song B", "Song C"]
playlist.append("Song D")
print(playlist[1:3])

scores = {"alex": 90, "sam": 75}
scores["jo"] = 88
for name, pts in scores.items():
    print(name, pts)

unique = set([1, 2, 2, 3, 3, 3])
print(unique)

print([n * n for n in range(6) if n % 2 == 0])
