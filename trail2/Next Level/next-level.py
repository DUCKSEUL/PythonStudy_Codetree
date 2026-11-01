class character:
    def __init__(self, id="codetree", level=10):
        self.id = id
        self.level = level

c1 = character()
print("user", c1.id, "lv", c1.level)

raw_id, raw_level = input().split()
raw_level = int(raw_level)

c1.id, c1.level = raw_id, raw_level
print("user", c1.id, "lv", c1.level)