bri = set(['Brasil','Russia','India'])
print('India' in bri)

print('USA' in bri)

bric = bri.copy()
print(bric)
bric.add('China')
print(bric)
print(bric.issuperset(bri))