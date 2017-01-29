import parse_input
import random
import math

# X     1x64
# wji   64x8
# netj  1x8
# y     1x8
# wkj   8x3
# netk  1x3
# z     1x3
#lr learning rate

def sigmoid(v):
    return math.tanh(v)

def sigmoid_prime(v):
    return 1-(math.tanh(v)*math.tanh(v))


def forward_propagation(d,nH,c,x,wji,wkj):
	netj=[0]*nH
	y=[0]*nH
	for j in xrange(nH):
		for i in xrange(d):
			netj[j]+=x[i]*wji[j][i]	
		y[j]=sigmoid(netj[j])
		
	netk=[0]*c
	z=[0]*c
	for k in xrange(c):
		for j in xrange(nH):
			netk[k]+=y[j]*wkj[k][j]	
		z[k]=sigmoid(netk[k])
	
	return (netj,y,netk,z)

def backward_propagation(d,nH,c,x,netj,y,netk,z,t,wji,wkj,lr):

	delta_wkj=[[0 for j in range(nH)] for k in range(c)]
	delta_wji=[[0 for i in range(d)] for j in range(nH)]
	
	delta_k=[0 for k in range(c)]
	delta_j=[0 for j in range(nH)]
	
	for k in xrange(c):
		delta_k[k]=(t[k]-z[k])*sigmoid_prime(netk[k])
		for j in xrange(nH):
			delta_wkj[k][j]=lr*delta_k[k]*y[j]
			
		
	for j in xrange(nH):
		for k in xrange(c):
			delta_j[j]+=delta_k[k]*wkj[k][j]*sigmoid_prime(netj[j])
		
	
	for j in xrange(nH):
		for i in xrange(d):
			delta_wji[j][i]=lr*delta_j[j]*x[i]
	
	return (delta_wji,delta_wkj)
	
def update_weights(d,nH,c,wji,wkj,delta_wji,delta_wkj):
	for j in xrange(nH):
		for i in xrange(d):
			wji[j][i]+=delta_wji[j][i]
	
	for k in xrange(c):
		for j in xrange(nH):
			wkj[k][j]+=delta_wkj[k][j]
	return (wji,wkj)
		

def neural_net(X,n,nH,d,t,lr,theta):


    	iterations = 1000000

	W1=[]
	W01=[]
	W2=[]
	W02=[]
	d=65
	nH=9
	c=2
	
    	for it in xrange(iterations):
		total=0
		mc=0
		for t in xrange(len(X)):
			if(it==0):
				w1=[[random.uniform(0, 1) for i in range(d)] for j in range(nH)]
				W1.append(w1)
				w2=[[random.uniform(0, 1) for j in range(nH)] for k in range(c)]
				W2.append(w2)

				w01=random.uniform(0, 1)
				W01.append(w01)
				w02=random.uniform(0, 1)
				W02.append(w02)
				
			netj,y,netk,z = forward_propagation(d,nH,c,X[t],W1[t],W2[t])
			
			delta_wji,delta_wkj = backward_propagation(d,nH,c,x,netj,y,netk,z,T[t],W1[t],W2[t],lr)
			
			W1[t],W2[t] = update_weights(d,nH,c,W1[t],W2[t],delta_wji,delta_wkj)
			
			total+=loss(c,T[t],z)
			mc+=is_misclassified(c,T[t],z)
		print it, total, mc
		if(abs(total)<theta):
			print "Great results!"
			print "W1s"	
			for t in xrange(len(W1)):
				print "W1[",t,"]"
				print W1[t]
			
			print "W2s"	
			for t in xrange(len(W2)):
				print "W2[",t,"]"
				print W2[t]
			
			break

def is_misclassified(c,t,z):
	mxt=0
	mxz=0
	for k in xrange(c):
		if(z[mxz]<z[k]):	
			mxz=k
		if(t[mxt]<t[k]):	
			mxt=k
	if(mxt!=mxz):
		return 1
	else:
		return 0
	

def loss(c,t,z):
	t_loss=0
	for k in xrange(c):
        	t_loss += (0.5)*(t[k]-z[k])*(t[k]-z[k])

        return t_loss

if __name__ == "__main__":

    digits = parse_input.parse('train')
    X =[]
    T =[]
    ct =0
    mx = 20
    theta = 0.1
    for x in digits['0']:
        if ct == mx:
            break
        ct+=1
        X.append(x)
     	T.append([1,0])

    ct=0
    for x in digits['1']:
        if ct == mx:
            break
        ct+=1
     	X.append(x)
     	T.append([0,1])
    ct=0
    for x in digits['5']:
        if ct == mx:
            break
        ct+=1
     	X.append(x)
     	T.append([0,1])


    dim_input = 65
    dim_hidden = 8
    dim_output = 3

    learning_rate = 0.1
    neural_net(X, dim_input,dim_hidden,dim_output, T, learning_rate,theta)


