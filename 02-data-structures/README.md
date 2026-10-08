# 02 · Data Structures

Programs need to hold *collections* of things: a playlist, an inventory,
a leaderboard.

## list: ordered, changeable
```python
inventory = ["sword", "shield", "potion"]
inventory.append("map")
inventory[0]          # 'sword'
inventory[-1]         # 'map' (last item)
inventory[1:3]        # slicing: ['shield', 'potion']
len(inventory)
```

## tuple: ordered, NOT changeable
```python
position = (10, 20)
x, y = position       # unpacking
```

## dict: key → value
```python
player = {"name": "Alex", "hp": 100}
player["hp"] -= 10
player.get("mana", 0)   # safe lookup with default
for key, value in player.items():
    print(key, value)
```

## set: unique items, no order
```python
tags = {"fps", "co-op", "fps"}   # duplicates vanish
a = {1, 2, 3}; b = {2, 3, 4}
a & b    # intersection {2, 3}
a | b    # union
```

## Comprehensions: build collections in one line
```python
squares = [n * n for n in range(5)]            # [0, 1, 4, 9, 16]
evens   = [n for n in range(10) if n % 2 == 0]
lengths = {w: len(w) for w in ["hi", "python"]}
```

## Why this matters
Choosing the right structure makes code shorter and faster. Need
uniqueness? set. Need lookup by name? dict. Need order? list.

## Your turn
`pytest 02-data-structures`
