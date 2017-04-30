
# Fixing Majic

My python everything recently collapsed. And for the better, it was a horribly stitched together scoffold that represented the just in time or fall back required use cases I employed the langauge for - whenever trusty R and my comfortable RStudio wasn't up for the task - _rarely_ - or when I was looking to expand my experience into a different environment and try to figure out what everyone is barking about on the other side of the fense.

Now the time has come for me to walk that fense more regularly. While I love R and could play around in RStudio all day, I am quite aware that when working with other teams, or in the world outside of my machine, that python plays better with others.

Following the 99% I downloaded Anaconda - _after deleting a previous build I had forgotten about from a past project_ - only to find my path all fudged up from some recent computer vision work that required bindings all over the place from 3.5 to 2.7 to OpenCV 2 then 3 then 2 again... _I was really missing RStudio right about then_

Regardless, after a few nukes and lots of time at the command line I was making progress. I loaded up a notebook to play around and start changing over past projects. Starting with python 2.7 everything seemed happy. I put my machine to bed after a long night only to be struck with anxiety moments after waking up and jumping on.

`ImportError: bad magic number in 'numpy': b'\x03\xf3\r\n'` <-- what's this magic stuff!?! I thought python was supposed to be straight forward with no tricks and now theres rabits jumping out of hats?

Again I took to the CL but with no luck this time I hit the boards. There where plenty of similar cases but all of them were package specific - most of which not Numpy - and none of them seeemed to apply to me.
After finally taking someone's issue with the `math` package far enough I believe I have worked my way out of this mess and wanted to record doing so here for others to find someday, or as a constant reminder of my previous loveR.

## Import Numpy  
.. or try at least

First allow me to show you my problem:


```python
import numpy
```


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-1-5a0bd626bb1d> in <module>()
    ----> 1 import numpy
    

    ImportError: bad magic number in 'numpy': b'\x03\xf3\r\n'


**Bad Magic!**
Note the number `'\x03\xf3\r\n'` points to a python 2 package.  
_Finding that out was the big breakthrough I needed_  

Allow me to show you.


```python
import sys
```


```python
sys.version
```




    '3.5.2 |Anaconda custom (x86_64)| (default, Jul  2 2016, 17:52:12) \n[GCC 4.2.1 Compatible Apple LLVM 4.2 (clang-425.0.28)]'



...hmm we are in a Python 3 kernel supported notebook and using the kernel drop down to switch leaves me with a dead kernel.

Let's do this:
_Note: using the `!` symbol before a command tells the notebook to execute it in the terminal. This is great for accessing `conda install`, `pip install` etc..._

Using the bang to access a terminal within the notebook allows us to access, download then activate a python2 kernel for us to use in our current notebook:


```python
!conda create -n ipykernel_py2 python=2 ipykernel
```

    
    
    CondaValueError: Value error: prefix already exists: /Users/irJERAD/anaconda/envs/ipykernel_py2
    
    



```python
!source activate ipykernel_py2
```

Place this in our current path:


```python
!python -m ipykernel install --user
```

    Installed kernelspec python2 in /Users/irJERAD/Library/Jupyter/kernels/python2


Now we can select python 2 in the kernel drop down above.  
For my resources check out the conda docs on [python 2 inside py3 notebook](http://ipython.readthedocs.io/en/stable/install/kernel_install.html)  

Now lets see where that takes us:


```python
import sys
```


```python
sys.version
```




    '3.5.2 |Anaconda custom (x86_64)| (default, Jul  2 2016, 17:52:12) \n[GCC 4.2.1 Compatible Apple LLVM 4.2 (clang-425.0.28)]'



Amazing!  
Now back to that numpy package and it's _magic_ location

Now that we are here in python 2, let's see if we can find that magic number...


```python
import imp
```


```python
imp.get_magic()
```




    b'\x16\r\r\n'



Look at that `\x03\xf3\r\n` a perfect match

... but if that were so, then `numpy` would work fine now that we are in python 2


```python
import numpy
```


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-11-5a0bd626bb1d> in <module>()
    ----> 1 import numpy
    

    ImportError: bad magic number in 'numpy': b'\x03\xf3\r\n'



```python
numpy.__version__
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-12-6886416a6112> in <module>()
    ----> 1 numpy.__version__
    

    NameError: name 'numpy' is not defined


Alright, now we are getting expected results.  
Time for a solution!  
Let's see where this trouble causing numpy resides:  


```python
numpy.__path__
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-13-4cdc7ab03370> in <module>()
    ----> 1 numpy.__path__
    

    NameError: name 'numpy' is not defined


Ok now I am double sure I have found the culprit; it's time to lay down some justice and _finally_ get to work on data analytics, exploratory science and story telling with actionable insights like we should have been this entire time.

Change back to the python 3 kernel using the method from  the menu above   
[kernel | dropdown] --> [Change Kernel] --> select Python 3


```python
import sys
```


```python
sys.version
```




    '3.5.2 |Anaconda custom (x86_64)| (default, Jul  2 2016, 17:52:12) \n[GCC 4.2.1 Compatible Apple LLVM 4.2 (clang-425.0.28)]'



And were back to where we started!  
Only now we have much more context to work with.


```python
import sys
```

double check where we are. _so many circles can leave you dizzy_


```python
sys.version
```




    '3.5.2 |Anaconda custom (x86_64)| (default, Jul  2 2016, 17:52:12) \n[GCC 4.2.1 Compatible Apple LLVM 4.2 (clang-425.0.28)]'



**Perfect!**  
Now to find out where the pesky package is hiding


```python
import importlib
```


```python
importlib.util.find_spec('numpy')
```




    ModuleSpec(name='numpy', loader=<_frozen_importlib_external.SourcelessFileLoader object at 0x105415b38>, origin='/usr/local/lib/python2.7/site-packages/numpy/__init__.pyc', submodule_search_locations=['/usr/local/lib/python2.7/site-packages/numpy'])



Looks like we found our red herring or some other more appropriate metaphor...  
I'll make it more clear where by showing all the paths being used by our python 3.5 build:


```python
import sys
```


```python
sys.path
```




    ['',
     '/Users/irJERAD/anaconda/lib/python35.zip',
     '/Users/irJERAD/anaconda/lib/python3.5',
     '/Users/irJERAD/anaconda/lib/python3.5/plat-darwin',
     '/Users/irJERAD/anaconda/lib/python3.5/lib-dynload',
     '/Users/irJERAD/.local/lib/python3.5/site-packages',
     '/usr/local/lib/python2.7/site-packages',
     '/Users/irJERAD/anaconda/lib/python3.5/site-packages',
     '/Users/irJERAD/anaconda/lib/python3.5/site-packages/Sphinx-1.5.1-py3.5.egg',
     '/Users/irJERAD/anaconda/lib/python3.5/site-packages/aeosa',
     '/Users/irJERAD/anaconda/lib/python3.5/site-packages/setuptools-27.2.0-py3.5.egg',
     '/Users/irJERAD/anaconda/lib/python3.5/site-packages/IPython/extensions',
     '/Users/irJERAD/.ipython']



**Hey!** There shouldn't be a python 2.7 site packages path in our system paths for python 3.5.  
Let's rectify that.

Credit goes to [this answer](http://stackoverflow.com/questions/26471889/permanently-remove-something-from-python-sys-path) for finding a different problem with the same fix:


```python
sys.path.remove('/usr/local/lib/python2.7/site-packages')
```

**And for the grand finale!!!**


```python
import numpy
```


```python
numpy.__version__
```




    '1.11.3'



Looking good!  
_but just to be safe_


```python
sys.path
```




    ['',
     '/Users/irJERAD/anaconda/lib/python35.zip',
     '/Users/irJERAD/anaconda/lib/python3.5',
     '/Users/irJERAD/anaconda/lib/python3.5/plat-darwin',
     '/Users/irJERAD/anaconda/lib/python3.5/lib-dynload',
     '/Users/irJERAD/.local/lib/python3.5/site-packages',
     '/Users/irJERAD/anaconda/lib/python3.5/site-packages',
     '/Users/irJERAD/anaconda/lib/python3.5/site-packages/Sphinx-1.5.1-py3.5.egg',
     '/Users/irJERAD/anaconda/lib/python3.5/site-packages/aeosa',
     '/Users/irJERAD/anaconda/lib/python3.5/site-packages/setuptools-27.2.0-py3.5.egg',
     '/Users/irJERAD/anaconda/lib/python3.5/site-packages/IPython/extensions',
     '/Users/irJERAD/.ipython']



Hurrah!  
And that is how you fix the magic that should not be. Because everything has some propabalistic measure and if you just keep sampling enough then by the law of large numbers your recorded average will approximate the actual average.  
So keep sampling out there and I'll see you on average - _with a bunch of normal assumptions of course..._

### Sources  
[Python 2 kernel inside a Python 3 notebook](http://ipython.readthedocs.io/en/stable/install/kernel_install.html)  

[Finding the source of the magic number](http://stackoverflow.com/questions/25776782/i-cannot-get-import-random-to-work-python-3)  

[Remove a bad system path](http://stackoverflow.com/questions/26471889/permanently-remove-something-from-python-sys-path)  
