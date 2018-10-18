# Info
```
#
# Copyright (c) 2009-2018  Steve J.South [NamJungGu] <nowage@gmail.com>
#
#                    Power by http://finfra.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# Description : Pseudodata Datafile Generator
```

# What is dataGenerator
* Pseudodata Datafile Generator by json file is data definiton.
* no need nuympy, no need pandas.

# Usage :
```
  $ python dataGenerator.py {rowCountToGenerate} {rowFormantFilePath} > {destinationFilePath}
```

# Excution Examples
```
$ cat rowFormat.md
$ vi rowFormat.json        # no need to chanage for test
$ python dataGenerator.py
Date,X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,Y
18-01-01 00:00:00,9.9,0.07,8.09,9.15,9.22,9.44,3.46,3.92,8.66,3.94,9.09,19.06
18-01-02 00:00:00,8.83,4.52,2.55,9.77,9.64,5.67,7.27,1.95,8.98,2.14,4.95,18.3
18-01-03 00:00:00,1.45,5.65,3.29,4.0,3.24,0.64,0.36,6.5,7.6,8.11,7.06,14.16
18-01-04 00:00:00,8.99,8.0,5.85,9.23,7.15,0.19,2.84,9.57,4.3,1.35,4.67,21.66
18-01-05 00:00:00,2.49,4.65,1.57,8.27,1.49,5.43,4.61,9.18,3.75,3.08,3.5,10.64
18-01-06 00:00:00,4.85,0.74,6.32,7.33,3.87,0.29,2.71,1.62,2.19,7.37,3.05,8.64
18-01-07 00:00:00,7.52,1.95,7.94,7.21,1.32,2.95,7.03,2.34,5.44,4.17,6.16,15.63
18-01-08 00:00:00,1.21,1.01,2.06,3.59,1.53,7.83,5.6,0.73,9.28,3.39,7.78,10.0
18-01-09 00:00:00,3.84,3.3,4.14,0.81,0.19,2.71,4.54,4.94,6.1,7.29,5.43,12.57
18-01-10 00:00:00,9.15,0.8,4.88,9.55,4.32,4.0,1.43,3.67,9.7,1.97,5.65,15.6

$ python dataGenerator.py 2
Date,X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,Y
18-01-01 00:00:00,8.77,7.83,8.42,7.58,7.1,0.53,1.23,5.46,2.05,3.21,0.62,17.22
18-01-02 00:00:00,4.35,7.2,4.41,7.58,0.56,0.95,6.91,9.7,1.71,0.41,7.08,18.63

$ python dataGenerator.py 1000 > ../data.csv
$ head ../data.csv
Date,X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,Y
18-01-01 00:00:00,3.69,6.09,7.32,3.93,2.64,9.72,2.85,2.44,2.05,4.68,1.45,11.2299
18-01-02 00:00:00,6.35,6.17,6.84,5.08,8.16,8.24,0.84,1.12,3.88,0.26,5.59,18.11
18-01-03 00:00:00,8.06,8.04,0.67,3.59,5.34,0.98,7.98,5.26,6.22,5.32,7.37,23.47
18-01-04 00:00:00,6.79,6.73,6.83,9.56,4.37,3.22,8.67,5.66,4.03,2.06,6.72,20.2399
18-01-05 00:00:00,2.4,0.72,3.93,7.24,9.74,5.27,4.52,8.66,2.41,7.1,9.63,12.75
18-01-06 00:00:00,4.69,3.69,5.35,0.71,1.58,0.22,2.68,5.67,0.8,7.8,0.7,9.08
18-01-07 00:00:00,7.79,9.34,5.87,5.45,6.13,7.63,5.28,9.26,6.23,0.19,0.77,17.9
18-01-08 00:00:00,3.35,8.04,2.84,8.81,7.82,9.65,8.09,5.5,4.98,4.73,3.49,14.88
18-01-09 00:00:00,9.46,9.21,6.96,2.23,0.68,1.14,3.62,6.31,5.66,6.65,3.2,21.87
```

# Requirement
1. python3.5 or over.


# toDo
1. Add Comment on the Code.
