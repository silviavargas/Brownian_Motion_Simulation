# Brownian motion model

Brownian motion can be described by a continuous-time stochastic process called the Wiener process.
Let ***X(t)*** be a random variable that depends continuosly on ***t*** in ***[0,T]***. The random variable is characterized by: 
1. ***X(0)=0*** with probability 1
2. For 0 <a href="https://www.codecogs.com/eqnedit.php?latex=\tiny&space;\leq" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\tiny&space;\leq" title="\tiny \leq" /></a> s < t <a href="https://www.codecogs.com/eqnedit.php?latex=\tiny&space;\leq" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\tiny&space;\leq" title="\tiny \leq" /></a> T, the increment:

   <a href="https://www.codecogs.com/eqnedit.php?latex=\small&space;X(t)-X(s)\simeq&space;\sqrt{t-s}&space;\mathcal{N}(\mu,&space;\sigma^2)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\small&space;X(t)-X(s)\simeq&space;\sqrt{t-s}&space;\mathcal{N}(\mu,&space;\sigma^2)" title="\small X(t)-X(s)\simeq \sqrt{t-s} \mathcal{N}(\mu, \sigma^2)" /></a> (1)

   Where <a href="https://www.codecogs.com/eqnedit.php?latex=\small&space;\mathcal{N}(\mu,&space;\sigma^2)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\small&space;\mathcal{N}(\mu,&space;\sigma^2)" title="\small \mathcal{N}(\mu, \sigma^2)" /></a> denotes the normal distribution with mean <a href="https://www.codecogs.com/eqnedit.php?latex=\small&space;\mu" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\small&space;\mu" title="\small \mu" /></a> and variance <a href="https://www.codecogs.com/eqnedit.php?latex=\small&space;\sigma" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\small&space;\sigma" title="\small \sigma" /></a>.

3. ***X(t)*** has indipendent increments, which means that if 0 <a href="https://www.codecogs.com/eqnedit.php?latex=\tiny&space;\leq" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\tiny&space;\leq" title="\tiny \leq" /></a> s < t < u < v <a href="https://www.codecogs.com/eqnedit.php?latex=\tiny&space;\leq" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\tiny&space;\leq" title="\tiny \leq" /></a> T, then X(t)-X(s) and X(v)-X(u) are also independent. 

## Brownian motion in Python

To implement the Brownian motion in Python, suppose we discretize the time interval ***[0,T]*** into ***N-1*** equidistant subintervals or ***N*** points:

   <a href="https://www.codecogs.com/eqnedit.php?latex=\small&space;0<t_1<...<t_{j-1}<t_j<t_{j&plus;1}<...<t_{N-1}<t_N=T" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\small&space;0<t_1<...<t_{j-1}<t_j<t_{j&plus;1}<...<t_{N-1}<t_N=T" title="\small 0<t_1<...<t_{j-1}<t_j<t_{j+1}<...<t_{N-1}<t_N=T" /></a>

The time step <a href="https://www.codecogs.com/eqnedit.php?latex=\small&space;\Delta&space;t=&space;t_{j&plus;1}-t{j}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\small&space;\Delta&space;t=&space;t_{j&plus;1}-t{j}" title="\small \Delta t= t_{j+1}-t{j}" /></a>, is obtained from <a href="https://www.codecogs.com/eqnedit.php?latex=\small&space;\Delta&space;t=\frac{T}{N}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\small&space;\Delta&space;t=\frac{T}{N}" title="\small \Delta t=\frac{T}{N}" /></a>.
The increment can be given by 
   <a href="https://www.codecogs.com/eqnedit.php?latex=\small&space;dX(t_j)=X(t_j)-X(t_{j-1})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\small&space;dX(t_j)=X(t_j)-X(t_{j-1})" title="\small dX(t_j)=X(t_j)-X(t_{j-1})" /></a> (2)   
   <a href="https://www.codecogs.com/eqnedit.php?latex=\small&space;=\sqrt{\Delta&space;t}&space;\mathcal{N}(0,1)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\small&space;=\sqrt{\Delta&space;t}&space;\mathcal{N}(0,1)" title="\small =\sqrt{\Delta t} \mathcal{N}(0,1)" /></a> (3)

for standard normal distribution with <a href="https://www.codecogs.com/eqnedit.php?latex=\small&space;\mu=0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\small&space;\mu=0" title="\small \mu=0" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=\small&space;\sigma^2=1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\small&space;\sigma^2=1" title="\small \sigma^2=1" /></a>.
