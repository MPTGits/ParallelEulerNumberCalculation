# ParallelEulerNumberCalculation

<h2>Usage</h2>
 
<a href="https://www.codecogs.com/eqnedit.php?latex=e&space;=&space;\sum&space;\frac{2*k&plus;1}{(2*k)!}&space;,k&space;=&space;0...inf" target="_blank"><img src="https://latex.codecogs.com/gif.latex?e&space;=&space;\sum&space;\frac{2*k&plus;1}{(2*k)!}&space;,k&space;=&space;0...inf" title="e = \sum \frac{2*k+1}{(2*k)!} ,k = 0...inf" /></a>
<ul>
<li>-q  - If passed program doesn’t print to the STDOUT(not fully implemented).</li>
<li>-p {integer} - Number of members of the sequence to be summed up.(default = 10 000)</li>
<li>-t {integer} - Number of processes to be used.(default = 1)</li>
<li>-o {name of file} - File in which the output will be saved(default = 'eulerNumCalculation_{timestamp}.txt')</li>
</ul>
<p>NOTE: Current precision of the output number is set to 100 000 this should cover partial sums up to around 7000 members. Will add <precision> parameter to command line call in future.</p>

<h2>Some test results</h2>
<p>NOTE: The precision in the graphs is the number of acurate digits in the euler number(it is not the number of member of the partial sum)</p>
<b>Code was run on the following machine:</b>
<ul>
<li>Model: Intel Xeon CPU E5-2660 2.20 GHz </li>
<li>Architecture: 64 bit </li>
<li>CPU(s): 32 </li>
<li>Number of processors: 2 physical </li>
<li>RAM: 64GB </li>
</ul>
 
<img src="https://i.ibb.co/xLM9Y9y/1.png"/>
<img src="https://i.ibb.co/hx5Mkpd/2.png"/>
