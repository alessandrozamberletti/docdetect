# docdetect

[![Build Status](https://travis-ci.org/alessandrozamberletti/docdetect.svg?branch=master)](https://travis-ci.org/alessandrozamberletti/docdetect)
[![Build status](https://ci.appveyor.com/api/projects/status/l1gjc8g7c1q3846j/branch/master?svg=true)](https://ci.appveyor.com/project/alessandrozamberletti/docdetect/branch/master)
[![codecov](https://codecov.io/gh/alessandrozamberletti/docdetect/branch/master/graph/badge.svg)](https://codecov.io/gh/alessandrozamberletti/docdetect)

~~Unofficial implementation of~~ Trying to emulate [Fast and Accurate Document Detection for Scanning](https://blogs.dropbox.com/tech/2016/08/fast-and-accurate-document-detection-for-scanning/) without ML
 
2018/10/20: edge detection wip -> check literature and datasets **done**  
2018/10/23: edge detection wip -> use canny+contours+hough & compare with ml approach **done**  
2018/11/01: too many lines from hough with low thr -> cluster lines with similar rho, ~~theta~~ values **done**  
2018/11/02: detect potential doc edges intersections, drop unusual ones -> **done**  
2018/11/02: detect all closed shapes with 4 'ok' angles -> *wip*  

1. canny  
2. mser  
3. hough  
4. remove duplicates
5. candidates

# resources  
* https://arxiv.org/pdf/1504.06375.pdf
* https://pdollar.github.io/files/papers/DollarPAMI15edges.pdf
