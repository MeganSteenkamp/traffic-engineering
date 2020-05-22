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
        """ A property for each constraint in the optimization formulation """
        self.x = x
        self.y = y
        self.z = z
        self.filename = ""
        self.set_filename()

        # Lists of strings for LP file output for each constraint
        self.demand = ""
        self.capp1 = ""
        self.capp2 = ""
        self.transit = ""
        self.binary_var = ""
        self.equal_path = ""
        self.bounds = ""
        self.binaries = ""


    def demand_constraints(self):
        """ Generates string with each line being a demand volume constraint """
        # I think we can just output a multi-line string at the end of each method
        # by using something like:
        # self.demand '\n'.join(demand_constraints)
        pass


    def capp1_constraints(self):
        """ Generates a string with each line being a capacity constraint for the capacity
            from a source node to a transit node
        """
        pass


    def capp2_constraints(self):
        """ Generates a string with each line being a capacity constraint for the capacity
            from a transit node to a destination node
        """
        pass


    def transit_constraints(self):
        """ Generates a string with each line being a transit node load constraint """
        pass


    def binary_var_constraints(self):
        """ Generates a string with each line being a binary variable constraint """
        pass


    def equal_path_constraints(self):
        """ Generates a string with each line being an equal path flow constraint """
        pass


    def bounds(self):
        """ Generates a string with each line being a non-negativity constraint """
        pass


    def binaries(self):
        """ Generates a string with each line being a binary constraint.
            This will go under the 'Binaries' heading.
        """
        pass


    def set_filename(self):
        """ Sets the filename to be XYZ.lp"""
        self.filename = f"{self.x}{self.y}{self.z}.lp"


    def create_file_content(self):
        """ Combines the content of all constraints to create the content for the lp file """
        # TODO: Decide whether we need r >-= 0 constraint
        return \
            f"""Minimize
                obj: r
                Subject To
                {self.demand}
                {self.capp1}
                {self.capp2}
                {self.transit}
                {self.binary_var}
                {self.equal_path}
                Bounds
                {self.bounds}
                0 <= r
                Binaries
                {self.binaries}
                End
            """


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
