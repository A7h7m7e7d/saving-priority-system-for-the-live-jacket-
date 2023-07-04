fx = 333
fy = 120
fs = "live"  # takes "live"
fc = "under"  # "under"

sx = 160
sy = 203
ss = ""
sc = "under"

tx = 60
ty = 160
ts = "live"
tc = "under"

import turtle
import math

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Turtle Sea")
screen.setup(width=800, height=600)

# Set the background color to represent the sea
screen.bgcolor("deep sky blue")

# Create a turtle instance
t = turtle.Turtle()

# Now you can draw other elements on top of the sea background
# For example, you can draw waves or other sea-related objects using turtle commands.

# Keep the turtle window open until it is manually closed

pen4 = turtle.Turtle()
pen1 = turtle.Turtle()
pen2 = turtle.Turtle()
pen2.color("green")
pen1.color("yellow")
pen3 = turtle.Turtle()
pen3.color("purple")
pen3.width(5)
pen1.width(5)
pen2.width(5)
pen1.speed(0)
pen1.penup()
pen1.goto(fx, fy)  # Updated to go to the specific coordinates (0, 0)
pen1.pendown()
pen2.speed(0)
pen2.penup()
pen2.goto(sx, sy)  # Updated to go to the specific coordinates (160, 203)
pen2.pendown()
pen1.begin_fill()
pen1.circle(15)
pen1.end_fill()
pen2.begin_fill()
pen2.circle(15)
pen4.penup()
pen4.goto(tx, ty)  # Updated to go to the specific coordinates (160, 203)
pen4.pendown()
pen2.end_fill()
pen4.begin_fill()
pen4.circle(15)
pen4.end_fill()
print(pen3.xcor())

# the nearest function
def nearest(fx, fy, sx, sy, tx, ty):
    d1 = math.sqrt(fx ** 2 + fy ** 2)
    d2 = math.sqrt(sx ** 2 + sy ** 2)
    d3 = math.sqrt(tx ** 2 + ty ** 2)
    a = [d1, d2, d3]
    a_name = {d1: "fn", d2: "sn", d3: "tn"}
    a_sorted = sorted(a)
    return a_name[a_sorted[0]], a_name[a_sorted[1]], a_name[a_sorted[2]]


# a live or not
def alive(fs, ss, ts):
    if fs == "live" and ss == "live" and ts == "live":
        return "b"
    elif fs == "live" and ss == "live" and ts != "live":
        nearest_vals = list(nearest(fx, fy, sx, sy, tx, ty))
        if "tn" in nearest_vals:
            nearest_vals.remove("tn")
        return nearest_vals[0], nearest_vals[1], "tn"
    elif fs == "live" and ss != "live" and ts == "live":
        nearest_vals = list(nearest(fx, fy, sx, sy, tx, ty))
        if "sn" in nearest_vals:
            nearest_vals.remove("sn")
        return nearest_vals[0], nearest_vals[1], "sn"
    elif fs != "live" and ss == "live" and ts == "live":
        nearest_vals = list(nearest(fx, fy, sx, sy, tx, ty))
        if "fn" in nearest_vals:
            nearest_vals.remove("fn")
        return nearest_vals[0], nearest_vals[1], "fn"
    elif fs == "live" and ss != "live" and ts != "live":
        nearest_vals = list(nearest(fx, fy, sx, sy, tx, ty))
        if "fn" in nearest_vals:
            nearest_vals.remove("fn")
        return "fn", nearest_vals[0], nearest_vals[1]
    elif fs != "live" and ss == "live" and ts != "live":
        nearest_vals = list(nearest(fx, fy, sx, sy, tx, ty))
        if "sn" in nearest_vals:
            nearest_vals.remove("sn")
        return "sn", nearest_vals[0], nearest_vals[1]
    elif fs != "live" and ss != "live" and ts == "live":
        nearest_vals = list(nearest(fx, fy, sx, sy, tx, ty))
        if "tn" in nearest_vals:
            nearest_vals.remove("tn")
        return "tn", nearest_vals[0], nearest_vals[1]
    elif fs != "live" and ss != "live" and ts != "live":
        return "b"


# under or beneath the water
def conditions(fc, sc, tc):
    if fc == "under" and sc == "under" and tc == "under":
        return "b"
    elif fc == "under" and sc == "under" and tc != "under":
        return "tn"
    elif fc == "under" and sc != "under" and tc == "under":
        return "sn"
    elif fc != "under" and sc == "under" and tc == "under":
        return "fn"
    elif fc == "under" and sc != "under" and tc != "under":
        return "sn", "tn"
    elif fc != "under" and sc == "under" and tc != "under":
        return "fn", "tn"
    elif fc != "under" and sc != "under" and tc == "under":
        return "fn", "fn"
    elif fc != "under" and sc != "under" and tc != "under":
        return "b"


n = [nearest(fx, fy, sx, sy, tx, ty), alive(fs, ss, ts), conditions(fc, sc, tc)]

if n[1] == "b" and n[2] == "b":
    for v in n[0]:
        if v == "fn":
            pen3.goto(fx, fy)
        elif v == "sn":
            pen3.goto(sx, sy)
        elif v == "tn":
            pen3.goto(tx, ty)
elif n[2] == "b":
    print(n[1])
    for gt in n[1]:
        if gt == "fn":
            pen3.goto(fx, fy)
        elif gt == "sn":
            pen3.goto(sx, sy)
        elif gt == "tn":
            pen3.goto(tx, ty)
