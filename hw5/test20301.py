from pattern.web import Facebook, NEWS, COMMENTS, LIKES, FRIENDS

fb = Facebook(license='CAAEuAis8fUgBAGvbgzlR88GbrThcUGshnz9njXesze8zWbc6ha9heTCKuHNE3KmGdrZCpTitFpFQwlIA5DN9b1kfYtueew9d5N74EKGfGjqGu8E8Ux2168sfjrsJ3QFi9pNG5DL4yBvWrEEmF9aOoTCIWfW8tCpyT9LXPKK61pkH4E5R0D')
me = fb.profile(id=None) # (id, name, date, gender, locale, likes)-tuple
count=0
for post in fb.search(100000008147254, type=NEWS, count=1000):
    count+=1
    print post.description
    print repr(post.id)
    print repr(post.date)
    print repr(post.text)
    print repr(post.url)
    if post.comments > 0:
        print '%i comments' % post.comments 
        print [(r.text, r.author) for r in fb.search(post.id, type=COMMENTS)]
    if post.likes > 0:
#        print post.text
        print '%i likes' % post.likes 
        print [r.author for r in fb.search(post.id, type=LIKES)]
