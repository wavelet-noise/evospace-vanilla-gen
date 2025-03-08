import json
import os
import errno
import sys
import csv
import re
import shutil

our_path = os.path.dirname(sys.argv[0])

def res_cost(level, mul = 1):
	arr = []
	arr.append({"Name": "Computations", "Count": tiers_base_cost[level] * mul})
		
	return arr

def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)


def round_25(x):
    return round(x*4)/4

def write_file(filename, data):
	if not os.path.exists(os.path.dirname(our_path + "/../Content/" + filename)):
		try:
			os.makedirs(os.path.dirname(our_path + "/../Content/" + filename))
		except OSError as exc: 
			if exc.errno != errno.EEXIST:
				raise 
		
	data_file = open(our_path + "/../Content/" + filename, "w")
	#data_file.write(json.dumps(data, separators=(',', ': ')))
	#data_file.write(json.dumps(data, separators=(',', ':')))
	data_file.write(json.dumps(data, indent=4, sort_keys=True))
	data_file.close()

def write_text_file(filename, data):
	if not os.path.exists(os.path.dirname(our_path + "/../Content/" + filename)):
		try:
			os.makedirs(os.path.dirname(our_path + "/../Content/" + filename))
		except OSError as exc: 
			if exc.errno != errno.EEXIST:
				raise
		
	with open(our_path + "/../Content/" + filename, "w", newline='', encoding='utf-8') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		spamwriter.writerow(["Key", "SourceString"])
		for x in data:
			spamwriter.writerow(x)
			
def CamelToSpaces(name):
	return re.sub(r"([a-z])([A-Z])", r"\g<1> \g<2>", name)
	
def simple_in_out_recipe(name):
	if not hasattr(simple_in_out_recipe, "counter"):
		simple_in_out_recipe.counter = -1
		
	simple_in_out_recipe.counter += 1
	
	return {
		"Name": "SimpleInOutRecipe" + str(simple_in_out_recipe.counter),
		"Input":{
			"Items":[
				{
					"Name": name,
					"Count": 1
				}
			]
		},
		"Output":{
			"Items":[
				{
					"Name": name,
					"Count": 1
				}
			]
		},
		"Ticks": 20
	}
	
level_labels = [
	"I",
	"II",
	"III",
	"IV",
	"V",
	"VI",
	"VII",
	"VIII",
	"IX",
	"X"
]

tiers_name_helper = [
	"",
	"2",
	"3",
	"4",
	"5",
	"6",
	"7",
	"8",
	"9",
	"10",
	"11",
	"12"
]

tiers_base_cost = [
	20, # stone
	200, # copper
	2000, # steel
	20000, # alum
	200000, # ss
	2000000, # tita
	20000000, # hm
	200000000, # neu
	2000000000,
	2000000000,
	2000000000,
	2000000000,
	2000000000,
	2000000000
]

tiers_energy_level = [
	10*20*1,
	10*20*4,
	10*20*4**2,
	10*20*4**3,
	10*20*4**4,
	10*20*4**5,
	10*20*4**6,
	10*20*4**7,
	10*20*4**8,
	10*20*4**9,
	10*20*4**10,
	10*20*4**11,
]

tiers_adv_cost = [
	0,
	0,
	8,
	16,
	32,
	32,
	32,
	16,
	32,
	36,
	38,
	40,
	42,
	44,
	46,
	48,
]

def clamp(val, _min, _max):
	return max(_min, min(val, _max))

def has_hand_recipe(recipes_hand, result):
	for r in recipes_hand:
		if not r["Output"]["Items"][0]["Name"].find(result) == -1:
			return True
			
	return False
	
def get_hand_recipe(recipes_hand, result):
	for r in recipes_hand:
		if not r["Output"]["Items"][0]["Name"].find(result) == -1:
			return r
			
	return None

def create_item(name, count=1):
    return {"Name": name, "Count": count}

def one_item(item_name, count=1):
    return {"Items": [create_item(item_name, count)]}

def items(array, tier=0):
	items = []
	for entry in array:
		if len(entry) == 1:
			item, count_fn = entry[0], 1
		else:
			item, count_fn = entry
		count = count_fn(tier) if callable(count_fn) else count_fn
		if count > 0:
			items.append({
				"Name": item,
				"Count": count
			})

	return {"Items": items}

single_battery_cell_charge = 100000

def battery_mul(level):
	return 4 * pow(5, level)
	
f_machine_bonus = 1.5

fission_fullpower = 7100 * 3.3 * 2 * 1.1 * 2

tiers_numlist = [0,1,2,3,4,5,6,7]

static_item = ""

int32max = 2147483647

quest = "StaticQuest"
qchapter = "StaticQuestChapter"

static_research = ""
static_chapter = "StaticChapter"
static_block = ""
static_surface = ""

static_cover = "StaticCover"

slot_logic = "ItemLogic"

building_cube_logic = "BuildingSurfaceBlockItemLogic"
building_single_logic = "BuildingSingleBlockItemLogic"
building_drill_logic = "BuildingDrillBlockItemLogic"
building_plane_logic = "BuildingPlaneBlockItemLogic"
building_decoration_logic = "BuildingDecorationItemLogic"
building_prop_logic = "BuildingPropItemLogic"
building_big_prop_logic = "BuildingPropItemLogic"

cover_item_logic = "CoverItemLogic"

building_brush_slot_logic = "BuildingBrushItemLogic"
assembler_r_dict = "AssemblerRecipeDictionary"
r_dict = "RecipeDictionary"
breaking_recipe = "RecipeDictionary"
ico_generator = "IcoGenerator"

tesselator = "Tesselator"
tesselator_cube = "TesselatorCube"
tesselator_static_mesh = "TesselatorStaticMesh"

item_data = "ItemData"
basic_slot_widget_c = "Gui/BasicStackedSlotWidget.BasicStackedSlotWidget_C"

ico = ""
additive_ico = "Additive"


def parts_ramp(level, factor = 5):
	if level == 0:
		return 0
	if level < 3:
		return level * factor
	else:
		return factor * 3
	
def exp_ramp(level, factor = 2):
	return factor ** level

tiers_res_item = [
	"Computations",
	"Circuit",
	"AdvancedCircuit",
	"Processor",
	"QuantumCircuit",
	"QuantumProcessor",
	"QuantumBrain",
	"QuantumBrain",
	"QuantumBrain",
	"QuantumBrain",
	"QuantumBrain",
	"QuantumBrain",
	"QuantumBrain",
	"QuantumBrain",
	"QuantumBrain",
]

euler = 2.718281