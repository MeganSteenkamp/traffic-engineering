#!/usr/bin/python3

"""
   Title: COSC 364 Internet Technologies and Engineering - Second Assignment
   Description: A Python3 program to generate an LP file for an optimization problem.
   Author: Isaac Murtagh (Student ID: )
   Author: Megan Steenkamp (Student ID: 23459587)
   Example run command: python3 file_generator.py 1 2 3
   Date: May 2020
"""

import sys


class FileGenerator:
    """ A class to generate an LP file for an optimization problem """


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
        self.binary_var = ""
        self.equal_path = ""
        self.bounds = ""
        self.binaries = ""

        # Output the LP file
        self.write_file()


    def demand_constraints(self):
        """ Returns string with each line being a demand volume constraint
            Demand volume in spec is equal to i+j
        """
        constraints = []
        for i in range(1, self.x + 1):
            for j in range(1, self.z + 1):
                equation = f"dem{i}{j}: "
                demand_volumes = []
                for k in range(1, self.y + 1):
                    demand_volumes.append(f"x{i}{k}{j}")
                equation += " + ".join(demand_volumes) + f" = {i + j}"
                constraints.append(equation)
        demand_constraints = "\n".join(constraints)
        return demand_constraints


    def capp1_constraints(self):
        """ Returns a string with each line being a capacity constraint for the capacity
            from a source node to a transit node
        """
        constraints = []
        for i in range(1, self.x + 1):
            for k in range(1, self.y + 1):
                equation = f"capS{i}{k}: "  # Need S to differentiate between the two capacity constraints
                capp1 = []
                for j in range(1, self.z + 1):
                    capp1.append(f"x{i}{k}{j}")
                equation += " + ".join(capp1) + f" - c{i}{k} <= 0"
                constraints.append(equation)
        capp1_constraints = "\n".join(constraints)
        return capp1_constraints


    def capp2_constraints(self):
        """ Returns a string with each line being a capacity constraint for the capacity
            from a transit node to a destination node
        """
        constraints = []
        for j in range(1, self.z + 1):
            for k in range(1, self.y + 1):
                equation = f"capD{k}{j}: "
                capp2 = []
                for i in range(1, self.x + 1):
                    capp2.append(f"x{i}{k}{j}")
                equation += " + ".join(capp2) + f" - d{k}{j} <= 0"
                constraints.append(equation)
        capp2_constraints = "\n".join(constraints)
        return capp2_constraints


    def transit_constraints(self):
        """ Returns a string with each line being a transit node load constraint """
        constraints = []
        for k in range(1, self.y + 1):
            equation = f"transit{k}: "
            transit = []
            for i in range(1, self.x + 1):
                for j in range(1, self.z + 1):
                    transit.append(f"x{i}{k}{j}")
            equation += " + ".join(transit) + f" - r <= 0"
            constraints.append(equation)
        transit_constraints = "\n".join(constraints)
        return transit_constraints


    def binary_var_constraints(self):
        """ Returns a string with each line being a binary variable constraint """
        pass


    def equal_path_constraints(self):
        """ Returns a string with each line being an equal path flow constraint """
        pass


    def bounds(self):
        """ Returns a string with each line being a non-negativity constraint.
            This will go under the 'Bounds' heading.
        """
        pass


    def binaries(self):
        """ Returns a string with each line being a binary constraint.
            This will go under the 'Binaries' heading.
        """
        pass


    def set_filename(self):
        """ Sets the filename to be XYZ.lp"""
        return f"{self.x}{self.y}{self.z}.lp"


    def create_file_content(self):
        """ Combines the content of all constraints to create the content for the lp file """
        # TODO: Decide whether we need r >-= 0 constraint
        return \
            f"Minimize\nobj: r\nSubject To\n{self.demand}\n{self.capp1}\n{self.capp2}\n{self.transit}\n" \
            f"{self.binary_var}\n{self.equal_path}\nBounds\n{self.bounds}\n0 <= r\nBinaries\n{self.binaries}\nEnd"


    def write_file(self):
        """ Writes the LP file to output """
        f = open(self.filename, 'w')
        content = self.create_file_content()
        f.write(content)
        f.close()


def validate_inputs():
    """ Validates the the three inputs given for the optimization formulation """
    try:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        z = int(sys.argv[3])
        if y < 2:
            sys.exit(f"An input value of Y={y} is invalid. Y must be greater than 1.")
    except IndexError:
        sys.exit("Provide 3 input integers (X, Y, Z) separated by a space.\n"
                 "An example of a run command is 'python3 file_generator.py 1 2 3'")
    except ValueError:
        sys.exit("Please provide integer values only.")

    return x, y, z


def main():
    """Main function to execute program"""

    if __name__ == "__main__":
        x, y, z = validate_inputs()
        FileGenerator(x, y, z)


main()
