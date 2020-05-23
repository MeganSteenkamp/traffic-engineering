#!/usr/bin/python3

"""
   Title: COSC 364 Internet Technologies and Engineering - Second Assignment
   Description: A Python3 program to generate an LP file for an optimization problem.
   Author: Isaac Murtagh (Student ID: 78178123)
   Author: Megan Steenkamp (Student ID: 23459587)
   Example run command: python3 file_generator.py 1 2 3
   Date: May 2020
"""

import sys


class FileGenerator:
    """ A class to generate an LP file for a load balancing optimization problem """


    def __init__(self, x, y, z):
        """ A property for each set of constraints in the optimization formulation """
        # Initialization variables
        self.x = x
        self.y = y
        self.z = z
        self.filename = self.set_filename()

        # Lists of strings for LP file output for each constraint
        self.demand = self.demand_constraints()
        self.capp1 = self.capp1_constraints()
        self.capp2 = self.capp2_constraints()
        self.transit = self.transit_constraints()
        self.binary_var = self.binary_var_constraints()
        self.equal_path = self.equal_path_constraints()
        self.bounds = self.bounds_contraints()
        self.binaries = self.binaries_constraints()

        # Output the LP file
        self.write_file()


    def demand_constraints(self):
        """ Returns string with each line being a demand volume constraint
            Demand volume in spec is equal to i+j
        """
        constraints = []
        for i in range(1, self.x + 1):
            for j in range(1, self.z + 1):
                equation = f"\tdem{i}{j}: "
                demand_volumes = []
                for k in range(1, self.y + 1):
                    demand_volumes.append(f"x{i}{k}{j}")
                equation += " + ".join(demand_volumes) + f" = {i + j}"
                constraints.append(equation)
        demand_constraints = "\n".join(constraints)
        demand_constraints += "\n"
        return demand_constraints


    def capp1_constraints(self):
        """ Returns a string with each line being a capacity constraint for the capacity
            from a source node to a transit node
        """
        constraints = []
        for i in range(1, self.x + 1):
            for k in range(1, self.y + 1):
                equation = f"\tcapS{i}{k}: "  # Need S to differentiate between the two capacity constraints
                capp1 = []
                for j in range(1, self.z + 1):
                    capp1.append(f"x{i}{k}{j}")
                equation += " + ".join(capp1) + f" - c{i}{k} <= 0"
                constraints.append(equation)
        capp1_constraints = "\n".join(constraints)
        capp1_constraints += "\n"
        return capp1_constraints


    def capp2_constraints(self):
        """ Returns a string with each line being a capacity constraint for the capacity
            from a transit node to a destination node
        """
        constraints = []
        for j in range(1, self.z + 1):
            for k in range(1, self.y + 1):
                equation = f"\tcapD{k}{j}: "
                capp2 = []
                for i in range(1, self.x + 1):
                    capp2.append(f"x{i}{k}{j}")
                equation += " + ".join(capp2) + f" - d{k}{j} <= 0"
                constraints.append(equation)
        capp2_constraints = "\n".join(constraints)
        capp2_constraints += "\n"
        return capp2_constraints


    def transit_constraints(self):
        """ Returns a string with each line being a transit node load constraint """
        constraints = []
        for k in range(1, self.y + 1):
            equation = f"\ttransit{k}: "
            transit = []
            for i in range(1, self.x + 1):
                for j in range(1, self.z + 1):
                    transit.append(f"x{i}{k}{j}")
            equation += " + ".join(transit) + f" - r <= 0"
            constraints.append(equation)
        transit_constraints = "\n".join(constraints)
        transit_constraints += "\n"
        return transit_constraints


    def binary_var_constraints(self):
        """ Returns a string with each line being a binary variable constraint """
        constraints = []
        for i in range(1, self.x + 1):
            for j in range(1, self.z + 1):
                equation = f"\tbin{i}{j}: "
                constants = []
                for k in range(1, self.y + 1):
                     constants.append(f"u{i}{k}{j}")
                equation += " + ".join(constants)
                equation += " = 2"
                constraints.append(equation)
        binary_constraints = "\n".join(constraints)
        binary_constraints += "\n"
        return binary_constraints

    def equal_path_constraints(self):
        """ Returns a string with each line being an equal path flow constraint """
        constraints = []
        for i in range(1, self.x + 1):
            for j in range(1, self.z + 1):
                for k in range(1, self.y + 1):
                    equation = f"\teqlPath{i}{k}{j}: 2 x{i}{k}{j} - {i + j} u{i}{k}{j} = 0"
                    constraints.append(equation)
        equal_path_constraints = "\n".join(constraints)
        equal_path_constraints += "\n"
        return equal_path_constraints


    def bounds_contraints(self):
        """ Returns a string with each line being a non-negativity constraint.
            This will go under the 'Bounds' heading.
        """
        constraints = {
            "r": {"\tr >= 0"}, 
            "x": set(),
            "c": set(),
            "d": set(),
            }
        for i in range(1, self.x + 1):
            for j in range(1, self.z + 1):
                for k in range(1, self.y + 1): 
                    constraints["x"].add(f"\tx{i}{k}{j} >= 0")
                    constraints["c"].add(f"\tc{i}{k} >= 0")
                    constraints["d"].add(f"\td{k}{j} >= 0")
        equality_constraints = ""
        for values in constraints.values():
            equality_constraints += "\n".join(values)
            equality_constraints += "\n"
        return equality_constraints


    def binaries_constraints(self):
        """ Returns a string with each line being a binary constraint.
            This will go under the 'Binaries' heading.
        """
        constraints = []
        for i in range(1, self.x + 1):
            for j in range(1, self.z + 1):
                for k in range(1, self.y + 1):
                    constraints.append(f"\tu{i}{k}{j}")
        binary_constraints = "\n".join(constraints)
        binary_constraints += "\n"
        return binary_constraints



    def set_filename(self):
        """ Sets the filename to be XYZ.lp"""
        return f"files/{self.x}{self.y}{self.z}.lp"


    def create_file_content(self):
        """ Combines the content of all constraints to create the content for the lp file """
        return ("Minimize \n"
                "\tobj: r\n\n\n"
                "Subject To\n"
                    f"{self.demand}\n"
                    f"{self.capp1}\n"
                    f"{self.capp2}\n"
                    f"{self.transit}\n"
                    f"{self.binary_var}\n"
                    f"{self.equal_path}\n\n"
                "Bounds\n"
                    f"{self.bounds}\n\n"
                "Binaries\n"
                    f"{self.binaries}\n\n"
                "End")


    def write_file(self):
        """ Writes the LP file to output """
        f = open(self.filename, 'w')
        content = self.create_file_content()
        f.write(content)
        f.close()


def validate_inputs():
    """ Validates the the three inputs given for the optimization formulation """
    if (len(sys.argv) != 4):
        sys.exit("Provide 3 input integers (X, Y, Z) separated by a space.\n"
                 "An example of a run command is 'python3 file_generator.py 1 2 3'")
    try:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        z = int(sys.argv[3])
        if y < 2:
            sys.exit(f"An input value of Y={y} is invalid. Y must be greater than 1.")
    except ValueError:
        sys.exit("Please provide integer values only.")

    return x, y, z


def main():
    """Main function to execute program"""

    if __name__ == "__main__":
        x, y, z = validate_inputs()
        file_generator = FileGenerator(x, y, z)
        file_generator


main()
