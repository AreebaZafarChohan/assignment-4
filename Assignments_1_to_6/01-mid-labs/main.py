from sample_madlibs import study, motivation, adventure, sci_fi, technology
import random

if __name__ == "__main__":
    m = random.choice([ study, motivation, adventure, sci_fi, technology])
    m.madlib()