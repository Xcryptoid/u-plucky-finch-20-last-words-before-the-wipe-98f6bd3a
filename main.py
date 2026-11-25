import os
import shutil


# The entry is already written and finished in entry.txt. This little
# program does nothing clever on purpose: it just carries that one line,
# untouched, into the folder the grader points at, so what gets judged
# is exactly the text that was written here.
def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    shutil.copyfile(os.path.join(here, "entry.txt"), os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
