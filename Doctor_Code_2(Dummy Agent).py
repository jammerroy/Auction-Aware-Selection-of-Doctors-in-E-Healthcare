import networkx as nx
import random
import matplotlib.pyplot as plt

nodes=16
Budget=75

G=nx.Graph()
G=nx.read_edgelist('nodes.txt',nodetype=int)	

for i in range(nodes):
	G.node[i]['influencing_flag']=0
	G.node[i]['influenced_flag']=0
	G.node[i]['marginal_cost']=0

cost=[]
for i in range(nodes):
	cost.append(random.randrange(8,10))

print 'Cost of Nodes:\n',cost

cost_till_now=0

nodes_considered=[]
for i in range(nodes):
	if (cost_till_now+cost[i])<=Budget:
		cost_till_now=cost_till_now+cost[i]
		nodes_considered.append(i)

#print nodes_considered

dummy_node_cost=Budget-cost_till_now
print dummy_node_cost
cost[len(nodes_considered)]=dummy_node_cost

#print cost

count=0

for i in range(nodes):
	count=0
	if G.node[i]['influencing_flag'] == 0:
		dic=G.neighbors(i)
		for items in dic:
			if G.node[items]['influenced_flag'] == 0:
				G.node[items]['influenced_flag']=1
				count=count+1
		G.node[i]['influencing_flag']=1
		G.node[i]['marginal_cost']=count	


marginal=[]
for i in range(nodes):
	marginal.append(G.node[i]['marginal_cost'])

#print 'Marginal Value of Nodes:',marginal

dummy_node_marginal=G.node[len(nodes_considered)]['marginal_cost']
print 'Marginal Cont. of Dummy Node',len(nodes_considered),G.node[len(nodes_considered)]['marginal_cost']

max_val=0.0
index=0
counter=2

B_whenby_2=open("B2.txt","w+")
B_whenby_3=open("B3.txt","w+")
B_whenby_4=open("B4.txt","w+")

for i in range(1):

	B=Budget/counter

	taken=[]
	before_this=0

	for i in range(nodes):
		max_val=0.0
		for j in range(nodes):	
			value=float(G.node[j]['marginal_cost'])/float(cost[j])
			if value>max_val:
				if j not in taken:
					max_val=value
			 		index=j
		if max_val==0:
			break
		#print 'Ratio:',max_val,'Node:',index

		if cost[index]<=B*(float(G.node[index]['marginal_cost'])/float((G.node[index]['marginal_cost']+before_this))):
			#print (float(G.node[index]['marginal_cost'])/float((G.node[index]['marginal_cost']+before_this)))
			taken.append(index)	

		before_this=before_this+G.node[index]['marginal_cost']

	print 'Nodes that have been selected:',taken
	
	cost_taken=[]

	for i in range(len(taken)):
		cost_taken.append(cost[taken[i]])

	#print 'Cost of the nodes that have been selected:',cost_taken	
	
	Quality=[]
	for i in range(len(taken)):
		Quality.append(random.randrange(1,5))

	#print 'Quality of the nodes generated randomly:',Quality

	ratio_array=[]
	for i in range(len(taken)):
		ratio_array.append(float(Quality[i])/float(cost_taken[i]))

	#print 'Ratio of Quality and Cost for each selected node:',ratio_array
	#print '\n'

	taken2=[]
	vector2=[]
	index=0
	max_val=0
	before_this=0

	for i in range(len(ratio_array)):
		max_val=0
		for j in range(len(ratio_array)):
			value=ratio_array[j]
			if value > max_val:
				if j not in taken2:
					max_val=value
					index=j
		taken2.append(index)
		before_this=before_this+max_val
		if cost[index]<=B*(max_val/before_this):
			#print 'Yes'
			vector2.append(taken[index])

	#print 'Nodes which further got selected:',vector2
	
	#### NEW PART

	F=nx.Graph()

	yes_vector=taken

	for i in range(len(yes_vector)):

		#print '\n'
		F=nx.read_edgelist('nodes.txt',nodetype=int)

		for j in range(16):
			F.node[j]['influencing_flag']=0
			F.node[j]['influenced_flag']=0
			F.node[j]['marginal_cost']=0

		print 'Calculating Payment for Node',yes_vector[i]
		F.remove_node(yes_vector[i])
		nodes=len(F)

		for j in range(nodes):
			count=0
			if j == yes_vector[i]:
				continue
			if F.node[j]['influencing_flag'] == 0:
				dic=F.neighbors(j)
				for items in dic:
					if F.node[items]['influenced_flag'] == 0:
						F.node[items]['influenced_flag']=1
						count=count+1
				F.node[j]['influencing_flag']=1
				F.node[j]['marginal_cost']=count	

		marginal2=[]
		for j in range(16):
			if j == yes_vector[i]:
				marginal2.append(-1)
			else:
				marginal2.append(F.node[j]['marginal_cost'])

		#print 'New Marginal Value of Nodes:',marginal2

		max_val=0.0
		index=0

		taken2=[]
		before_this=0
		value=0

		for j in range(16):
			max_val=0.0
			for k in range(16):
				if k == yes_vector[i]:
					continue
				value=float(F.node[k]['marginal_cost'])/float(cost[k])
				if value>max_val:
					if k not in taken2:
						max_val=value
						index=k
			if max_val==0:
				break
			#print 'Ratio:',max_val,'Node:',index
						
			if cost[index]<=B*(F.node[index]['marginal_cost']/F.node[index]['marginal_cost']+before_this):
				taken2.append(index)
			
			before_this=before_this+max_val	

		#print 'Nodes that have been selected without the certain node:',taken2
		
		before_this=0
		value=0
		max_val=0

		for j in range(len(taken2)):
			new_cost=G.node[yes_vector[i]]['marginal_cost']*(float(cost[taken2[j]])/float(marginal2[taken2[j]]))
			
			before_this=before_this+marginal2[taken2[j]]
			
			prob_cost=G.node[yes_vector[i]]['marginal_cost']*(float(B)/float(before_this))
			
			#print new_cost,prob_cost

			value=min(new_cost,prob_cost)
			if value>max_val:
				max_val=value

		print max_val

		if counter==2:
	  		B_whenby_2.write("%s %s %s\n" % (int(yes_vector[i]),(max_val),int(cost[yes_vector[i]])))
	  	if counter==3:
	  		B_whenby_3.write("%s %s %s\n" % (int(yes_vector[i]),(max_val),int(cost[yes_vector[i]])))
	  	if counter==4:
	  		B_whenby_4.write("%s %s %s\n" % (int(yes_vector[i]),(max_val),int(cost[yes_vector[i]])))
		
		#nx.draw(F,with_labels=True,node_size=500)
		#plt.show()

		F.clear()
		del marginal2[:]
		del taken2[:]
		
	counter=counter+1