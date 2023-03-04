lines = int(input())
chemical_compounds = {*()}

for i in range(lines):
    chemical_compounds = chemical_compounds.union(input().split())

print("\n".join(chemical_compounds))