
class color:
   DARKCYAN = '\033[36m'
   RED = '\033[31m'
   REDBRIGHT = '\033[91m'
   BOLD = '\033[1m'
   ITALIC = '\033[3m'
   END = '\033[0m'

def box_lines(lines, width):
    topBottomRow = "+" + "-" * width + "+"
    middle = "\n".join("|" + x.ljust(width) + "|" for x in lines)
    return "\n" + color.BOLD + color.RED + "{0}\n{1}\n{0}".format(topBottomRow, middle) + color.END + color.END


def split_line(line, width):
    return [line[i:i+width] for i in range(0, len(line), width)]


def split_msg(msg, width):
    lines = msg.split("\n")
    split_lines = [split_line(line, width) for line in lines]
    return [item for sublist in split_lines for item in sublist] # flatten


def border_msg(msg, width):
    return(box_lines(split_msg(msg, width), width))

def dotted_line():
    print(color.BOLD + "-------------------------------------------------------" + color.END)

def end_line():
	 print(color.BOLD + color.REDBRIGHT + "----------------END GAME------------------" + color.END + color.END)