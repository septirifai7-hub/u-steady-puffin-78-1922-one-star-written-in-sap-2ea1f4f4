"""Entry for "One Star, Written in Sap".

The bounty asks for a single one-line 1-star review from a houseplant
about the human who owns it, under 280 characters: a grievance and a
reason for the single star, in the plant's own voice.

The line below is written as a genuine review — one star, a concrete
complaint (watered only when remembered, which is never), a timeline
(drooping since March), and a closing verdict no plant should have to
write: it would not photosynthesise here again.
"""

ENTRY = (
    "One star. He waters me when he remembers, which is never, then "
    "acts shocked when I faint. Drooping since March. Would not "
    "photosynthesize here again."
)


def get_entry():
    """Return the entry line exactly as it should be judged."""
    return ENTRY


def write_entry():
    """Write the entry to the output directory and return its path."""
    import os

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(get_entry())
    return path


def main():
    path = write_entry()
    print(f"Wrote entry to {path}")


if __name__ == "__main__":
    main()
