print('-------------------------------')
d = {'simple_key' :'hello'}
print(d['simple_key'])
print('-------------------------------')
d = {'k1' :{'k2' :'hello'}}
print(d['k1']['k2'])
print('-------------------------------')
d = {'k1' :[{'nest_key' : ['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])
print('-------------------------------')
d = {'k1' :[1,2,{'k2' :['this is tricky' ,{'tough' :[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])
print('-------------------------------')
