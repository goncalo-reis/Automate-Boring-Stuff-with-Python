import sys, pyperclip

text = pyperclip.paste()
bullets = text.split('\n')
for bullet in range(len(bullets)):
    bullets[bullet] = '* ' + bullets[bullet]
final = '\n'.join(bullets)
pyperclip.copy(final)



