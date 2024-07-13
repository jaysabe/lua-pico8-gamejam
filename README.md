## PCC Makerspace OMIC Training Camp - STEAM for 9th Graders
Welcome to the Portland Community College Makerspace OMIC Training Camp! This two-day camp was designed to introduce 9th-grade students to the exciting world of STEAM (Science, Technology, Engineering, Arts, and Mathematics) through hands-on projects and interactive learning.

## Camp Overview
### Day 1: Game Development with pico8
On the first day, students learned the basics of game development using pico8, a fantasy console for making, sharing, and playing tiny games and other computer programs. They coded their own adventure game, gaining valuable programming skills and understanding game design principles.

### Day 2: Embedded Programming with Microbits
The second day focused on embedded programming with microbits, small programmable devices used for teaching coding and electronics. Students worked on an interactive project called "Rain Game," which introduced them to the basics of hardware programming.

### Equipment and Activities
The camp took place at the OMIC Fab Lab, equipped with a variety of tools and machines, including:
- Prusa 3D printers
- Shopbot and Carbide CNC routers
- Universal laser cutters
- Soldering irons
- Heat press
- Cricut cutters
- Printmaking press
- And more!

Students had the opportunity to see these tools in action and understand their applications in real-world STEAM projects.

## Program: adventure(8).p8
Description: This program is a simple adventure game where players navigate through various challenges. Students learned to create sprites, design levels, and implement game logic.

```lua

-- Adventure Game for pico8
-- Created by: Jay Abegglen
-- Date: June 15th, 2024

function _init()
	stars = {}
	
	for i=1,50 do
		s = {x=rnd(127),
							y=rnd(127),
							r=rnd(2),
							v=rnd()+0.1,
							c=flr(rnd(20))}
		add(stars,s)
	end
	
	-- character init
	cx = 80
	cy = 80
	
	area_size = 40
	half_area = area_size / 2
	
	dragon_x = cx
	dragon_y = cy
	
	-- timer 
	move_delay = 7
	b_timer = move_delay
end


function update_dragon()
	b_timer -= 1
	
	if b_timer <= 0 then
	
		-- get a random num between 0 and 3
		local direction = flr(rnd(4))
	
		if direction == 0 and dragon_y > cy - half_area then
			--move up
			dragon_y -= 1
		elseif direction == 1 and dragon_y < cy + half_area then
			-- move down
			dragon_y += 1
		elseif direction == 2 and dragon_x > cx - half_area then
			-- move left 
			dragon_x -= 1
		elseif direction == 3 and dragon_x < dragon_x + half_area then
			dragon_x += 1
			end
			
			b_timer = move_delay
	end
end

function _update()
	
	oldx = cx
	oldy = cy
		
	for s in all(stars) do
		s.y += s.v
		
		s.c += 1
		
		if s.c % 30 == 0 then 
			s.r = (s.r+1)%2
		end
		
		if s.y > 127 then
			del(stars,s)
			news = {x=rnd(127),
											y=-10+rnd(5),
											r=rnd(2),
											v=rnd()+0.1,
											c=flr(rnd(20))}
			add(stars, news)
		end
	end
		
		update_dragon()
		
	if (btn(⬅️)) cx = cx - 1
	if (btn(➡️)) cx = cx + 1
	if (btn(⬆️)) cy = cy - 1
	if (btn(⬇️)) cy = cy + 1
	
	if mapcollide(x,y) then
		cx = oldx
		cy = oldy
	end
end

function _draw()
cls()
map()

	for s in all(stars) do
		circ(s.x,s.y,s.r,7)
	end

-- spawn monster and hero
spr(2,cx+3,cy)
spr(1,cx,cy)
spr(3,dragon_x,dragon_y)
end
-->8
function mapcollide(x,y)

	x1 = cx \ 8
	y1 = cy \ 8
	x2 = (cx+7) \ 8
	y2 = (cy+7) \ 8
	
	a = fget(mget(x1,y1),0)
	b = fget(mget(x2,y1),0)
	c = fget(mget(x1,y2),0)
	d = fget(mget(x2,y2),0)
	
	return (a or b or c or d)
	
end


function spritecollide(xp,yp,xe,ye)
	a = xp + 7 < xe
	b = xp > xe+7
	c = yp + 7 < ye
	d = yp > ye + 7
	
	return not (a or b or c or d)
	
end
```

## Program: raingame.hex
Description: This program is a rain simulation game where the microbit detects "rain drops" and responds with appropriate actions. Students learned to write code that interacts with the microbit’s sensors and display.
*Note: was exported from Microbit Editor into [hex code](https://python.microbit.org/v/3).*
```python
# Rain Game for microbit
# Date: June 27th, 2024

from microbit import *
import random as r
import radio
import music
radio.config(group=42)
import sys as s

radio.on()
player = 2
rainx = r.randint(0,4)
rainy = -1
score = 0
inc_sec = 0
var = 0

# Code in a 'while True:' loop repeats forever
while True:
    inc_sec += 1
    inc_sec /= 10
    if button_a.was_pressed() and player > 0:
        display.set_pixel(player,4,0)
        player -= 1
    if button_b.was_pressed() and player < 4:
        display.set_pixel(player,4,0)
        player += 1
    display.set_pixel(player,4,9)

    # rain movement
    rainy += 1 
    if rainy < 5:
        display.set_pixel(rainx,rainy,9)
    if rainy > 0 and rainy < 6:
        display.set_pixel(rainx,rainy-1,0)
    if rainy == 4 and rainx == player:
        score += 1
    if rainy > 4:
        rainx = r.randint(0,4)
        rainy = -1

    if score > 4:
        # music.play(music.FUNERAL)
        display.scroll("You survived " + str(inc_sec))
        s.exit()
    sleep(100)
    
    
    
    if button_a.was_pressed() and button_b.was_pressed():
        radio.send('rain game fr')
        display.show('message sent.')
    
    rec_mess = radio.receive()
    if rec_mess:
        display.scroll(rec_mess)
    # Same:
        # cout << "This person is " << age << "years old." endl;
        # print(f"This person is {21} years old.")
```
Feel free to explore these programs and modify them to create your own unique projects!
