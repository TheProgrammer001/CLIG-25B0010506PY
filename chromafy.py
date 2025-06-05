"""
CLIU-24A0020901PY — Terminal text formatter for colored and styled output

This module provides a function to format strings with ANSI escape codes
to display colors and text attributes (like bold) in the terminal.

Functions:
- format(text: str, attribute: int = None, foreground: list[int] = None, background: list[int] = None) -> str:
    Returns the input text wrapped in ANSI escape codes to apply
    optional styles such as text attribute (e.g. bold), foreground color,
    and background color specified as RGB lists.

Usage example:
    print(format("Hello World", attribute=1, foreground=[255,0,0], background=[255,255,255]))

Author: Dr. Programmer, 2024
"""


# print("\033[1;38;2;255;0;0;48;2;0;255;255mHello World!\033[0m")

def format(text: str, attribute: int = None, foreground: list[int] = None, background: list[int] = None):
    """
        Format a text string with ANSI escape codes for terminal styling.

        Args:
            text (str): The text to be formatted.
            attribute (int, optional): Text attribute code (e.g., 1 for bold).
            foreground (list[int], optional): RGB color for text foreground as [R, G, B].
            background (list[int], optional): RGB color for text background as [R, G, B].

        Returns:
            str: The formatted string with ANSI codes that apply the requested styles.
    """

    reset = "\033[0m"
    esc_seq = "\033["
    format_code = []

    if attribute:
        format_code.append(attribute)

    if foreground:
        format_code.append(f"38;2;{';'.join(map(str, foreground))}")

    if background:
        format_code.append(f"48;2;{';'.join(map(str, background))}")

    if format_code:
        esc_seq += ';'.join(map(str, format_code)) + 'm'

        return f"{esc_seq}{text}{reset}"

    else:
        return text

    # out = f"\033[{attribute};38;2;{';'.join(map(str, foreground))};48;2;{';'.join(map(str, background))}m{text}\033[0m"
    # print(out)

if __name__ == "__main__":
    print(format("Hello World", 1, [255,0,0], [255, 255, 255]))
    print(format("Hello"))
