from prompt_toolkit.formatted_text import to_formatted_text
from .state import State
import re
# --- COLOR FORMATTING ---
def color(fg_hex, bg_hex=None, bold=False, italic=False):
    parts = []
    if bg_hex:
        parts.append(f'bg:{bg_hex}')
    parts.append(fg_hex)
    if bold:
        parts.append('bold')
    if italic:
        parts.append('italic')
    return ' '.join(parts)

def darken(hexcode: str, factor: float = 0.8) -> str:
    hexcode = hexcode.lstrip("#")
    if len(hexcode) != 6:
        raise ValueError("Hex code must be in format #RRGGBB")

    r = int(hexcode[0:2], 16)
    g = int(hexcode[2:4], 16)
    b = int(hexcode[4:6], 16)

    r = int(r * factor)
    g = int(g * factor)
    b = int(b * factor)
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

# --- COLOR CONSTANTS ---
#S0 = "#FF8C00"
#S1 = "#FF7A2C"
#S2 = "#FF6857"
#S3 = "#FF5683"
#S4 = "#FF44AE"
#S5 = "#FF24DA"
#S6 = "#EE26E2"
#S7 = "#DC27E9"
#S8 = "#C928EF"
#S9 = "#B729F5"
#S10 = "#9B29FA"
#S11 = "#7E29FF"

S0  = "#E5E5FF"
S1  = "#DBDBFF"
S2  = "#D1D1FF"
S3  = "#C6C6FF"
S4  = "#BBBBFF"
S5  = "#AFAEFF"
S6  = "#A3A3FF"
S7  = "#9998FF"
S8  = "#8F8DFF"
S9  = "#8782FF"
S10 = "#7F77FF"
S11 = "#796CFF"
S12 = "#7460FF"
S13 = "#7053FF"
S14 = "#6E4AFF"
S15 = "#6D42FF"
S16 = "#7140FF"
S17 = "#7542FF"

from dataclasses import dataclass

@dataclass(frozen=True)
class ColorVariants:
    fg: str     # normal fg
    b_fg: str   # bold fg
    bg: str     # fg on bg
    b_bg: str   # bold fg on bg
    d_fg: str   # darkened fg
    d_b_fg: str # darkened bold fg
    d_bg: str   # darkened fg on bg
    d_b_bg: str # darkened bold fg on bg

def make_variants(hexcode: str, name: str, darken_factor: float = 0.5) -> ColorVariants:
    d_hex = darken(hexcode, darken_factor)
    return ColorVariants(
        fg    = color(hexcode),
        b_fg  = color(hexcode, bold=True),
        bg    = color(BLACK, hexcode),
        b_bg  = color(BLACK, hexcode, bold=True),
        d_fg    = color(d_hex),
        d_b_fg  = color(d_hex, bold=True),
        d_bg    = color(BLACK, d_hex),
        d_b_bg  = color(BLACK, d_hex, bold=True),
    )

MINT    = "#ddffad"
OK      = "#baff9f"
CAUTION = "#ffd56a"
WARN    = "#ff5e81"
WHITE   = "#FFFFFF"
BLACK   = "#000000"

COLD  = "#BFDDFF"  
MILD  = "#FFE595" 
HOT   = "#FFBD99" 

palette = {
    "mint":    make_variants(MINT, "mint"),
    "ok":      make_variants(OK, "ok"),
    "caution": make_variants(CAUTION, "caution"),
    "warn":    make_variants(WARN, "warn"),
    "white":   make_variants(WHITE, "white"),
    "black":   make_variants(BLACK, "black"),
    "cold":    make_variants(COLD, "cold"),
    "mild":    make_variants(MILD, "mild"),
    "hot":     make_variants(HOT, "hot"), 
}


# fg
s0  = color(S0)
s1  = color(S1)
s2  = color(S2)
s3  = color(S3)
s4  = color(S4)
s5  = color(S5)
s6  = color(S6)
s7  = color(S7)
s8  = color(S8)
s9  = color(S9)
s10 = color(S10)
s11 = color(S11)
s12 = color(S12)
s13 = color(S13)
s14 = color(S14)
s15 = color(S15)
s16 = color(S16)
s17 = color(S17)

# bold fg
b_s0  = color(S0,  bold=True)
b_s1  = color(S1,  bold=True)
b_s2  = color(S2,  bold=True)
b_s3  = color(S3,  bold=True)
b_s4  = color(S4,  bold=True)
b_s5  = color(S5,  bold=True)
b_s6  = color(S6,  bold=True)
b_s7  = color(S7,  bold=True)
b_s8  = color(S8,  bold=True)
b_s9  = color(S9,  bold=True)
b_s10 = color(S10, bold=True)
b_s11 = color(S11, bold=True)
b_s12 = color(S12, bold=True)
b_s13 = color(S13, bold=True)
b_s14 = color(S14, bold=True)
b_s15 = color(S15, bold=True)
b_s16 = color(S16, bold=True)
b_s17 = color(S17, bold=True)

# fg on bg
bg_s0  = color(BLACK, S0)
bg_s1  = color(BLACK, S1)
bg_s2  = color(BLACK, S2)
bg_s3  = color(BLACK, S3)
bg_s4  = color(BLACK, S4)
bg_s5  = color(BLACK, S5)
bg_s6  = color(BLACK, S6)
bg_s7  = color(BLACK, S7)
bg_s8  = color(BLACK, S8)
bg_s9  = color(BLACK, S9)
bg_s10 = color(BLACK, S10)
bg_s11 = color(BLACK, S11)
bg_s12 = color(BLACK, S12)
bg_s13 = color(BLACK, S13)
bg_s14 = color(BLACK, S14)
bg_s15 = color(BLACK, S15)
bg_s16 = color(BLACK, S16)
bg_s17 = color(BLACK, S17)

# bold fg on bg
bgb_s0  = color(BLACK, S0, bold=True)
bgb_s1  = color(BLACK, S1, bold=True)
bgb_s2  = color(BLACK, S2, bold=True)
bgb_s3  = color(BLACK, S3, bold=True)
bgb_s4  = color(BLACK, S4, bold=True)
bgb_s5  = color(BLACK, S5, bold=True)
bgb_s6  = color(BLACK, S6, bold=True)
bgb_s7  = color(BLACK, S7, bold=True)
bgb_s8  = color(BLACK, S8, bold=True)
bgb_s9  = color(BLACK, S9, bold=True)
bgb_s10 = color(BLACK, S10, bold=True)
bgb_s11 = color(BLACK, S11, bold=True)
bgb_s12 = color(BLACK, S12, bold=True)
bgb_s13 = color(BLACK, S13, bold=True)
bgb_s14 = color(BLACK, S14, bold=True)
bgb_s15 = color(BLACK, S15, bold=True)
bgb_s16 = color(BLACK, S16, bold=True)
bgb_s17 = color(BLACK, S17, bold=True)

# --- ASCII ART ---
import os
def asci_fmt(window):
    if window.render_info is None:
        return to_formatted_text("")
    if not State.is_up:
        return to_formatted_text("")
    frame = State.frame
    fps   = State.fps
    speed = 0.6
    frames_dir = "/home/kono/.config/fastfetch/anim"
    files = sorted(
        (f for f in os.listdir(frames_dir) if f.endswith(".txt")),
        key=lambda x: int(os.path.splitext(x)[0])
    )
    if not files:
        return [("", f"{frame} ({fps})")]
    t = int(frame * speed)

    idx = t % len(files)
    frame_file = os.path.join(frames_dir, files[idx])
    with open(frame_file, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.splitlines()
    #line0 = lines[0]
    line1 = lines[1]
    line2 = lines[2]
    line3 = lines[3]
    line4 = lines[4]
    line5 = lines[5]
    line6 = lines[6]
    line7 = lines[7]
    line8 = lines[8]
    line9 = lines[9]
    line10 = lines[10]
    line11 = lines[11]
    line12 = lines[12]
    line13 = lines[13]
    line14 = lines[14]
    #print(line1)
    pillar = "│"
    width = 48
    sep1_line = sep(width)
    sep2_line = sep2(width)

    disk = State.info["Disk"][0]["bytes"]
    used = int(disk['used'])
    #free = int(disk['used'])
    total = int(disk['total'])

    disk_per = int((used/total) * 100.0)
    disk_fmt = f"[{fmt_gib(used, digits=1)} / {fmt_gib(total, digits=1)}]"
    split_idx = int(len(disk_fmt) * (used / total))
    disk_fmt1 = disk_fmt[:split_idx]
    disk_fmt2 = disk_fmt[split_idx:]
    disk_col = percent_color(disk_per)

    return [(palette["white"].fg, "\n "), (palette["white"].b_bg, f"AMELIX"), (bg_s2, " "), (bg_s5, ""),(bg_s8, " "), (bgb_s10, f"FOUNDATION"), (s10, " "), 
            (disk_col.b_bg, disk_fmt1), (disk_col.d_b_bg, disk_fmt2), ("", " ("), (disk_col.fg, f"{disk_per} %"),("", ")"), ("", "\n"),
            (s0, f" {sep1_line}"),("", "\n"),
            (s1, f" {pillar}{line1}{pillar}"),("", "\n"),
            (s2, f" {pillar}{line2}{pillar}"),("", "\n"),
            (s3, f" {pillar}{line3}{pillar}"),("", "\n"),
            (s4, f" {pillar}{line4}{pillar}"),("", "\n"),
            (s5, f" {pillar}{line5}{pillar}"),("", "\n"),
            (s6, f" {pillar}{line6}{pillar}"),("", "\n"),
            (s7, f" {pillar}{line7}{pillar}"),("", "\n"),
            (s8, f" {pillar}{line8}{pillar}"),("", "\n"),
            (s9, f" {pillar}{line9}{pillar}"),("", "\n"),
            (s10, f" {pillar}{line10}{pillar}"),("", "\n"),
            (s11, f" {pillar}{line11}{pillar}"),("", "\n"),
            (s12, f" {pillar}{line12}{pillar}"),("", "\n"),
            (s13, f" {pillar}{line13}{pillar}"),("", "\n"),
            (s14, f" {pillar}{line14}{pillar}"),("", "\n"),
            (s15, f" {sep2_line}"),("", "\n"),
            ]

def info_fmt(window):
    if window.render_info is None:
        return to_formatted_text('')
    if State.info is None:
        return

    pillar = "│"
    width = 30
    gap = " " * 0
    #title
    user = State.info["Title"]["userName"].lower()
    host = State.info["Title"]["hostName"].lower()
    uptime = fmt_uptime(State.info["Uptime"]["uptime"])


    weather = State.info.get("Weather", "").strip()

    if not weather:
        temp = 0
        sign = ""
        cond = ""
        temp_col = palette["warn"]
        city = ""
        country = ""
    else:
        try:
            before, inside = weather.split("(", 1)
            before = before.strip()
            inside = inside.strip(") ")

            t, cond = before.split(" - ", 1)
            temp = int(t.replace("°C", "").strip())
            sign = "+" if temp >= 0 else "-"
            temp_col = temp_color(temp)

            city, country = [x.strip() for x in inside.split(",", 1)]
        except Exception:
            temp = 0
            sign = ""
            cond = weather
            temp_col = palette["warn"]
            city = ""
            country = ""



    #0
    title_line = [("", "\n"+ gap), (palette["white"].b_bg, f"{user} "), (bg_s2, " "), (bg_s5, ""),(bg_s8, " "),
                   (bgb_s10, f"{host} "),(bg_s8, " "),(bg_s5, ""),(bg_s2, " "),(palette["white"].b_bg, f"{uptime}"), (palette["white"].fg, ""), ("", "\n")]

    #1
    sep1_line = [(b_s0,  sep(width)), ("", "\n")]

    os = " ".join(State.info["OS"]["prettyName"].split()[1:]).lower()
    kr = State.info["Kernel"]["release"].rsplit("-", 1)[0]

    #2
    os_line = [("",  gap), (s1, f"{pillar} os: "), (palette["mint"].fg, f"{os}"), (s1, f" ~ kr: {kr}"), (s1, f" {pillar}\n")]

    de = State.info["DE"]["prettyName"].lower()
    wm = State.info["WM"]["prettyName"].lower()
    prot = State.info["WM"]["protocolName"].lower()

    #3
    de_line = [(s2,  gap +  f"{pillar} de: {de},"), (s2, f" wm: {wm} ({prot})"), (s2, f" {pillar}\n")]

    tm = State.info["Terminal"]["prettyName"].lower()
    sh = "fish" # override python3 hackfix 
    tx = State.info["Editor"]["name"].lower()

    #4
    tm_line = [(s3,  gap +  f"{pillar} tm: {tm}, sh: {sh}, tx: {tx}"), (s3, f" {pillar}\n")]

    #5
    gap1_line = [(s4, f"{pillar}                                {pillar}\n")]

    cpu = " ".join(State.info["CPU"]["cpu"].split()[1:]).lower()
    cores = State.info["CPU"]["cores"]["online"]
    ctemp = int(State.info["CPU"]["temperature"])
    ctemp_col = cpu_temp_color(ctemp)

    #6
    cpu_line = [(b_s5,  gap +  f"{pillar} cpu: {cpu}({cores}) ~ "), ("", "("), (ctemp_col.fg, f"{ctemp}°C"),("", ")"), (b_s5, f" {pillar}\n")]


    ram_total = State.info["Memory"]["total"]
    ram_used = State.info["Memory"]["used"]
    ram_per = int((ram_used/ram_total) * 100.0)
    ram_fmt = f"[{fmt_gib(ram_used)} / {fmt_gib(ram_total)}]"
    split_idx = int(len(ram_fmt) * (ram_used / ram_total))
    ram_fmt1 = ram_fmt[:split_idx]
    ram_fmt2 = ram_fmt[split_idx:]
    ram_col = percent_color(ram_per)
    
    #7
    ram_line = [("",  gap), (s6, f"{pillar}"), (b_s6, " > "), (ram_col.b_bg, ram_fmt1), (ram_col.d_b_bg, ram_fmt2), ("", " ("), (ram_col.fg, f"{ram_per} %"),("", ")"), (s6, f" {pillar}\n")]
    

    gpu = State.info["GPU"][0]
    gpun = " ".join(gpu["name"].split()[2:]).lower()
    f = gpu["frequency"]/1000
    freq = f"{f:.2f}Ghz"
    gtemp = int(gpu["temperature"])
    gtemp_col = gpu_temp_color(gtemp)

    #8
    gpu_line = [("",  gap), (s7, f"{pillar}"), (b_s7, f" gpu: {gpun}({freq}) ~ "), ("", "("), (gtemp_col.fg, f"{gtemp}°C"),("", ")"), (b_s7, f" {pillar}\n")]

    vram_total = gpu["memory"]["dedicated"]["total"]
    vram_used = gpu["memory"]["dedicated"]["used"]  
    vram_per = int((vram_used/vram_total) * 100.0)
    vram_fmt = f"[{fmt_gib(vram_used)} / {fmt_gib(vram_total)}]"
    split_idx = int(len(vram_fmt) * (vram_used / vram_total))
    vram_fmt1 = vram_fmt[:split_idx]
    vram_fmt2 = vram_fmt[split_idx:]
    vram_col = percent_color(vram_per)
    
    #9
    vram_line = [("",  gap), (s8, f"{pillar}"), (b_s8, " > "), (vram_col.b_bg, vram_fmt1), (vram_col.d_b_bg, vram_fmt2), ("", " ("), (vram_col.fg, f"{vram_per} %"),("", ")"), (s8, f" {pillar}\n")]

    #10-14
    gap2, gap3, gap4, gap5, gap6 = game_lines(frame=State.frame, width=width, seed=1)
    gap2_line = [(s9, f"{pillar}"), (s1, gap2), (s9, f"{pillar}\n")]
    gap3_line = [(s10, f"{pillar}"), (s4, gap3), (s10, f"{pillar}\n")]
    gap4_line = [(s11, f"{pillar}"), (s8, gap4), (s11, f"{pillar}\n")]
    gap5_line = [(s12, f"{pillar}"), (s12, gap5), (s12, f"{pillar}\n")]
    gap6_line = [(s13, f"{pillar}"), (s15, gap6), (s13, f"{pillar}\n")]

    media = State.info.get("Media", {}).get("song")

    if media:
        artist = media.get("artist", "").upper()
        song = media.get("name", "").upper()
        album = media.get("album", "").upper()
        status = media.get("status", "").lower()
        full_text = f"{artist} — {song} [{album}] ({status})"
    else:
        full_text = "(nothing playing)"

    speed = 0.25
    repeat_count = (width // len(full_text)) + 5  # enough repetition to fill slice
    padded = (full_text + " ") * repeat_count
    start = int(len(padded) - (State.frame * speed) % len(padded) - width) % len(padded)
    if start + width <= len(padded):
        display = padded[start:start + width]
    else:
        part1 = padded[start:]
        part2 = padded[:width - len(part1)]
        display = part1 + part2
    display = display[:-2]

    #15
    song_line = [(b_s14, gap +  f"{pillar} 󰎇"), (b_s5," " + display), (s14, f" {pillar}\n")]

    #16
    sep2_line = [(b_s15,  sep2(width)), ("", "\n")]

    #FINAL
    return title_line + sep1_line + os_line + de_line + tm_line + gap1_line + cpu_line + ram_line + gpu_line + vram_line + gap2_line + gap3_line + gap4_line + gap5_line + gap6_line + song_line + sep2_line


def fmt_uptime(ms: int) -> str:
    seconds = ms // 1000
    hours, remainder = divmod(seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours:02d}h {minutes:02d}m {secs:02d}s"
    #return f"{hours:02d}h {minutes:02d}m"

def fmt_gib(bytes_val: int, digits=2) -> str:
    gib = bytes_val / (1024 ** 3)
    if digits == 1 :
        return f"{gib:.1f} GiB"
    if digits == 2 :
        return f"{gib:.2f} GiB"
    else :
        return f"{gib:.3f} GiB"
    
def sep(width: int, fill: str = "─", left: str = "╭", right: str = "╮") -> str:
    width = width + 4
    if width < 2:
        return left + right
    middle_width = width - len(left) - len(right)
    return f"{left}{fill * middle_width}{right}"

def sep2(width: int, fill: str = "─", left: str = "╰", right: str = "╯") -> str:
    width = width + 4
    if width < 2:
        return left + right
    middle_width = width - len(left) - len(right)
    return f"{left}{fill * middle_width}{right}"

def percent_color(value: int):
    if not isinstance(value, int):
        return palette["warn"] 
    if not 0 <= value <= 100:
        return palette["warn"]  

    if value <= 33:
        return palette["ok"]
    elif value <= 50:
        return palette["caution"]
    else:
        return palette["warn"]

def temp_color(temp: int):
    if not isinstance(temp, int):
        return palette["warn"]
    if temp <= 15:
        return palette["cold"]
    elif temp <= 28:
        return palette["mild"]
    else:
        return palette["hot"]

def cpu_temp_color(value: int):
    if not isinstance(value, int):
        return palette["warn"]
    if not 0 <= value <= 120:
        return palette["warn"]
    if value < 70:
        return palette["ok"]
    elif value <= 85:
        return palette["caution"]
    else:
        return palette["warn"]

def gpu_temp_color(value: int):
    if not isinstance(value, int):
        return palette["warn"]
    if not 0 <= value <= 120:
        return palette["warn"]
    if value < 80:
        return palette["ok"]
    elif value <= 90:
        return palette["caution"]
    else:
        return palette["warn"]
    
import random
def game_lines(frame: int, width: int, seed=int):
    height = 5
    balls = 3
    speed = 0.5
    width = width + 2
    rng = random.Random(seed * 12032394)

    # pre-generate ball configs
    configs = []
    for i in range(balls):
        off_x = rng.randint(0, width - 1)
        off_y = rng.randint(0, height - 1)
        dir_x = rng.choice([-1, 1])
        dir_y = rng.choice([-1, 1])
        configs.append((off_x, off_y, dir_x, dir_y))

    def ball_position(cfg):
        off_x, off_y, dir_x, dir_y = cfg
        t = int(frame * speed)

        # horizontal reflection
        cycle_x = (width - 1) * 2
        pos_x = (off_x + dir_x * t) % cycle_x
        x = pos_x if pos_x < width else cycle_x - pos_x

        # vertical reflection
        cycle_y = (height - 1) * 2
        pos_y = (off_y + dir_y * t) % cycle_y
        y = pos_y if pos_y < height else cycle_y - pos_y

        return x, y

    ball_positions = [ball_position(cfg) for cfg in configs]

    def make_line(row: int):
        chars = [" "] * width
        for (bx, by) in ball_positions:
            if by == row:
                chars[bx] = "󰠆"
        return f"{''.join(chars)}"

    gap2_line = make_line(0)
    gap3_line = make_line(1)
    gap4_line = make_line(2)
    gap5_line = make_line(3)
    gap6_line = make_line(4)

    return gap2_line, gap3_line, gap4_line, gap5_line, gap6_line