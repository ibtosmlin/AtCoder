#name#
# output0
#description#
# print(ret)
#body#
print(ret)
#prefix#
# print(0ret)
#end#

#name#
# output
#description#
# print(Yes/No)
#body#
print('Yes' if ret else 'No')
#prefix#
# print(1Yes/No)
#end#

#name#
# output2
#description#
# print(INF)
#body#
print(-1 if ret == INF else ret)
#prefix#
# print(2INF)
#end#

#name#
# output3
#description#
# print(joinret)
#body#
print('\n'.join(ret))
#prefix#
# print(3joinret)
#end#

#name#
# output4
#description#
# print(join(map(str(ret)
#body#
print('\n'.join(map(str, ret)))
#prefix#
# print(4join(map(str(ret)
#end#