def is_palindrome(s):
  left =0
  right = len(s)-1
  skip =0

  while (left<right):
    if s[left]==s[right]:
      left+=1
      right -=1
    else:
      skip+=1
      if s[left+1] == s[right]:
        left+=2
        right-=1
      elif s[left] ==s[right-1]:
        left+=1
        right -=2
    if skip ==2:
      return False
  return True