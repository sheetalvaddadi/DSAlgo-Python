def is_palindrome(s):
  rp=0
  lp = len(s)-1
  while(rp<=lp):
    if(s[rp] ==s[lp]):
      rp+=1
      lp-=1
      continue
    else:
      return False
  return True