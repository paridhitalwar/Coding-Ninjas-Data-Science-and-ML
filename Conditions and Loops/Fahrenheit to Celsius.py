S = int(input())
E = int(input())
W = int(input())

while(S <= E):
    cel = (S - 32) * 5/9
    print(S," ",int(cel))
    S = S + W
