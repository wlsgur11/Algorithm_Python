# [3258] Three Robots
### 채점 결과
Accepted
### 제출 일자
2026년 04월 10일 05:46:40
### 성능 요약[추후 구현 예정]
- 메모리: N/A KB
- 시간: N/A ms
---
### 문제 링크
https://code.pusan.ac.kr/problem/3258
### 난이도
어려움
### 문제 설명
An undirected weighted graph 𝐺 is given and 𝐺 is connected, that is, arbitrary two vertices in 𝐺 must be connected by a path. Three robots are exploring 𝐺 through edges. Here the weight of each edge means the time to be spent when a robot passes through it. The speeds of all the robots are identical and at least two robots may be passed through a same edge at a time. At some instant of the explorations of the robots, all of them should get together at a vertex to share their information. It is called a rendezvous.Initially, three robots lie on specified vertices. Of course, at least two robots may be located on an identical vertex. Also all the three robots start to move simultaneously. We wish to know the minimum time needed to fulfill the first rendezvous.For example, initially, three robots are located on the vertices 1, 5, and 7 in Figure L.1. A movement of the robot on the vertex 1 into the vertex 9 requires at least 9 time units. Also it takes at least 8 and 3 time units, respectively that the robots on the vertices 5 and 7 travel into the vertex 9. So the rendezvous at the vertex 9 requires at least 9 time units and it is the minimum time needed for the first rendezvous. Of course, the first rendezvous happens either at the vertex 1 or 4 and it also requires the minimum time of 9.Given a weighted and connected graph 𝐺 and the initial locations of three robots, write a program to find the minimum time needed to fulfill the first rendezvous.
### 입력
Your program is to read from standard input. The input starts with a line containing two integers, 𝑁 and 𝑀(1 ≤ 𝑁 ≤ 20,000, 𝑁 − 1 ≤ 𝑀 ≤ 100,000), where 𝑁 and 𝑀 are the numbers of vertices and edges of 𝐺, respectively. The vertices of 𝐺 are represented by 1, 2, … , 𝑁. In each of the following 𝑀 lines, three integers 𝑎, 𝑏, and 𝑡 (1 ≤ 𝑎 ≠ 𝑏 ≤ 𝑁, 1 ≤ 𝑡 ≤ 10,000) are given, where an edge connects the two vertices 𝑎 and 𝑏, and its weight is 𝑡. The last (𝑀 + 2)-th line contains three integers 𝑢, 𝑣, and 𝑤, which are the initial locations ofthree robots (1 ≤ 𝑢, 𝑣, 𝑤 ≤ 𝑁). Of course, it is possible that at least two of the three robots are initially located on an identical vertex.
### 출력
Your program is to write to standard output. Print exactly one line which contains the minimum time needed to fulfill the first rendezvous.
### 예제 입력/출력
**예제 입력 1**
```
4 6
1 2 8
3 2 6
3 1 1
1 4 10
4 2 2
3 4 3
1 1 2
```
**예제 출력 1**
```
4
```
**예제 입력 2**
```
9 13
1 2 5
3 1 6
1 4 1
2 5 4
3 4 3
5 4 9
6 3 2
4 7 5
8 5 6
7 8 9
5 9 8
7 6 1
7 9 3
1 5 7
```
**예제 출력 2**
```
9
```
### 제약 사항
- 시간 제한   1000ms
- 메모리 제한   256mb