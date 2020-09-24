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

# Project structure
The project is divided into different blocks: 

- In the file [Brownian_motion](https://github.com/silviavargas/Brownian_motion_simulation/blob/master/Brownian_motion.py) the brownian_motion function was built using the *Numpy package*. By providing the number of discrete time steps ***N***, the number of continuous-time steps ***T***, we simply generate N increments ***dX*** from the normal distribution with some variance ***h*** and distribute them across the continuous-time steps T. Then, the Brownian motion ***X(t)*** is a cumulative sum of the increments, so the *cumsum* function is used and at last the initial condition are inserted with the method *insert*.

- In the file [main_Brownian_motion](https://github.com/silviavargas/Brownian_motion_simulation/blob/master/main_Brownian_motion.py) there is the main part of the code: we initialize the brownian function ***brownian_motion*** parameters N,T,h and the normalizing constant dt=T/N. Then we generate two brownian motion arrays ***X*** and ***Y***, since the same function  can be used to generate Brownian motion in two dimensions where each dimension is just a one-dimensional Brownian motion. It is generated also the time array ***t*** with the numpy method *linspace*.

- In the files [plot_1D](https://github.com/silviavargas/Brownian_motion_simulation/blob/master/plot_1D.py) and [plot_2D](https://github.com/silviavargas/Brownian_motion_simulation/blob/master/plot_2D.py) the brownian motion in one dimension and two dimensions respectively is plotted, with the functions of the *Mathoplotlib* package. To see the obtained random motion the user has to launch the plot_1D or the plot_2D file.

- In the file [animation_1D](https://github.com/silviavargas/Brownian_motion_simulation/blob/master/animation_1D.py) using *Matplotlib’s animation API* we generate an animated brownian motion in one dimension. The animation function needs three essential inputs: i) an instance of the figure to show the animation, ii) data initialization function and iii) a function that defines the animation logic. Additionally, we provide the number of frames to draw and the delay in milliseconds between them. The *animate* function plays a central role. Every iteration, we generate from scratch a Brownian Motion with 10 more steps compared to the one in the previous iteration. To see the resulting animation in *gif* format the user has to launch the file animation_1D. 

