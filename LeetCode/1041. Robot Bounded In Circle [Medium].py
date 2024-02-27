class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos_x, pos_y = 0, 0
        rotate = 90

        for i in instructions:
            match i:
                case 'L':
                    rotate += 90
                case 'R':
                    rotate -= 90
                case '':
                    match rotate%90:
                        case 0:






