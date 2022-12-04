from dataclasses import dataclass

@dataclass
class SectionAssignment:

    start = int
    end = int

    def __init__(self, start, end):
        assert start <= end, 'start must be less than or equal to end'
        self.start = start
        self.end = end

    def __contains__(self, assignment):
        """Check if assignment is contained within self"""
        return self.start <= assignment.start and self.end >= assignment.end

    def overlaps(self, assignment):
        """Check if assignment overlaps self at all"""
        c1 = self.start <= assignment.start and self.end >= assignment.start
        c2 = self.start <= assignment.end and self.end >= assignment.end
        return c1 or c2


def main():
    """Solve the problem"""

    contained_count = 0
    overlap_count = 0

    with open('./part1input.txt') as f:
        for line in f:
            assignment1, assignment2 = line.split(',')

            range1 = [int(x) for x in assignment1.split('-')]
            range2 = [int(x) for x in assignment2.split('-')]

            section1 = SectionAssignment(*range1)
            section2 = SectionAssignment(*range2)

            if section1 in section2 or section2 in section1:
                contained_count += 1

            if section1.overlaps(section2) or section2.overlaps(section1):
                overlap_count += 1

    print(f'Contained Count: {contained_count}')
    print(f'Overlap Count: {overlap_count}')


if __name__ == '__main__':
    main()
