---
layout: post
title: "R on Jupyter"
date: "2016-10-04 21:01:36 -0700"
categories: Data
tags: ['pbdZMQ' had non-zero exit status, R, Jupyter, Notebook, IPython, Data, Analytics]
---

Trying to setup an environment with an R kernel via conda for use with a Jupyter Notebook I ran into a problem that all but stopped me from progressing. Normally a few permutations of a decent google-ing would suffice but not tonight. Merging a few new technology I was very interested in with one a love dearly, I knew I was just over my head but my fascination with the problem combined with an incredible lack of patience to sit through a drawn out forum conversation or GitHub request - _of which there were already multiple making no progress._  

If you are half as excited as I am about using these technologies together, then I best get straight to the fix:

[Click Here][Current Source File] to download the source file.
Even better - rather than relying on me to constantly update this link _and I **wont**_ is to go to the [CRAN Package Site][pbdZMQ CRAN site] and download the most current binary from there.

For me this looked like:
```r
> install.packages('~/Downloads/pbdZMQ_0.2-4.tar', repos = NULL, type="source")
```

**NOTE:**
```bash
USER$ R CMD INSTALL path_to_file
# and
~/path_to_file USER$ R CMD INSTALL file_name
```

Using R from the Terminal as shown above should also work - _however_ - between the time I already invested in failing to find a suitable solution, creating this one, writing up this quick draft, and the greater anticipation of playing around with R in a Jupyter notebook where I could simultaneously web scape with Python while generating easy to follow and reproduce journal entries for this same [site](https://Jerad.xyz) _It was time to move on._

Some more interesting notes that I could look into if I didn't have more exciting repos of data awaiting my exploration, would be that `pbdZMQ` is designed to provide high level wrappers for the `ZeroMQ` library but the [Cran site][pbdZMQ CRAN site] explicitly states:
>For convenience, a minimal 'ZeroMQ' library (4.1.0 rc1) is shipped with 'pbdZMQ', which can be used if no system installation of 'ZeroMQ' is available.  

So it could also be that linking `ZeroMQ` as a package dependency could fix all this. The package is only in Version: 0.2-4 at the writing of this piece. And as mentioned, there are plenty of GitHub bug reports, unanswered Stack Overflow queries - which I will be right on tomorrow morning as it's already well into the morning and I've got an interview with a alluring data company in the IoT business in a few hours that I best rest up for.

---

[Interesting academic paper on the pbdZMQ library](https://cran.r-project.org/web/packages/pbdZMQ/vignettes/pbdZMQ-guide.pdf) that inspired a few iterations in my solution.

[irkernel GitHub Install Page](https://irkernel.github.io/installation/#binary-panel)

[Article From Continnuum](https://www.continuum.io/blog/developer/jupyter-and-conda-r)

[Current Source File]: <https://cran.r-project.org/bin/macosx/mavericks/contrib/3.3/pbdZMQ_0.2-4.tgz> "Current pbdZMQ package source file"  

[pbdZMQ CRAN site]: <https://cran.r-project.org/web/packages/pbdZMQ/index.html> "CRAN site for the pbdZMQ package"
