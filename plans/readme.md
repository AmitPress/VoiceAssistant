# Objective: 
The primary goal is to design a voice assistance which can mimic the mainstream assistant in a limited way. No doubt there will be less features and testing with respect to the mainstream once. But we have to ensure that the voice assistant does not break in its limited area of expertise.

Means to achieve the goal:
- a tool that can read english texts
    - solution: gtts
- a tool that can record voice and encrypt that to a audio file
    - solution: gtts
- a tool that can play a audio file
    - solution: playsound
- we will need some driver program/libraries as well
    - solution:
- system apis and standard libraries
    - solution: os, random, time, webbrowser
### Note that:
- We have to make sure that User Class and Voice Assistant is a singletone class

### Warnings:
- It requires network connection.
- anomalies:
    - `Search google in youtube`