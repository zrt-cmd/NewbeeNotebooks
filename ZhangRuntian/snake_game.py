# 贪吃蛇小游戏 - Python Turtle
import turtle
import random
import time

# 游戏基础设置
screen = turtle.Screen()
screen.title("经典贪吃蛇")
screen.bgcolor("#1a1a1a")
screen.setup(width=600, height=600)
screen.tracer(0)  # 关闭自动刷新

# 蛇头
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("#00ff00")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# 食物
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("#ff4444")
food.penup()
food.goto(0, 100)

# 蛇身体
segments = []

# 分数
score = 0
high_score = 0

# 分数显示
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("得分: 0  最高分: 0", align="center", font=("Arial", 20, "bold"))

# 方向控制函数
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# 移动函数
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# 键盘绑定
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# 主游戏循环
def game_loop():
    global score, high_score
    screen.update()

    # 撞墙检测
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        # 隐藏身体
        for seg in segments:
            seg.goto(1000,1000)
        segments.clear()
        score = 0
        pen.clear()
        pen.write(f"得分: {score}  最高分: {high_score}", align="center", font=("Arial", 20, "bold"))

    # 吃到食物
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x,y)
        # 增加身体
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#00cc00")
        new_segment.penup()
        segments.append(new_segment)
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f"得分: {score}  最高分: {high_score}", align="center", font=("Arial", 20, "bold"))

    # 身体跟随
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # 撞自己检测
    for seg in segments:
        if seg.distance(head) < 10:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for seg in segments:
                seg.goto(1000,1000)
            segments.clear()
            score = 0
            pen.clear()
            pen.write(f"得分: {score}  最高分: {high_score}", align="center", font=("Arial", 20, "bold"))

    screen.ontimer(game_loop, 100)

# 启动游戏
game_loop()
screen.mainloop()