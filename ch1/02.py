s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
s = s.replace(",", "")
s = s.replace(".", "")
s = s.split()
print([len(i) for i in s])
