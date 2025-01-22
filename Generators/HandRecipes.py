from Common import *
from MachinesList import *
from MiscGen import *
import copy

objects_array = []

recipes_hand = []

recipes_press = []

def append_recipe_hand_press(recipe):
	item_count = 0
	for item in recipe["Input"]["Items"]:
		item_count = item_count + item["Count"]
	
	dec_recipe = copy.deepcopy(recipe)

	recipes_hand.append(recipe)
	
	output = copy.deepcopy(dec_recipe["Input"])
	
	dec_recipe["Ticks"] = 60
	dec_recipe["ResourceInput"] = { "Name": "Kinetic", "Count": 100 }
	recipes_press.append(dec_recipe)	

recipes_hand.append({
	"Name": "ClayBlock",
	"Input":{
		"Items":[
			{
				"Name": "Clay",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "ClayBlock",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"Bricks",
	"Input":{
		"Items":[
			{
				"Name": "StoneSurface",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Bricks",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"RedBricks",
	"Input":{
		"Items":[
			{
				"Name": "RedStoneSurface",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "RedBricks",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"DarkBricks",
	"Input":{
		"Items":[
			{
				"Name": "DarkStoneSurface",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DarkBricks",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "SandSurface",
	"Input":{
		"Items":[
			{
				"Name": "GravelSurface",
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "SandSurface",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "GravelSurface",
	"Input":{
		"Items":[
			{
				"Name": "StoneSurface",
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "GravelSurface",
				"Count": 1
			}
		]
	},
	"Ticks": 20,
})

recipes_hand.append({
	"Name":"StoneTiles",
	"Input":{
		"Items":[
			{
				"Name": "StoneSurface",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "StoneTiles",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"DarkTiles",
	"Input":{
		"Items":[
			{
				"Name": "DarkStoneSurface",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "DarkTiles",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"RedTiles",
	"Input":{
		"Items":[
			{
				"Name": "RedStoneSurface",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "RedTiles",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"TerracottaTiles",
	"Input":{
		"Items":[
			{
				"Name": "Terracotta",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "TerracottaTiles",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"TerracottaBricks",
	"Input":{
		"Items":[
			{
				"Name": "TerracottaTiles",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "TerracottaBricks",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"CircuitBoard",
	"Input":{
		"Items":[
			{
				"Name": "Plank",
				"Count": 1
			},
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "CircuitBoard",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"GoldWire",
	"Input":{
		"Items":[
			{
				"Name": "GoldIngot",
				"Count": 1
			},	
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "GoldWire",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"CopperWire",
	"Input":{
		"Items":[
			{
				"Name": "CopperPlate",
				"Count": 1
			},	
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "CopperWire",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"Circuit",
	"Input":{
		"Items":[
			{
				"Name": "CopperWire",
				"Count": 6
			},	
			{
				"Name": "CircuitBoard",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Circuit",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"AdvancedCircuit",
	"Input":{
		"Items":[
			{
				"Name": "Silicon",
				"Count": 1
			},	
			{
				"Name": "Circuit",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "AdvancedCircuit",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"Processor",
	"Input":{
		"Items":[
			{
				"Name": "SiliconWafer",
				"Count": 1
			},	
			{
				"Name": "AdvancedCircuit",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Processor",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"QuantumCircuit",
	"Input":{
		"Items":[
			{
				"Name": "QuantumCore",
				"Count": 2
			},	
			{
				"Name": "Processor",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "QuantumCircuit",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name":"QuantumProcessor",
	"Input":{
		"Items":[
			{
				"Name": "QuantumCircuit",
				"Count": 2
			},	
			{
				"Name": "Processor",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "QuantumProcessor",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "WoodenChest",
	"Input":{
		"Items":[
			{
				"Name": "Plank",
				"Count": 6
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "WoodenChest",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

append_recipe_hand_press({
	"Name": "WoodenPlanks",
	"Input":{
		"Items":[
			{
				"Name": "Plank",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "WoodenPlanks",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Steampack",
	"Input":{
		"Items":[
			{
				"Name": "CopperParts",
				"Count": 6
			},
			{
				"Name": "CopperPlate",
				"Count": 2
			},
			{
				"Name": "CopperPipe",
				"Count": 4
			},
			{
				"Name": "Circuit",
				"Count": 10
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Steampack",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "AdvancedSteampack",
	"Input":{
		"Items":[
			{
				"Name": "StainlessSteelParts",
				"Count": 30
			},
			{
				"Name": "StainlessSteelPlate",
				"Count": 10
			},
			{
				"Name": "CopperPipe",
				"Count": 30
			},
			{
				"Name": "Processor",
				"Count": 10
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "AdvancedSteampack",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "HighCapacitySteampack",
	"Input":{
		"Items":[
			{
				"Name": "SteelParts",
				"Count": 30
			},
			{
				"Name": "SteelPlate",
				"Count": 10
			},
			{
				"Name": "CopperPipe",
				"Count": 5
			},
			{
				"Name": "Circuit",
				"Count": 15
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "HighCapacitySteampack",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "HighPressureSteampack",
	"Input":{
		"Items":[
			{
				"Name": "SteelParts",
				"Count": 6
			},
			{
				"Name": "SteelPlate",
				"Count": 2
			},
			{
				"Name": "CopperPipe",
				"Count": 30
			},
			{
				"Name": "Circuit",
				"Count": 15
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "HighPressureSteampack",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Jetpack",
	"Input":{
		"Items":[
			{
				"Name": "AluminiumParts",
				"Count": 10
			},
			{
				"Name": "AluminiumPlate",
				"Count": 3
			},
			{
				"Name": "AluminiumPipe",
				"Count": 6
			},
			{
				"Name": "AdvancedCircuit",
				"Count": 10
			},
			{
				"Name": "AluminiumElectricEngine",
				"Count": 2
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Jetpack",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "AdvancedJetpack",
	"Input":{
		"Items":[
			{
				"Name": "StainlessSteelParts",
				"Count": 10
			},
			{
				"Name": "StainlessSteelPlate",
				"Count": 3
			},
			{
				"Name": "StainlessSteelPipe",
				"Count": 6
			},
			{
				"Name": "Processor",
				"Count": 10
			},
			{
				"Name": "StainlessSteelElectricEngine",
				"Count": 2
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "AdvancedJetpack",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "AntigravityUnit",
	"Input":{
		"Items":[
			{
				"Name": "HardMetalParts",
				"Count": 20
			},
			{
				"Name": "HardMetalPlate",
				"Count": 2
			},
			{
				"Name": "HardMetalPipe",
				"Count": 6
			},
			{
				"Name": "QuantumProcessor",
				"Count": 10
			},
			{
				"Name": "Catalyst",
				"Count": 4
			},
			{
				"Name": "HardMetalElectricEngine",
				"Count": 8
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "AntigravityUnit",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Plank",
	"Input":{
		"Items":[
			{
				"Name": "Log",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Plank",
				"Count": 2
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Chair",
	"Input":{
		"Items":[
			{
				"Name": "Plank",
				"Count": 4
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Chair",
				"Count": 1
			}
		]
	}, 
	"Ticks" : 20 
})

recipes_hand.append({
	"Name": "CopperChair",
	"Input":{
		"Items":[
			{
				"Name": "Chair",
				"Count": 1
			},
			{
				"Name": "CopperPlate",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "CopperChair",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Ladder",
	"Input":{
		"Items":[
			{
				"Name": "Plank",
				"Count": 4
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Ladder",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Door",
	"Input":{
		"Items":[
			{
				"Name": "Plank",
				"Count": 8
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Door",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Window",
	"Input":{
		"Items":[
			{
				"Name": "Glass",
				"Count": 2
			},
			{
				"Name": "Plank",
				"Count": 2
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Window",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "PlasticWindow",
	"Input":{
		"Items":[
			{
				"Name": "Glass",
				"Count": 2
			},
			{
				"Name": "Plastic",
				"Count": 2
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "PlasticWindow",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Table",
	"Input":{
		"Items":[
			{
				"Name": "Plank",
				"Count": 6
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Table",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Bed",
	"Input":{
		"Items":[
			{
				"Name": "Plank",
				"Count": 8
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Bed",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Rack",
	"Input":{
		"Items":[
			{
				"Name": "Plank",
				"Count": 4
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Rack",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "WoodenStairs",
	"Input":{
		"Items":[
			{
				"Name": "WoodenPlanks",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "WoodenStairs",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Stairs",
	"Input":{
		"Items":[
			{
				"Name": "Bricks",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Stairs",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Fence",
	"Input":{
		"Items":[
			{
				"Name": "Plank",
				"Count": 3
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Fence",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "SteelFence",
	"Input":{
		"Items":[
			{
				"Name": "SteelParts",
				"Count": 3
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "SteelFence",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "StainlessSteelFence",
	"Input":{
		"Items":[
			{
				"Name": "StainlessSteelParts",
				"Count": 3
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "StainlessSteelFence",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "Flashlight",
	"Input":{
		"Items":[
			{
				"Name": "SteelPipe",
				"Count": 1
			},
			{
				"Name": "SteelLamp",
				"Count": 1
			}
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "Flashlight",
				"Count": 1
			}
		]
	},
	"Ticks" : 20
})

recipes_hand.append({
	"Name": "ConcreteTiles",
	"Input":{
		"Items":[
			{
				"Name": "Concrete",
				"Count": 1
			},		
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "ConcreteTiles",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 20,
})
recipes_hand.append({
	"Name": "ConcreteSmallTiles",
	"Input":{
		"Items":[
			{
				"Name": "Concrete",
				"Count": 1
			},		
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "ConcreteSmallTiles",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 20,
})
recipes_hand.append({
	"Name": "ConcreteBricks",
	"Input":{
		"Items":[
			{
				"Name": "Concrete",
				"Count": 1
			},		
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "ConcreteBricks",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 20,
})
recipes_hand.append({
	"Name": "ReinforcedConcreteTiles",
	"Input":{
		"Items":[
			{
				"Name": "ReinforcedConcrete",
				"Count": 1
			},		
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "ReinforcedConcreteTiles",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 20,
})
recipes_hand.append({
	"Name": "ReinforcedConcreteSmallTiles",
	"Input":{
		"Items":[
			{
				"Name": "ReinforcedConcrete",
				"Count": 1
			},		
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "ReinforcedConcreteSmallTiles",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 20,
})
recipes_hand.append({
	"Name": "ReinforcedConcreteBricks",
	"Input":{
		"Items":[
			{
				"Name": "ReinforcedConcrete",
				"Count": 1
			},		
		]
	},
	"Output":{
		"Items":[
			{
				"Name": "ReinforcedConcreteBricks",
				"Count": 1
			}
		]
	},
	
	"Ticks" : 20,
})

for r in recipes_hand:
	r["Locked"] = True

objects_array.append({ "Class": base_recipe,
	"Name": "Hand" + base_recipe,
	"Recipes": recipes_hand
})

objects_array.append({ "Class": base_recipe,
	"Name": "Press" + base_recipe,
	"Recipes": recipes_press
})

data = {
	"Objects": objects_array
}

write_file("Generated/Recipes/misc_hand.json", data);