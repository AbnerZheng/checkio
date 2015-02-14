i=lambda x:[e for e in range(2,x) if x%e==0]
golf=lambda x:[e for e in range(x+1,98689) if str(e)[::-1]==str(e) and not i(e)][0]
