M = 80
text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer semper porta
molestie. Vivamus nisl diam, malesuada id ligula sed, facilisis viverra tortor.
Nunc dolor ante, consequat eu porttitor id, malesuada at eros. Mauris vehicula
velit ac nibh semper tristique. Mauris lorem eros, condimentum a dolor et,
maximus euismod ex. Sed eget odio ultrices, suscipit elit eget, vehicula mauris.
Ut eget risus ut nibh tincidunt pharetra. Donec euismod nibh non pulvinar
sagittis. Donec sodales id turpis ac pulvinar. Vivamus vel eleifend risus. Donec
fringilla pharetra tempor."""

lines = text.split("\n")
wrong_line = -1
count = 0
for i in range(len(lines) - 1):
    if len(lines[i]) > M:
        wrong_line = i
        break
    count += (M - len(lines[i])) ** 2
if wrong_line == -1:
    print("Penalty : "+str(count))
else:
    print("Fail : Ligne "+str(wrong_line)+" trop longue : "+str(len(lines[wrong_line]))+" > "+str(M))
