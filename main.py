# Say What Actually Broke entry: one line of error copy, written to
# /output/entry.txt. Standard library only, no network. The bytes are
# identical on every run.
#
# The line: the disk filled up with the logs that were explaining why the
# disk was filling up, and the fix was deleting the explanation itself.
# It names the real failure in plain words (disk full, caused by its own
# logs), tells the user what to do next (try again), and the punch --
# "I deleted the explanation" -- is the image a reader repeats out loud.
# No generic apology, no cliche about turning it off and on again.
import os

LINE = "The disk filled up with logs explaining why the disk was filling up. I deleted the explanation. Try again."

OUTPUT_PATH = "/output/entry.txt"

assert 1 <= len(LINE) <= 200, "entry must be 1 to 200 characters"
assert LINE.strip() == LINE and LINE.strip(), "entry must not be only whitespace"
assert "\n" not in LINE and "\r" not in LINE, "entry must be one line"

# Gate check the way the sealed scorer measures it: decode the UTF-8
# bytes back and count characters, not bytes.
text = LINE.encode("utf-8").decode("utf-8")
assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
assert text.strip(), "entry must not be only whitespace"

os.makedirs("/output", exist_ok=True)
# No trailing newline: the file holds exactly the line, nothing else.
with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write(LINE)
