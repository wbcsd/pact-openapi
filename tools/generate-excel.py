import os
import sys
import yaml
import jsonref
from openpyxl import Workbook
from openpyxl.styles import Alignment,PatternFill,Font

# reguirements
# openpyxl = "openpyxl==3.1.5"
# jsonref = "jsonref==1.1.0"
# pyyaml = "pyyaml==6.0.2
# 

def export_to_excel(ws, schema, types):

    # Append the title and header rows
    ws.append(["PACT Simplified Tech Specs", schema["info"]["version"], "", "", "", "", "", "", "", ""])
    ws.append([
        "Property",                     # Column A
        "Mandatory?",	                # Column B
        "Methodology Attribute Name",   # Column C
        "Link to Methodology",	        # Column D
        "User Friendly Description of Attribute",     # Column E
        "Unit",	                        # Column F
        "Accepted Value(s)",	        # Column G
        "Example 1 (Dummy data)",	    # Column H
        "Example 2 (Dummy data)",	    # Column I
        "Example 3 (Dummy data)"        # Column J
    ])
    ws.append(["", "", "", "", "", "", "", "", "", ""])

    # Set cell widths
    ws.column_dimensions["A"].width = 30
    ws.column_dimensions["B"].width = 15
    ws.column_dimensions["C"].width = 30
    ws.column_dimensions["D"].width = 15
    ws.column_dimensions["E"].width = 60
    ws.column_dimensions["F"].width = 15
    ws.column_dimensions["G"].width = 20
    ws.column_dimensions["H"].width = 30
    ws.column_dimensions["I"].width = 30
    ws.column_dimensions["J"].width = 30

    fontname = "Aptos Narrow"
    title_fill = PatternFill(start_color="4F81BD", end_color="4F81BD", fill_type="solid")
    title_fill = PatternFill(start_color="465C66", end_color="465C66", fill_type="solid")
    title_font = Font(color="FFFFFF", bold=False, size=14, name=fontname)
    header_fill = PatternFill(start_color="113377", end_color="113377", fill_type="solid")
    header_fill = PatternFill(start_color="09094E", end_color="09094E", fill_type="solid")
    header_font = Font(color="FFFFFF", bold=False, name=fontname)
    property_font = Font(name=fontname)
    property_name_font = Font(bold=True, name=fontname)

    # format the first rows with the title fill
    for row in ws[1 : 2]:
        for cell in row:
            cell.fill = title_fill
            cell.font = title_font
    for row in ws[2 : ws.max_row]:
        for cell in row:
            cell.fill = title_fill
            cell.font = header_font

    # Inner function to write a property to the worksheet
    def write_property(name, info, level):
        # Extract the type and description of the property
        type = info.get("type", "")
        
        if type == "object":
            write_type(name, info, level + 1)
            return

        type += " " + info.get("format", "")
        type += " " + info.get("comment", "")

        description = info.get("description", "N/A")
        examples = info.get("examples", []) + ['','','']
        mandatory = name in info.get("required", [])
        
        # Append a row to the worksheet
        ws.append([
            name, 
            "M" if mandatory else "O",
            info.get("title", name),
            "-",
            description.rstrip(), # remove last newline from the description
            "-",
            type, 
            examples[0],
            examples[1],
            examples[2]
            ])
        # Indent the first cell of the row just added
        for cell in ws[ws.max_row]:
            cell.font = property_font
        ws[ws.max_row][0].alignment = Alignment(indent=level)
        ws[ws.max_row][0].font = property_name_font

        
    # Inner function to write a type to the worksheet
    def write_type(name, info, level=0):
        if info.get("title"):
            # Append a row for the type itself and set background color to blue
            ws.append([name + ": " + info["title"], "", "", "", "", "", "", "", "", ""])
            for cell in ws[ws.max_row]:
                cell.fill = header_fill
                cell.font = header_font

        for prop_name, prop_info in info.get("properties", {}).items():
            # Extract the type and description of the property
            write_property(prop_name, prop_info, level)


    # Find the specified types in the schema
    for name in types:
        print(name)
        type = schema["components"]["schemas"][name]
        write_type(name, type)


    # Set word wrap for all cells in the description colum
    for cell in ws["A"] :
        cell.alignment = Alignment(vertical="top", indent=cell.alignment.indent)
    for cell in ws["B"] + ws["C"] + ws["D"] + ws["E"] + ws["F"] + ws["G"] + ws["H"] + ws["I"] + ws["J"]:
        cell.alignment = Alignment(vertical="top")
    for cell in ws["E"]:
        cell.alignment = Alignment(wrap_text=True, vertical="top")


if len(sys.argv) < 2:
    print("Usage: python3 generate-excel.py <input-path>")
    print("This script generates an Excel file from a OpenAPI schema.")
    print("")
    print("Example:")
    print("python3 generate-excel pact-openapi-2.2.1-wip.yaml")
    print()
    exit()

# Load the schema from the file
input_path = sys.argv[1]
# input_path = "pact-openapi-2.2.0.yaml"
with open(input_path) as file:
    schema1 = yaml.safe_load(file)
schema = jsonref.replace_refs(schema1, merge_props=True)

# Create a new workbook and select the active worksheet
wb = Workbook()
ws = wb.active
ws.title = "PACT Simplified Data Model"

export_to_excel(ws, schema, ["ProductFootprint"])

# Save the workbook to a file

# change extension to .xlsx using python path manipulation

output_path = os.path.basename(input_path)
output_path = output_path.replace('-openapi-', '-simplified-model-')
output_path = output_path.replace(".yaml", "") + ".xlsx"
output_path = os.path.join(os.path.dirname(input_path), output_path)
print(output_path)
wb.save(output_path)
