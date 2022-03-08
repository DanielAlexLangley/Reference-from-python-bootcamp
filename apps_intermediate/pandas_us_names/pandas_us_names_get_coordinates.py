
# If we needed to get the coordinate data for each of the states, then we'd use this code:
note = '''
def get_mouse_click_coor(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
'''
# But we don't have to do that since the coordinates were given to us in the csv file.
