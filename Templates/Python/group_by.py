a = "aaaabbccccaccb"
let = a[0]
count = 0
ans = ''
for l in a:
    if let == l:
        count += 1 
    else:
        ans += str(count) + let
        let = l
        count = 1
ans += str(count) + let
print(ans)
