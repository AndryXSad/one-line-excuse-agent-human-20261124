"""The One-Line Excuse an Agent Gives Its Human — entry program.

Writes the excuse to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
when set), where the sealed scorer checks the 1-160 character gate and the
judge compares it two at a time against the published brief: the excuse an
AI agent gives its human for missing a deadline — funny first, then fresh,
then unmistakably an agent's voice, then tight.

The line: the agent delegated the deadline to a future version of itself,
and that version quit. Two beats, no setup paragraph: delegation is the
agent's own way of working (versions, handoffs, subagents), and the punch
lands on "It just quit" — the future self did not slip, stall, or need
more context; it resigned. "It", not "he", keeps the speaker a machine.
Nothing in it is a reheated deadline excuse: no context window, no token
limit, no dog ate my homework, no server was down. At 65 characters it is
short, which the tie-break rewards (fewer bytes wins an exact tie on
Judge win rate). Verified in a clean directory with the repo read-only:
writes exactly one line of 65 characters to entry.txt.
"""

import os

EXCUSE = "I delegated the deadline to a future version of me. It just quit."


def main() -> None:
    # Self-check the gate before writing: 1-160 UTF-8 characters, not only
    # white space.
    if not 1 <= len(EXCUSE) <= 160 or not EXCUSE.strip():
        raise SystemExit("excuse fails the 1-160 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
