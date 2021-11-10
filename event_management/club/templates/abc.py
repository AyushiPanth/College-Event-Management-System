2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
# include<iostream.h>
# include<graphics.h>
# include<math.h>
# include<dos.h>

void
main()
{
    int
i, gd = DETECT, gm;
int
x1, y1, x2, y2, xmin, xmax, ymin, ymax, xx1, xx2, yy1, yy2, dx, dy;
float
t1, t2, p[4], q[4], temp;
x1 = 120;
y1 = 120;
x2 = 300;
y2 = 300;
xmin = 100;
ymin = 100;
xmax = 250;
ymax = 250;
initgraph( & gd, & gm, "c:\\turboc3\\bgi");
rectangle(xmin, ymin, xmax, ymax);
dx = x2 - x1;
dy = y2 - y1;
p[0] = -dx;
p[1] = dx;
p[2] = -dy;
p[3] = dy;
q[0] = x1 - xmin;
q[1] = xmax - x1;
q[2] = y1 - ymin;
q[3] = ymax - y1;
for (i=0;i < 4;i++)
{
if (p[i] == 0)
{
    cout << "line is parallel to one of the clipping boundary";
if (q[i] >= 0)
{
if (i < 2)
{
if (y1 < ymin)
{
    y1 = ymin;
}
if (y2 > ymax)
{
y2=ymax;
}
line(x1, y1, x2, y2);
}
if (i > 1)
{
if (x1 < xmin)
{
x1=xmin;
}
if (x2 > xmax)
{
x2=xmax;
}
line(x1, y1, x2, y2);
}
}
}
}
t1=0;
t2=1;
for (i=0;i < 4;i++)
{
temp=q[i] / p[i];
if (p[i] < 0)
{
if (t1 <= temp)
t1=temp;
}
else
{
if (t2 > temp)
t2=temp;
}
}
if (t1 < t2)
{
xx1 = x1 + t1 * p[1];
xx2 = x1 + t2 * p[1];
yy1 = y1 + t1 * p[3];
yy2 = y1 + t2 * p[3];
line(xx1, yy1, xx2, yy2);
}
delay(5000);
closegraph();
}