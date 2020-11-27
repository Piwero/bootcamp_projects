
'''
Find Cost of Tile to Cover W x H Floor - 
Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.
'''

def find(tile_cost, width, height):
	area_floor = width * height
	return tile_cost*area_floor

print(find(10,2,2))


