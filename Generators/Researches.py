from Common import *
from Materials import *
import copy
from NuclearResearches import *
from EquipmentResearches import *
from PartsResearchHelper import *

researches = []

tier_researches = [
	"MineralScan",
	"MineralScan",
	"SteelProduction",
	"AluminiumProduction",
	"StainlessSteelProduction",
	"TitaniumProduction",
	"HardMetalProduction",
	"NeutroniumProduction",
	"NeutroniumProduction",
	"NeutroniumProduction",
	"NeutroniumProduction",
	"NeutroniumProduction",
	"NeutroniumProduction",
]

csv = []

def append_levels(research_base):
	mini = research_base["Levels"][0] if "Levels" in research_base else 0
	maxi = research_base["Levels"][1] + 1 if "Levels" in research_base else 1
	for i in range(mini, maxi):
		thisLevel = i - mini
		research = copy.deepcopy(research_base)

		if "RequiredResearch" not in research:
			research["RequiredResearch"] = []

		if i != mini:
			research["IsUpgrade"] = True
			research["MainResearch"] = False
			research["CompleteByDefault"] = False
			research["Name"] = research["Name"] + str(thisLevel)
			if i != mini + 1:
				research["RequiredResearch"] = [research_base["Name"] + str(thisLevel - 1)]
			else:
				research["RequiredResearch"] = [research_base["Name"]]

			research["RequiredResearch"].append(tier_researches[i])

		if "RequiredResearchArr" in research:
			if len(research["RequiredResearchArr"]) > thisLevel:
				research["RequiredResearch"].extend(research["RequiredResearchArr"][thisLevel])

		if "MainResearchArr" in research and research["MainResearchArr"][thisLevel] == True:
			research["MainResearch"] = True

		if "Unlocks" in research:
			unl = copy.deepcopy(research["Unlocks"])
			research["Unlocks"] = []
			
			new = []
			for j in unl:
				new.append([j[0], j[1].replace("%Material%", tier_material[i])])                
			research["Unlocks"].append(new)
		
		CostMul = research["CostMul"] if "CostMul" in research else 1

		research["Level"] = thisLevel
		research["Levels"] = [i,i]
		research["DataPoints"] = {"Items" : [{
			"Name": "Computations",
			"Count": tiers_base_cost[i] * CostMul
			}]
		}
    
		researches.append(research)

append_levels({
	"Class": "StaticResearch",
	"Name": "MineralsScan" + static_research,
	"LabelParts": [["MineralsScan", "researches"]],
	"RequiredResearch": [],
	"Unlocks": [["Hand" + base_recipe, tier_material[0] + "Furnace"],["Hand" + base_recipe, "SandSurface"],["Hand" + base_recipe, "GravelSurface"]],
	"CompleteByDefault": True,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdditionalStorage" + static_research,
	"LabelParts": [["AdditionalStorage", "researches"]],
	"RequiredResearch": ["MineralsScan" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Chest"] ],
	"Levels":[0,7],
	"CompleteByDefault": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SingleTypeStorage" + static_research,
	"LabelParts": [["SingleTypeStorage", "researches"]],
	"RequiredResearch": ["AdditionalStorage" + static_research ],
	
	"Levels":[1,7],
	
	"Unlocks": [["Hand" + base_recipe, "%Material%ItemRack"] ],
})
append_levels({
	"Class": "StaticResearchBonusInventory",
	"Name": "InventoryUpgrade" + static_research,
	"LabelParts": [["InventoryUpgrade", "researches"]],
	"RequiredResearchArr": [["AdditionalStorage"],["AdditionalStorage1"],["AdditionalStorage2"],["AdditionalStorage3"],["AdditionalStorage4"],["AdditionalStorage5"],["AdditionalStorage6"],[],[],[],[],[],[],[]],
	"Unlocks": [],
	"Levels": [0,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Electricity" + static_research,
	"LabelParts": [["Electricity", "researches"]],
	"RequiredResearch": ["MineralScan"+static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[1] + "Connector"],["Hand" + base_recipe, tier_material[1] + "HandGenerator"]],
	"CompleteByDefault": True,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "ElectricFurnace" + static_research,
	"LabelParts": [["ElectricFurnace", "machines"]],
	"Levels": [2,7],
	"RequiredResearch": ["CopperWire" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%ElectricFurnace"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "ElectricalSwitch" + static_research,
	"LabelParts": [["ElectricalSwitch", "machines"]],
	"RequiredResearch": ["CopperWire" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[2] + "ElectricalSwitch"]],
	"Levels": [2,2],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Diode" + static_research,
	"LabelParts": [["Diode", "machines"]],
	
	"RequiredResearch": ["ElectricalSwitch" + static_research],
	"Levels": [2,7],
	
	"Unlocks": [["Hand" + base_recipe, "%Material%Diode"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "PowerGeneration" + static_research,
	"LabelParts": [["PowerGeneration", "researches"]],
	"RequiredResearch": ["Electricity" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%CompactGenerator"] ],
	"CompleteByDefault": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Electrolysis" + static_research,
	"LabelParts": [["Electrolysis", "researches"]],
	"RequiredResearch": ["SteelProduction" + static_research], 
	"Levels": [2,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Electrolyzer"] ],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SteelProduction" + static_research,
	"LabelParts": [["SteelProduction", "researches"]],
	"RequiredResearch": ["Drying"+static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%BlastFurnace"] ],
	"AlsoUnlocks": get_parts_unlocks(tier_material[2]),
	"MainResearch": True,
	"CostMul": 5
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdvancedSmelting" + static_research,
	"LabelParts": [["AdvancedSmelting", "researches"]],
	"RequiredResearch": ["SteelProduction" + static_research],
	"Levels": [2,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%ArcSmelter"] ],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SolarPanel" + static_research,
	"LabelParts": [["SolarPanel", "machines"]],
	"RequiredResearch": ["SiliconWafer" + static_research],
	"Levels": [3,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%SolarPanel"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AluminiumProduction" + static_research,
	"LabelParts": [["AluminiumProduction", "researches"]],
	"RequiredResearch": ["AdvancedSmelting" + static_research, "Electrolysis" + static_research],
	"Unlocks": get_parts_unlocks(tier_material[3]),
	"Levels": [3,3],
	"CostLevelOffset": -1,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "GasTurbine" + static_research,
	"LabelParts": [["GasTurbine", "machines"]],
	"RequiredResearch": ["MassivePowerGeneration" + static_research],
	"Levels": [4,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%GasTurbine"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Smelting" + static_research,
	"LabelParts": [["Smelting", "researches"]],
	"RequiredResearch": ["MineralsScan"+static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Smelter"]],
	"Levels": [0,2],
	"CompleteByDefault": True,
	"MainResearch": True
})
append_equipment([-1,3], append_levels, researches)
append_levels({
	"Class": "StaticResearch",
	"Name": "Metalwork" + static_research,
	"LabelParts": [["Metalwork", "researches"]],
	"RequiredResearch": ["Smelting"+static_research],
	"Unlocks": get_parts_unlocks(tier_material[1]),
	"Levels": [1,1],
	"CompleteByDefault": True,
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Valve" + static_research,
	"LabelParts": [["Vent", "machines"]],
	"RequiredResearch": ["Metalwork" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[1] + "Vent"]],
	"Levels": [1,1],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "BasicMachines" + static_research,
	"LabelParts": [["BasicMachines", "researches"]],
	"RequiredResearch": ["Metalwork" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Macerator"],
	["Hand" + base_recipe, "%Material%AutomaticHammer"]],
	"CostMul":0.25,
	"MainResearch": True,
	"Description": [["BasicMachinesDescription", "ui"]]
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Flywheel" + static_research,
	"LabelParts": [["Flywheel", "machines"]],
	"RequiredResearch": ["BasicMachines" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[2] + "Flywheel"]],
	"Levels": [2,2],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Destroyer" + static_research,
	"LabelParts": [["Destroyer", "machines"]],
	"Levels": [1,7],
	"RequiredResearch": ["Furnace" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Destroyer"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Pump" + static_research,
	"LabelParts": [["Pump", "machines"]],
	"RequiredResearch": ["Automatization" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Pump"] ],
	"CostMul":0.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Container" + static_research,
	"LabelParts": [["Container", "machines"]],
	"RequiredResearch": ["Pump" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Container"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "FluidFurnace" + static_research,
	"LabelParts": [["FluidFurnace", "machines"]],
	"RequiredResearch": ["Furnace" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%FluidFurnace"] ],
	"Levels": [1,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Automatization" + static_research,
	"LabelParts": [["Automatization", "researches"]],
	"RequiredResearch": ["BasicMachines" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%RobotArm"],
	["Hand" + base_recipe, "%Material%Conveyor"],
	["Hand" + base_recipe, "%Material%Splitter"]],
	"CostMul":0.25,
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "OverflowPump" + static_research,
	"LabelParts": [["OverflowPump", "machines"]],
	"RequiredResearch": ["Pump" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%OverflowPump"]],
	"Levels": [1,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AutomaticMining" + static_research,
	"LabelParts": [["AutomaticMining", "researches"]],
	"RequiredResearch": ["Automatization" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%DrillingRig"] ],
	"CostMul":0.5,
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Cutting" + static_research,
	"LabelParts": [["Cutting", "researches"]],
	"RequiredResearch": ["BasicMachines" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%CuttingMachine"] ],
	"MainResearch": True,
	"CostMul":0.25,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Pumpjack" + static_research,
	"LabelParts": [["Pumpjack", "machines"]],
	"RequiredResearch": ["AutomaticMining" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Pumpjack"] ],
	"Levels": [3,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AutomaticFarm" + static_research,
	"LabelParts": [["AutomaticFarm", "machines"]],
	"RequiredResearch": ["Automatization" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%AutomaticFarm"] ],
	"CostMul":0.5,
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "HeatTransferring" + static_research,
	"LabelParts": [["HeatTransferring", "researches"]],
	"RequiredResearch": ["Smelting" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%HeatPipe"] ],
	"Levels":[1,1],
	"CostMul":0.5,
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "KineticHeater" + static_research,
	"LabelParts": [["KineticHeater", "machines"]],
	"RequiredResearch": ["HeatTransferring" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%KineticHeater"] ],
	"Levels":[1,7],
	"CostMul":1,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Radiator" + static_research,
	"LabelParts": [["Radiator", "machines"]],
	"RequiredResearch": ["HeatTransferring" + static_research],
	"Levels": [3,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Radiator"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AtmosphericCondenser" + static_research,
	"LabelParts": [["AtmosphericCondenser", "machines"]],
	"RequiredResearch": ["AutomaticFarm" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%AtmosphericCondenser"] ],
	"CostMul":0.5,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "StirlingEngine" + static_research,
	"LabelParts": [["StirlingEngine", "machines"]],
	"RequiredResearch": ["MineralsScan"+static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%StirlingEngine"] ],
	"CompleteByDefault": True,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Drying" + static_research,
	"LabelParts": [["Drying", "researches"]],
	"RequiredResearch": ["Furnace" + static_research,],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Oven"] ],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DistributedComputing" + static_research,
	"LabelParts": [["DistributedComputing", "researches"]],
	"RequiredResearchArr": [["PowerGeneration"], ["AdvancedCircuit"], ["Processor"], ["QuantumCircuit"], ["QuantumProcessor"], ["QuantumBrain"]],
	"Unlocks": [["Hand" + base_recipe, "%Material%Computer"] ],
	"Levels": [1,7],
	"CompleteByDefault": True,
	"MainResearchArr": [True,True,True,True,True,True,True],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "CopperWire" + static_research,
	"LabelParts": [["CopperWire", "parts"]],
	"RequiredResearch": ["DistributedComputing" + static_research],
	"Levels": [1,1],
	"Unlocks": [["Hand" + base_recipe, "CopperWire"],["Assembler" + base_recipe, "CopperWire"]],
	"CompleteByDefault": True,
	"MainResearch": True,
	"CostMul": 0.125
})
append_levels({
	"Class": "StaticResearch",
	"Name": "CircuitBoard" + static_research,
	"LabelParts": [["CircuitBoard", "parts"]],
	"RequiredResearch": ["CopperWire" + static_research],
	"Levels": [1,1],
	"Unlocks": [["Hand" + base_recipe, "CircuitBoard"]],
	"CostMul":0.25,
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Circuit" + static_research,
	"LabelParts": [["Circuit", "parts"]],
	"RequiredResearch": ["CircuitBoard" + static_research],
	"Unlocks": [["Hand" + base_recipe, "Circuit"],["Assembler" + base_recipe, "Circuit"]],
	"Levels": [1,1],
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Furnace" + static_research,
	"LabelParts": [["Furnace", "machines"]],
	"RequiredResearch": ["StirlingEngine" + static_research],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Furnace"] ],
	"MainResearchArr": [True,True,True,True,True,True,True],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "MassivePowerGeneration" + static_research,
	"LabelParts": [["MassivePowerGeneration", "researches"]],
	"RequiredResearch": ["PowerGeneration" + static_research ],
	"Unlocks": [["Hand" + base_recipe, "%Material%Generator"] ,
	["Hand" + base_recipe, "%Material%Boiler"] ,
	["Hand" + base_recipe, "%Material%SteamTurbine"] ],
	"Levels": [2,7],
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "LogicCircuit",
	"LabelParts": [["LogicCircuit", "machines"]],
	"RequiredResearch": ["Circuit"],
	"Unlocks": [["Hand" + base_recipe, "SteelLogicCircuit"] ,
	["Hand" + base_recipe, "SteelLogicController"] ,
	["Hand" + base_recipe, "SteelLogicInterface"] ,
	["Hand" + base_recipe, "SteelLogicDisplay"] ,
	["Hand" + base_recipe, "SteelLogicWire"] ],
	"Levels": [2,2],
	"CostMul": 1.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdvancedCircuit",
	"LabelParts": [["AdvancedCircuit", "parts"]],
	"RequiredResearch": ["Separator", "Circuit"],
	"Levels": [2,2],
	"Unlocks": [["Hand" + base_recipe, "AdvancedCircuit"],["Assembler" + base_recipe, "AdvancedCircuit"]],
	"MainResearch": True,
	"CostMul":2.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "GoldWire",
	"LabelParts": [["GoldWire", "parts"]],
	"RequiredResearch": ["AdvancedCircuit", "OreWasher"],
	"Levels": [2,2],
	"Unlocks": [["Hand" + base_recipe, "GoldWire"],["Assembler" + base_recipe, "GoldWire"]],
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdvancedCircuitBoard",
	"LabelParts": [["AdvancedCircuitBoard", "parts"]],
	"RequiredResearch": ["GoldWire", "PyrolysisUnit"],
	"Levels": [3,3],
	"Unlocks": [["Hand" + base_recipe, "AdvancedCircuitBoard"],["Assembler" + base_recipe, "AdvancedCircuitBoard"]],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SiliconWafer" + static_research,
	"LabelParts": [["SiliconWafer", "parts"]],
	"RequiredResearch": ["AdvancedCircuit" + static_research],
	"Unlocks": [["Assembler" + base_recipe, "SiliconWafer"]],
	"Levels": [3,3],
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Processor" + static_research,
	"LabelParts": [["Processor", "parts"]],
	"RequiredResearch": ["SiliconWafer", "AdvancedCircuitBoard"],
	"Unlocks": [["Hand" + base_recipe, "Processor"],["Assembler" + base_recipe, "Processor"],["Assembler" + base_recipe, "Processor2"]],
	"Levels": [3,3],
	"MainResearch": True,
	"CostMul":2.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "QuantumCore",
	"LabelParts": [["QuantumCore", "parts"]],
	"RequiredResearch": ["Processor", "ChemicalBath"],
	"Levels": [4,4],
	"Unlocks": [["Hand" + base_recipe, "QuantumCore"],["Assembler" + base_recipe, "QuantumCore"]],
	"MainResearch": True,
	"CostMul":2.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "QuantumCircuit",
	"LabelParts": [["QuantumCircuit", "parts"]],
	"RequiredResearch": ["QuantumCore"],
	"Levels": [4,4],
	"Unlocks": [["Hand" + base_recipe, "QuantumCircuit"],["Assembler" + base_recipe, "QuantumCircuit"]],
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "QuantumProcessor",
	"LabelParts": [["QuantumProcessor", "parts"]],
	"RequiredResearch": ["QuantumCircuit"],
	"Levels": [5,5],
	"Unlocks": [["Hand" + base_recipe, "QuantumProcessor"],["Assembler" + base_recipe, "QuantumProcessor"]],
	"MainResearch": True,
	"CostMul":2.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "QuantumBrain",
	"LabelParts": [["QuantumBrain", "parts"]],
	"RequiredResearch": ["QuantumProcessor"],
	"Levels": [6,6],
	"Unlocks": [["Hand" + base_recipe, "QuantumBrain"],["Assembler" + base_recipe, "QuantumBrain"]],
	"MainResearch": True,
	"CostMul":2.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "MetalConstructions" + static_research,
	"LabelParts": [["MetalConstructions", "researches"]],
	"RequiredResearch": ["Metalwork" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Corner"] ,
	["Hand" + base_recipe, "%Material%Casing"] ,
	["Hand" + base_recipe, "%Material%Beam"] ],
	"Levels": [1,7],
	"Chapter":"Decorations"+static_chapter,
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Scaffold" + static_research,
	"LabelParts": [["Scaffold", "researches"]],
	"RequiredResearch": ["MetalConstructions" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Scaffold"] ],
	"Levels": [1,7],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Chemistry" + static_research,
	"LabelParts": [["Chemistry", "researches"]],
	"RequiredResearch": ["ElectricEngine" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%ChemReactor"] ],
	"Levels": [2,7],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Catalyst" + static_research,
	"LabelParts": [["Catalyst", "parts"]],
	"RequiredResearch": ["Chemistry" + static_research],
	"Unlocks": [["Hand" + base_recipe, "Catalyst"],["Assembler" + base_recipe, "Catalyst"]],
	"Levels": [2,2],
	"MainResearch": True,
	"CostMul":5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "IndustrialChemReactor" + static_research,
	"LabelParts": [["IndustrialChemReactor", "machines"]],
	"RequiredResearch": ["Catalyst" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialChemReactor"] ],
	"Levels": [3,7],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "FuelChemistry" + static_research,
	"LabelParts": [["FuelChemistry", "researches"]],
	"RequiredResearch": ["IndustrialChemReactor" + static_research],
	"Unlocks": [["IndustrialChemReactor" + base_recipe, "Superfuel"], ["IndustrialChemReactor" + base_recipe, "RocketFuel"]],
	"Levels": [3,3],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "FuelChemistry2" + static_research,
	"LabelParts": [["FuelChemistry2", "researches"]],
	"RequiredResearch": ["FuelChemistry" + static_research],
	"Unlocks": [["IndustrialChemReactor" + base_recipe, "RocketFuel2"], ["IndustrialChemReactor" + base_recipe, "Superfuel2"]],
	"Levels": [3,3],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Sifter" + static_research,
	"LabelParts": [["Sifter", "machines"]],
	"RequiredResearch": ["Chemistry" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Sifter"] ],
	"Levels": [3,7],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Separator" + static_research,
	"LabelParts": [["Separator", "machines"]],
	"RequiredResearch": ["ElectricEngine" + static_research],
	"Levels": [2,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Separator"] ],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "ElectricEngine" + static_research,
	"LabelParts": [["ElectricEngine", "machines"]],
	"RequiredResearch": ["Electrolysis" + static_research],
	"Levels": [2,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%ElectricEngine"] ],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "BiElectricEngine" + static_research,
	"LabelParts": [["BiElectricEngine", "machines"]],
	"RequiredResearch": ["ElectricEngine" + static_research],
	"Levels": [2,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%BiElectricEngine"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "OreWasher" + static_research,
	"LabelParts": [["OreWasher", "machines"]],
	"Levels": [2,7],
	"RequiredResearch": ["Separator" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%OreWasher"] ],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Mixer" + static_research,
	"LabelParts": [["Mixer", "machines"]],
	"RequiredResearch": ["OreWasher" + static_research],
	"Levels": [2,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Mixer"] ],
	"MainResearch": True,
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "ChemicalBath" + static_research,
	"LabelParts": [["ChemicalBath", "machines"]],
	"RequiredResearch": ["IndustrialChemReactor" + static_research],
	"Levels": [3,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%ChemicalBath"] ],
	"MainResearch": True,
	"CostMul":5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "OilCrackingTower" + static_research,
	"LabelParts": [["OilCrackingTower", "machines"]],
	"RequiredResearch": ["FuelChemistry" + static_research],
	"Levels": [4,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%OilCrackingTower"] ],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "CombustionEngine" + static_research,
	"LabelParts": [["CombustionEngine", "machines"]],
	"RequiredResearch": ["IndustrialChemReactor" + static_research],
	"Levels": [3,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%CombustionEngine"] ],
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "StainlessSteelProduction" + static_research,
	"LabelParts": [["StainlessSteelProduction", "researches"]],
	"RequiredResearch": ["Chemistry" + static_research, "AluminiumProduction" + static_research],
	"Unlocks": get_parts_unlocks(tier_material[4]),
	"AlsoUnlocks": [["Hand" + base_recipe, "Cell"]],
	"Levels": [4,4],
	"CostLevelOffset": -1,
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdvancedSeparation" + static_research,
	"LabelParts": [["AdvancedSeparation", "researches"]],
	"RequiredResearch": ["AluminiumProduction" + static_research],
	"Levels": [3,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialSeparator"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "SmallBattery" + static_research,
	"LabelParts": [["SmallBattery", "machines"]],
	"RequiredResearch": ["AluminiumProduction" + static_research],
	"Levels": [3,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%SmallBattery"] ],
	"MainResearch": True,
	"CostMul":1.5,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "BatteryBox" + static_research,
	"LabelParts": [["BatteryBox", "machines"]],
	"RequiredResearch": ["SmallBattery" + static_research],
	"Levels": [4,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%BatteryBox"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "TitaniumProduction" + static_research,
	"LabelParts": [["TitaniumProduction", "researches"]],
	"RequiredResearch": ["IndustrialSmelting" + static_research],
	"Unlocks": get_parts_unlocks(tier_material[5]),
	"Levels": [4,4],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "IndustrialBoiler" + static_research,
	"LabelParts": [["IndustrialBoiler", "machines"]],
	"RequiredResearch": ["TitaniumProduction" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialBoiler"],["Connector" + base_recipe, "%Material%IndustrialBoiler"]],
	"Levels": [5,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "IndustrialSteamTurbine" + static_research,
	"LabelParts": [["IndustrialSteamTurbine", "machines"]],
	"RequiredResearch": ["IndustrialBoiler" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialSteamTurbine"],["Connector" + base_recipe, "%Material%IndustrialSteamTurbine"]],
	"Levels": [5,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "IndustrialGenerator" + static_research,
	"LabelParts": [["IndustrialGenerator", "machines"]],
	"RequiredResearch": ["IndustrialSteamTurbine" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialGenerator"],["Connector" + base_recipe, "%Material%IndustrialGenerator"]],
	"Levels": [5,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Freezer" + static_research,
	"LabelParts": [["Freezer", "machines"]],
	"RequiredResearch": ["TitaniumProduction" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Freezer"] ],
	"Levels": [5,7],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "HardMetalProduction" + static_research,
	"LabelParts": [["HardMetalProduction", "researches"]],
	"RequiredResearch": ["Freezer" + static_research],
	"Unlocks": get_parts_unlocks(tier_material[6]),
	"Levels": [5,5],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "FusionReactor" + static_research,
	"LabelParts": [["FusionReactor", "machines"]],
	"RequiredResearch": ["HardMetalProduction" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%FusionReactor"] ],
	"Levels": [6,7],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "NeutroniumProduction" + static_research,
	"LabelParts": [["NeutroniumProduction", "researches"]],
	"RequiredResearch": ["FusionReactor" + static_research],
	"Unlocks": get_parts_unlocks(tier_material[7]),
	"Levels": [6,6],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "UltimateCatalyst" + static_research,
	"LabelParts": [["UltimateCatalyst", "parts"]],
	"RequiredResearch": ["NeutroniumProduction" + static_research],
	"Unlocks": [["Hand" + base_recipe, "UltimateCatalyst"],["Assembler" + base_recipe, "UltimateCatalyst"]],
	"Levels": [6,6],
	"MainResearch": True,
})
append_levels({
	 "Class": "StaticResearch",
	 "Name": "Portal" + static_research,
	 "LabelParts": [["Portal", "machines"]],
	 "RequiredResearch": ["UltimateCatalyst", "QuantumBrain"],
	 "Unlocks": [["Hand" + base_recipe, "%Material%Portal"] ],
	 "Levels": [7,7],
	 "MainResearch": True,
	 "CostMul": 5
 })
append_levels({
	"Class": "StaticResearch",
	"Name": "FissionReactor" + static_research,
	"LabelParts": [["FissionReactor", "machines"]],
	"RequiredResearch": ["UraniumCell" + static_research],
	"Levels": [5,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%FissionReactor"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "UraniumCell" + static_research,
	"LabelParts": [["UraniumCell", "parts"]],
	"RequiredResearch": ["TitaniumProduction" + static_research],
	"Levels": [5,5],
	"Unlocks": [["Hand" + base_recipe, "UraniumCell"],["Assembler" + base_recipe, "UraniumCell"]],
})
append_nuclear([7,-7], append_levels, researches)
append_levels({
	"Class": "StaticResearch",
	"Name": "IndustrialSmelting" + static_research,
	"LabelParts": [["IndustrialSmelting", "researches"]],
	"RequiredResearch": ["StainlessSteelProduction" + static_research],
	"Levels": [4,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialSmelter"] ],
	"MainResearch": True,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Fermentation" + static_research,
	"LabelParts": [["Fermentation", "researches"]],
	"Levels": [3,7],
	"RequiredResearch": ["Chemistry" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Fermenter"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "InductionCoil" + static_research,
	"LabelParts": [["InductionCoil", "machines"]],
	"RequiredResearch": ["IndustrialSmelting" + static_research],
	"Levels": [4,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%InductionCoil"] ],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "IndustrialElectricEngine" + static_research,
	"LabelParts": [["IndustrialElectricEngine", "machines"]],
	"RequiredResearch": ["InductionCoil" + static_research],
	"Levels": [4,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%IndustrialElectricEngine"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Terminal" + static_research,
	"LabelParts": [["Terminal", "machines"]],
	"Levels": [4,4],
	"RequiredResearch": ["StainlessSteelProduction" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[4] + "Terminal"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "FlatTerminal" + static_research,
	"LabelParts": [["FlatTerminal", "machines"]],
	"Levels": [4,4],
	"RequiredResearch": ["Terminal" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[4] + "FlatTerminal"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Constructor" + static_research,
	"LabelParts": [["Constructor", "machines"]],
	"RequiredResearch": ["Assembler" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Constructor"] ],
	"Levels": [2, 7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Assembler" + static_research,
	"LabelParts": [["Assembler", "machines"]],
	"RequiredResearch": ["Automatization" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Assembler"] ],
	"Levels": [1,7],
	"CostMul":0.5,
	"MainResearch": True
})
append_levels({
	"Class": "StaticResearch",
	"Name": "BigTerminal" + static_research,
	"LabelParts": [["BigTerminal", "machines"]],
	"RequiredResearch": ["Terminal" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[5] + "BigTerminal"]],
	"Levels": [4,4],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "BigFlatTerminal" + static_research,
	"LabelParts": [["BigFlatTerminal", "machines"]],
	"RequiredResearch": ["BigTerminal" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[5] + "BigFlatTerminal"]],
	"Levels": [4,4],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "HugeTerminal" + static_research,
	"LabelParts": [["HugeTerminal", "machines"]],
	"RequiredResearch": ["BigTerminal" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[6] + "HugeTerminal"]],
	"Levels": [5,5],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "HugeFlatTerminal" + static_research,
	"LabelParts": [["HugeFlatTerminal", "machines"]],
	"RequiredResearch": ["HugeTerminal" + static_research],
	"Unlocks": [["Hand" + base_recipe, tier_material[6] + "HugeFlatTerminal"]],
	"Levels": [5,5],
}) 
append_levels({
	"Class": "StaticResearch",
	"Name": "PyrolysisUnit" + static_research,
	"LabelParts": [["PyrolysisUnit", "machines"]],
	"RequiredResearch": ["Mixer" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%PyrolysisUnit"] ],
	"Levels": [3,7],
	"MainResearch": True,
})
	
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeWood" + static_research,
	"RequiredResearch": ["Cutting" + static_research],
	"LabelParts": [["DecorativeWood", "researches"]],
	"Unlocks": [["Hand" + base_recipe, "WoodenPlanks"],["Hand" + base_recipe, "WoodenStairs"],["Hand" + base_recipe, "Bed"],["Hand" + base_recipe, "Door"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeWood2" + static_research,
	"LabelParts": [["DecorativeWood", "researches"], [level_labels[1], "common"]],
	"RequiredResearch": ["DecorativeWood" + static_research],
	"Unlocks": [["Hand" + base_recipe, "Chair"],["Hand" + base_recipe, "Fence"],["Hand" + base_recipe, "Ladder"],["Hand" + base_recipe, "Rack"],["Hand" + base_recipe, "Table"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Fence" + static_research,
	"LabelParts": [["Fence", "misc"]],
	"RequiredResearch": ["DecorativeWood2" + static_research],
	"Unlocks": [["Hand" + base_recipe, "SteelFence"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Fence1" + static_research,
	"LabelParts": [["Fence", "misc"], [level_labels[1], "common"]],
	"RequiredResearch": ["Fence" + static_research],
	"Unlocks": [["Hand" + base_recipe, "StainlessSteelFence"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeWood4" + static_research,
	"LabelParts": [["DecorativeWood", "researches"], [level_labels[3], "common"]],
	"RequiredResearch": ["DecorativeWood2" + static_research],
	"Unlocks": [["Hand" + base_recipe, "CopperChair"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeWood3" + static_research,
	"LabelParts": [["DecorativeWood", "researches"], [level_labels[2], "common"]],
	"RequiredResearch": ["DecorativeWood2" + static_research, "AdvancedSmelting" + static_research],
	"Unlocks": [["Hand" + base_recipe, "Window"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativePlastic" + static_research,
	"LabelParts": [["DecorativePlastic", "researches"]],
	"RequiredResearch": ["Chemistry" + static_research, "PyrolysisUnit" + static_research, "DecorativeWood3" + static_research],
	"Unlocks": [["Hand" + base_recipe, "PlasticWindow"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "PlasticBlock" + static_research,
	"LabelParts": [["PlasticBlock", "misc"]],
	"RequiredResearch": ["DecorativePlastic" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "PlasticBlock"],["Press" + base_recipe, "PlasticBlock"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "BasicPlatform" + static_research,
	"LabelParts": [["BasicPlatform", "misc"]],
	"CompleteByDefault": True,
	"Unlocks": [["Hand" + base_recipe, "BasicPlatform"], ["Press" + base_recipe, "BasicPlatform"]],
	"RequiredResearch": []
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeStone" + static_research,
	"LabelParts": [["DecorativeStone", "researches"]],
	"RequiredResearch": ["Press"+static_research], 
	"Unlocks": [["Hand" + base_recipe, "StoneTiles"], ["CuttingMachine" + base_recipe, "StoneTiles"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeStone2" + static_research,
	"LabelParts": [["DecorativeStone", "researches"], [level_labels[1], "common"]],
	"RequiredResearch": ["DecorativeStone" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "DarkTiles"],["Hand" + base_recipe, "RedTiles"],["CuttingMachine" + base_recipe, "DarkTiles"],["CuttingMachine" + base_recipe, "RedTiles"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "GlassBlock" + static_research,
	"LabelParts": [["GlassBlock", "misc"]],
	"RequiredResearch": ["Press"+static_research], 
	"Unlocks": [["Hand" + base_recipe, "GlassBlock"],["Press" + base_recipe, "GlassBlock"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeStone3" + static_research,
	"LabelParts": [["DecorativeStone", "researches"], [level_labels[2], "common"]],

	"RequiredResearch": ["DecorativeStone2" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "DarkBricks"],["Hand" + base_recipe, "RedBricks"],["Hand" + base_recipe, "Bricks"],["CuttingMachine" + base_recipe, "DarkBricks"],["CuttingMachine" + base_recipe, "RedBricks"],["CuttingMachine" + base_recipe, "Bricks"]],
	
	
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeStone4" + static_research,
	"LabelParts": [["DecorativeStone", "researches"], [level_labels[3], "common"]],
	"RequiredResearch": ["DecorativeStone3" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "Stairs"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeConcrete" + static_research,
	"LabelParts": [["DecorativeConcrete", "researches"]],
	"RequiredResearch": ["Mixer" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "ConcreteTiles"], ["CuttingMachine" + base_recipe, "ConcreteTiles"],
			 ["Hand" + base_recipe, "ConcreteBeam"], ["Press" + base_recipe, "ConcreteBeam"]],
	"Levels": [1, 2],
})

for index, crafter, item, crafter2 in [
		(1, "Hand", "ConcreteSmallTiles", "CuttingMachine"), 
		(2, "Hand", "ConcreteBeam2", "Press"),
        (3, "Hand", "ConcreteRamp3", "Press"),
        (4, "Hand", "ConcreteRamp", "Press"),
        (5, "Hand", "ConcreteRamp2", "Press"),
        (6, "Hand", "DangerBlock", "Press")
	]:
	append_levels({
		"Class": "StaticResearch",
		"Name": "DecorativeConcrete" + item + static_research,
		"LabelParts": [["DecorativeConcrete", "researches"], [level_labels[index], "common"]],
		"RequiredResearch": ["DecorativeConcrete" + static_research], 
		"Unlocks": [[crafter + base_recipe, item], [crafter2 + base_recipe, item]],
		"Levels": [3, 3],
	})
     
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeReinforcedConcrete" + static_research,
	"LabelParts": [["ReinforcedConcrete", "researches"]],
	"RequiredResearch": ["DecorativeConcrete" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "ReinforcedConcreteTiles"], ["CuttingMachine" + base_recipe, "ReinforcedConcreteTiles"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeReinforcedConcrete2" + static_research,
	"LabelParts": [["ReinforcedConcrete", "researches"], [level_labels[1], "common"]],

	"RequiredResearch": ["DecorativeReinforcedConcrete" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "ReinforcedConcreteSmallTiles"], ["CuttingMachine" + base_recipe, "ReinforcedConcreteSmallTiles"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorativeReinforcedConcrete3" + static_research,
	"LabelParts": [["ReinforcedConcrete", "researches"], [level_labels[2], "common"]],
	"RequiredResearch": ["DecorativeReinforcedConcrete2" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "ReinforcedConcreteBricks"], ["CuttingMachine" + base_recipe, "ReinforcedConcreteBricks"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorationClay" + static_research,
	"LabelParts": [["DecorationClay", "researches"]],
	"RequiredResearch": ["Drying" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "TerracottaTiles"], ["CuttingMachine" + base_recipe, "TerracottaTiles"]],
	"Levels": [1,1],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "DecorationClay2" + static_research,
	"LabelParts": [["DecorationClay", "researches"], [level_labels[1], "common"]],
	"RequiredResearch": ["DecorationClay" + static_research], 
	"Unlocks": [["Hand" + base_recipe, "TerracottaBricks"], ["CuttingMachine" + base_recipe, "TerracottaBricks"]],
	"Levels": [1,1],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Press" + static_research,
	"LabelParts": [["Press", "machines"]],
	"RequiredResearch": ["SteelProduction"],
	"Levels": [2,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Press"] ],
})
append_levels({
	"Class": "StaticResearchToolUnlock",
	"Name": "PaintTool" + static_research,
	"LabelParts": [["PaintTool", "parts"]],
	"RequiredResearch": ["Press" + static_research],
	"Levels": [1,1],
	"Unlocks": [],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Lamp" + static_research,
	"LabelParts": [["Lamp", "machines"]],
	"RequiredResearch": [],
	"Levels": [1,7],
	"Unlocks": [["Hand" + base_recipe, "%Material%Lamp"] ],
	"CostMul": 0.1,
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Column" + static_research,
	"LabelParts": [["Column", "misc"]],
	"RequiredResearch": ["DecorativeStone" + static_research],
	"Levels": [1,1],
	"Unlocks": [["Hand" + base_recipe, "Column"],["Hand" + base_recipe, "FluetedColumn"],["Press" + base_recipe, "Column"],["Press" + base_recipe, "FluetedColumn"]],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "Sign" + static_research,
	"LabelParts": [["Sign", "machines"]],
	"RequiredResearch": ["Press" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%Sign"] ],
	"Levels": [0,7],
})
append_levels({
	"Class": "StaticResearch",
	"Name": "AdvancedSign" + static_research,
	"LabelParts": [["AdvancedSign", "machines"]],
	"RequiredResearch": ["Sign" + static_research],
	"Unlocks": [["Hand" + base_recipe, "%Material%AdvancedSign"] ],
	"Levels": [2,7]
})
	
data = {
	"Objects": researches
}

csv.append(["InventoryUpgrade", "Inventory Upgrade"])
csv.append(["PlutoniumReaction", "Plutonium Reaction"])
csv.append(["ThoriumReaction", "Thorium Reaction"])
csv.append(["Drying", "Drying"])	
csv.append(["PowerGeneration", "Power Generation"])
csv.append(["Automatization", "Automatization"])
csv.append(["AdditionalStorage", "Additional Storage"])
csv.append(["HeatTransferring", "Heat Transferring"])
csv.append(["BasicMachines", "Basic Machines"])
csv.append(["Container", "Fluid Storage"])
csv.append(["SingleTypeStorage", "Single Type Storage"])
csv.append(["DistributedComputing", "Distributed Computing"])
csv.append(["Electrolysis", "Electrolysis"])
csv.append(["Sign", "Sign"])
csv.append(["Cutting", "Cutting"])
csv.append(["SteelProduction", "Steel Production"])
csv.append(["AutomaticMining", "Automatic Mining"])
csv.append(["MetalConstructions", "Metal Constructions"])	
csv.append(["Chemistry", "Chemistry"])
csv.append(["MassivePowerGeneration", "Massive Power Generation"])
csv.append(["AdvancedSmelting", "Advanced Smelting"])
csv.append(["IndustrialSmelting", "Industrial Smelting"])
csv.append(["Fermentation", "Fermentation"])
csv.append(["AdvancedSeparation", "Advanced Separation"])
csv.append(["NeutroniumProduction", "Neutronium Production"])
csv.append(["AluminiumProduction", "Aluminium Production"])
csv.append(["StainlessSteelProduction", "Stainless Steel Production"])
csv.append(["TitaniumProduction", "Titanium Production"])
csv.append(["HardMetalProduction", "Hard Metal Production"])
csv.append(["MineralsScan", "Minerals Scan"])
csv.append(["Electricity", "Electricity"])
csv.append(["Smelting", "Smelting"])
csv.append(["Metalwork", "Metalwork"])
csv.append(["DecorativeWood", "Decorative Wood"])
csv.append(["DecorativePlastic", "Decorative Plastic"])
csv.append(["DecorativeStone", "Decorative Stone"])
csv.append(["DecorativeConcrete", "Decorative Concrete"])
csv.append(["DecorationClay", "Decoration Clay"])
csv.append(["ReinforcedConcrete", "Decorative Reinforced Concrete"])
csv.append(["AdvancedReflection", "Advanced Reflection"])
csv.append(["ReactionThrottling", "Reaction Throttling"])
csv.append(["FuelChemistry", "Fuel Chemistry"])
csv.append(["FuelChemistry2", "Fuel Chemistry II"])

write_file("Generated/Researches/basic.json", data)
write_file("Loc/source/researches.json", csv)
